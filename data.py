from item_list import Item_ammount
import requests


URL = "https://api.hypixel.net/skyblock/auctions"

class Data:

    def __init__(self):
        self.list = {}
        self.get_data()
    
    def check_if_key_exists(self, key):
        if key in self.list:
            return True
        else:
            return False
    
    def add(self, name):
        self.list[name] = Item_ammount(name)

    def get_data(self):
        data_for_page = requests.get(URL).json()
        page = data_for_page["totalPages"]

        for pages in range(page):
            datas = requests.get(f"{URL}?page={pages}").json()

            for data in datas["auctions"]:
                bin = data["bin"]
                if (bin != True):
                    continue

                name = data["item_name"]
                if(not self.check_if_key_exists(name)):
                    self.add(name)
                
                price = data["starting_bid"]
                uuid = data["uuid"]
                self.list[name].add(uuid, price)
    