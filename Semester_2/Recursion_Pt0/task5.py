class Order:
    def __init__(self, order_id, next=None):
        self.order_id = order_id
        self.next = next

    def __repr__(self):
        return f"Order(id={self.order_id})"


class OrderList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _validator_unique(self, order_id):
        curr = self.head
        while curr is not None:
            if curr.order_id == order_id:
                raise ValueError("Order already exists")
            curr = curr.next

    def add_order(self, order_id):
        self._validator_unique(order_id)
        
        new_node = Order(order_id)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse(self):
        curr = self.head
        prev = None
        self.tail = self.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        self.head = prev

    def __repr__(self):
        if self.head is None:
            return 'Empty Order List'
        
        st = []
        curr = self.head
        while curr is not None:
            st.append(repr(curr))
            curr = curr.next

        return " -> ".join(st)


if __name__ == "__main__":
    obj = OrderList()
    obj.add_order(10)
    obj.add_order(20)
    obj.add_order(30)
    obj.add_order(40)
    obj.add_order(50)
    print(obj)
    obj.reverse()
    print(obj)

    obj.reverse()
    print(obj)
    
