class Item:
    def __init__(self, uuid, price):
        self.uuid = uuid
        self.price = price

class Item_list:
    def __init__(self, name):
        self.items = []
        self.name = name

    def add(self, uuid, price):
        self.items.append(Item(uuid=uuid, price=price))