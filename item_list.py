class Item:
    def __init__(self, uuid, price):
        self.uuid = uuid
        self.price = price

class Item_ammount:
    def __init__(self, name):
        self.items = []
        self.name = name
        self.average = 0

    def add(self, uuid, price):
        self.items.append(Item(uuid=uuid, price=price))

    def calculate_min_average(self):
        prices = []
        for i in self.items:
            prices.append(i.price)
        prices.sort()
        average = 0
        for i in prices:
            average += i
        average = average / len(prices)
        self.average = int(round(average, 0))
