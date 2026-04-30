from enum import Enum
from typing import Dict, Optional

import time


class ZoneQueueException(Exception):
    """Base exception for ZoneQueue"""
    pass

class QueueFullException(ZoneQueueException):
    """Raised when attempting to add to a full queue"""
    pass

class InvalidZoneException(ZoneQueueException):
    """Raised when an invalid zone is specified"""
    pass

class InvalidItemException(ZoneQueueException):
    """Raised when invalid item data is provided"""
    pass


class ZoneType(Enum):
    RED = 3
    YELLOW = 2
    GREEN = 1


class ZoneQueue:
    def __init__(self,
                 red_timeout: int = 60,
                 yellow_timeout: int = 300,
                 green_timeout: int = 900,
                 max_zone_size: Dict[ZoneType, int] = None
                 ):
        self.zones = {
            ZoneType.RED: [],
            ZoneType.YELLOW: [],
            ZoneType.GREEN: []
        }
        self.timeouts = {
            ZoneType.RED: red_timeout,
            ZoneType.YELLOW: yellow_timeout,
            ZoneType.GREEN: green_timeout
        }
        self.max_sizes = max_zone_size or {
            ZoneType.RED: 100,
            ZoneType.YELLOW: 300,
            ZoneType.GREEN: 500
        }
        self.items_processed = {
            ZoneType.RED: 0,
            ZoneType.YELLOW: 0,
            ZoneType.GREEN: 0
        }


    def enqueue(self, item: dict, zone: ZoneType) -> None:
        if zone not in self.zones:
            raise InvalidZoneException(f"Invalid zone: {zone}")
        if len(self.zones[zone]) >= self.max_sizes[zone]:
            raise QueueFullException(f"{zone.name} zone is at capacity")
        if not all(k in item for k in ('id', 'type', 'data', 'timestamp')):
            raise InvalidItemException("Item must contain 'id', 'type', 'data', and 'timestamp'")
        if item['type'] not in ['TRADE', 'RISK', 'REPORT']:
            raise InvalidItemException(f"Invalid item type: {item['type']}. Must be 'TRADE', 'RISK', or 'REPORT'")
        
        self.zones[zone].append(item)


    def dequeue(self) -> Optional[dict]:
        curr_time = time.time()
        for zone in sorted([v for v in ZoneType], key=lambda z: z.value, reverse=True):
            timeout = self.timeouts[zone]
            for i, item in enumerate(self.zones[zone]):
                if curr_time - item['timestamp'] <= timeout:
                    self.items_processed[zone] += 1
                    return self.zones[zone].pop(i)
        return None


    def get_health_status(self) -> dict:
        total_items = 0
        total_capacity = 0
        status = {}
        for zone in sorted([v for v in ZoneType], key=lambda z: z.value, reverse=True):
            items = self.zones[zone]

            count = len(items)
            total_items += count

            total_capacity += self.max_sizes[zone]

            current_time = time.time()
            wait_times = [current_time - item['timestamp'] for item in items]
            avg = sum(wait_times) / len(wait_times) if wait_times else 0.0

            expired_count = sum(1 for item in items if time.time() - item['timestamp'] > self.timeouts[zone])
            
            load_percentage = (count / self.max_sizes[zone]) * 100
            
            status[zone] = {
            'current_items': count,
            'items_processed': self.items_processed[zone],
            'avg_wait_time': avg,
            'expired_items': expired_count,
            'load_percentage': load_percentage
            }

        total_load_pct = (total_items / total_capacity * 100) if total_capacity > 0 else 0.0

        return {
            'total_items': total_items,
            'total_load_percentage': total_load_pct,
            'zones': status
        }
    

    def cleanup_expired(self) -> list:
        curr_time = time.time()
        result = []
        for zone in sorted([v for v in ZoneType], key=lambda z: z.value, reverse=True):
            timeout = self.timeouts[zone]
            for i in range(len(self.zones[zone]) - 1, -1, -1):
                item = self.zones[zone][i]
                if curr_time - item['timestamp'] > timeout:
                    result.append(self.zones[zone].pop(i))
        
        return result
