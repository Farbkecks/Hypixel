import requests

search = input("search: ")

url = "https://api.hypixel.net/skyblock/auctions"
data = requests.get(url).json()
page = data["totalPages"]

for pages in range(page):
    datas = requests.get(f"{url}?page={pages}").json()

    for data in datas["auctions"]:
        name = data["item_name"]
        bin = data["bin"]

        if name == search and bin == True:
            price = data["starting_bid"]
            uuid = data["uuid"]
            print(f"{name}: price: {price}, uuid: {uuid}")
