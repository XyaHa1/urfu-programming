from dataclasses import dataclass
from typing import Optional, Tuple, Iterator, List
from enum import Enum


class DeveloperSpecialization(Enum):
    """Developer specializations in Decimal Precision"""
    CORE_ENGINE = "Trading Engine Developer"
    HFT = "High-Frequency Trading Engineer"
    DATA = "Data Engineer"
    REALTIME = "Real-time Analytics Engineer"
    INFRASTRUCTURE = "Infrastructure Engineer"


@dataclass
class Developer:
    name: str
    specialization: DeveloperSpecialization
    years_experience: int
    team_lead: bool = False

    def __post_init__(self):
        if not isinstance(self.specialization, DeveloperSpecialization):
            raise ValueError(
                f"Invalid specialization. Must be one of: "
                f"{', '.join([s.value for s in DeveloperSpecialization])}"
            )
        if self.years_experience < 0:
            raise ValueError("Years of experience cannot be negative")


class DeveloperNode:    
    def __init__(self, developer: Developer):
        self.developer = developer
        self.next: Optional['DeveloperNode'] = None
        self.prev: Optional['DeveloperNode'] = None


class CircularDeveloperList:
    def __init__(self):
        self.head: Optional[DeveloperNode] = None
        self.size = 0
        self._history: List[dict] = []
        self._history_max = 10
        self._recording_history = True

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[Developer]:
        if self.size == 0:
            return
        
        current = self.head
        for _ in range(self.size):
            yield current.developer
            current = current.next

    def _add_history_entry(self, operation: str, details: dict) -> None:
        if not self._recording_history:
            return
        entry = {
            "operation": operation,
            "details": details,
            "size_after": self.size
        }
        
        self._history.append(entry)
        
        if len(self._history) > self._history_max:
            self._history = self._history[-self._history_max:]

    def get_history(self) -> List[dict]:
        return self._history.copy()

    def add_developer(self, developer: Developer, position: Optional[int] = None) -> bool:

        new_node = DeveloperNode(developer)
        
        if self.size == 0:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.size = 1
            return True
        
        if position is None:
            position = self.size
        
        position = position % self.size
        
        if position == 0:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self._get_node_at_index(position)
            
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        
        self.size += 1
        
        self._add_history_entry("add_developer", {
            "name": developer.name,
            "specialization": developer.specialization.value,
            "position": position
        })
        
        return True
    
    def _get_node_at_index(self, index: int) -> DeveloperNode:
        if self.size == 0:
            raise IndexError("Cannot get node from empty list")
        
        index = index % self.size
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current
    
    def rotate_team(self, steps: int, section: Optional[Tuple[int, int]] = None) -> None:
        if self.size == 0:
            self._add_history_entry("rotate_team", {
                "steps": steps,
                "section": section
            })
            return
        
        if self.size == 1:
            self._add_history_entry("rotate_team", {
                "steps": steps,
                "section": section
            })
            return

        if section is None:
            original_steps = steps
            steps = steps % self.size
            if steps > 0:
                for _ in range(steps):
                    self.head = self.head.prev
            elif steps < 0:
                steps = abs(steps)
                for _ in range(steps):
                    self.head = self.head.next
            
            self._add_history_entry("rotate_team", {
                "steps": original_steps,
                "section": section
            })
            return

        start, end = section
        
        if start < 0 or end < 0:
            raise ValueError("Section boundaries cannot be negative")
        
        if start > end:
            raise ValueError(
                f"Invalid section: start ({start}) must be <= end ({end})"
            )
        
        if start >= self.size or end >= self.size:
            raise ValueError(
                f"Section boundaries out of range. List size: {self.size}"
            )

        section_length = end - start + 1
        
        if section_length <= 1:
            self._add_history_entry("rotate_team", {
                "steps": steps,
                "section": section
            })
            return

        steps = steps % section_length
        if steps == 0:
            self._add_history_entry("rotate_team", {
                "steps": steps,
                "section": section
            })
            return


        if start == 0:
            node_before = self.head.prev
        else:
            node_before = self._get_node_at_index(start - 1)
        
        node_after = self._get_node_at_index((end + 1) % self.size)

        section_nodes = []
        current = self._get_node_at_index(start)
        for _ in range(section_length):
            section_nodes.append(current)
            current = current.nxt

        section_nodes = section_nodes[-steps:] + section_nodes[:-steps]

        for i in range(len(section_nodes)):
            section_nodes[i].next = section_nodes[(i + 1) % len(section_nodes)]
            section_nodes[i].prev = section_nodes[(i - 1) % len(section_nodes)]

        node_before.next = section_nodes[0]
        section_nodes[0].prev = node_before

        section_nodes[-1].next = node_after
        node_after.prev = section_nodes[-1]

        if start == 0:
            self.head = section_nodes[0]

        self._add_history_entry("rotate_team", {
            "steps": steps,
            "section": section
        })

    def swap_teams(self, section1: Tuple[int, int], section2: Tuple[int, int]) -> None:
        if self.size == 0:
            return

        start1, end1 = section1
        start2, end2 = section2

        if start1 < 0 or end1 < 0 or start2 < 0 or end2 < 0:
            raise ValueError("Section boundaries cannot be negative")

        if start1 > end1:
            raise ValueError(
                f"Invalid section1: start ({start1}) must be <= end ({end1})"
            )
        if start2 > end2:
            raise ValueError(
                f"Invalid section2: start ({start2}) must be <= end ({end2})"
            )

        if end1 >= self.size or end2 >= self.size:
            raise ValueError(
                f"Section boundaries out of range. List size: {self.size}"
            )

        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        if len1 != len2:
            raise ValueError(
                f"Sections must be of equal size. "
                f"Section1 size: {len1}, Section2 size: {len2}"
            )

        sections_overlap = not (end1 < start2 or end2 < start1)
        
        if sections_overlap:
            raise ValueError(
                f"Sections overlap: section1 ({start1}, {end1}) and "
                f"section2 ({start2}, {end2})"
            )

        nodes1 = []
        current = self._get_node_at_index(start1)
        for _ in range(len1):
            nodes1.append(current)
            current = current.next

        nodes2 = []
        current = self._get_node_at_index(start2)
        for _ in range(len2):
            nodes2.append(current)
            current = current.next

        for i in range(len1):
            nodes1[i].developer, nodes2[i].developer = nodes2[i].developer, nodes1[i].developer

        self._add_history_entry("swap_teams", {
            "section1": section1,
            "section2": section2
        })

    def group_by_specialization(self, spec: DeveloperSpecialization) -> None:
        if self.size == 0:
            return

        if not isinstance(spec, DeveloperSpecialization):
            raise ValueError(
                f"Invalid specialization. Must be one of: "
                f"{', '.join([s.value for s in DeveloperSpecialization])}"
            )

        target_devs = []
        remaining_devs = []
        
        for dev in self:
            if dev.specialization == spec:
                target_devs.append(dev)
            else:
                remaining_devs.append(dev)

        if not target_devs:
            self._add_history_entry("group_by_specialization", {
                "specialization": spec.value
            })
            return

        if not remaining_devs:
            self._add_history_entry("group_by_specialization", {
                "specialization": spec.value
            })
            return

        self._recording_history = False
        
        self.head = None
        self.size = 0

        for dev in remaining_devs:
            self.add_developer(dev)
        
        for dev in target_devs:
            self.add_developer(dev)

        self._recording_history = True

        self._add_history_entry("group_by_specialization", {
            "specialization": spec.value
        })

    def validate_arrangement(self) -> bool:
        if self.size == 0:
            return True
        
        if self.size == 1:
            return True

        current = self.head
        
        for _ in range(self.size):
            if current.developer.team_lead and current.next.developer.team_lead:
                return False
            current = current.next
        
        if self.size >= 3:
            current = self.head
            
            for _ in range(self.size):
                p1 = current.developer.years_experience
                p2 = current.next.developer.years_experience
                p3 = current.next.next.developer.years_experience

                if not (p1 >= 5 or p2 >= 5 or p3 >= 5):
                    return False
                
                current = current.next

        return True
    