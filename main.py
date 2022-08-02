from data import Data

if __name__ == '__main__':
    items = Data().list
    for item in items:
        items[item].calculate_min_average()

    print("done")


"""
https://sky.coflnet.com/flipper
https://skyblockutils.com/
https://sky.coflnet.com/item/
"""





