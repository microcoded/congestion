import asyncio
import requests
import random
import threading
from bleak import BleakScanner

DEVICE_COUNT = 0
SERVER_URL = "http://172.19.119.30:1234/receive"
AREA_NAME = "CB11.04.400"

AREA_LIST = ["test", "bark", "cat", "dog", "Real UTS Study room", "Busy", "Server Crasher", "Not", "Wifi",
             "My Pants", "UTS Green", "More areas", "I need more names", "Thinking sucks", "😳", "😛",
             "😥", "🥸", "🤠", "Alumni Green", "Cooker", "Milo", "afhlawfjla", "carpark", "ajfkjawfkl", "こんばんは",
             "(；ﾟДﾟ)", "Boop",
             "AJW "
              "KFLHWAKLF JAWKLFJAW "
             "LKFJAWLK FJAWKLFJ LAWKFJ LKWAJFLKAWFJ "
             "KALWFJA KLWFJ KLAWFJKLAWFJKL  AWFJLKAWFJKLAWJFLKAWJFKL "
             "AWFJAWK LFJL KAWJFK LAWFJKLAWJFKL AWFJAWKLFJALKWFJAKLWFJAWKLFJLKAWJF "
             "KAWLFJAWKLFJ AWKLF JA WLKFJAWKLF JAWKLFJ AWKLFJ AWKLFJ AWKLFJA \n\n\n\n\n\n\n\n\nWKLFJAWKLFJA",
             "7", "", " ", 69, "a", "a", 10, "10"]



def simple_callback(device, advertisement_data):
    global DEVICE_COUNT
    DEVICE_COUNT += 1
    name = advertisement_data.local_name if advertisement_data.local_name else None
    # print(f"{device.address}: {name}")
    #
    # print(f"    Tx Power: {advertisement_data.rssi} dBm")
    #
    # if advertisement_data.manufacturer_data:
    #     for manufacturer_id, value in advertisement_data.manufacturer_data.items():
    #         print(f"    Manufacturer ID: {manufacturer_id}")
    #         print(f"    Manufacturer data: {value.hex()}")
    #
    # if advertisement_data.service_uuids:
    #     print(f"    Service UUID: {advertisement_data.service_uuids}")
    # if advertisement_data.service_data:
    #     print(f"    Service data: {advertisement_data.service_data}")


def request_task(url, data):
    try:
        requests.post(url, json=data)
    except:
        print(f"Update failed for {data['name']}")


def fire_and_forget(url, json):
    threading.Thread(target=request_task, args=(url, json)).start()


async def main():
    scanner = BleakScanner(
        simple_callback
    )
    global DEVICE_COUNT
    while True:
        print("(re)starting scanner")
        async with scanner:
            await asyncio.sleep(5.0)
        print(f"Device count: {DEVICE_COUNT}")
        fire_and_forget(SERVER_URL, json={'name': AREA_NAME, 'device_count': DEVICE_COUNT})

        for area in AREA_LIST:
            if area == "My Pants":
                rand_num = random.randrange(1, 21)
            else:
                rand_num = random.randrange(0, 1001)
            print(f"{area} count: {rand_num}")
            fire_and_forget(SERVER_URL, json={'name': area, 'device_count': rand_num})
        DEVICE_COUNT = 0


asyncio.run(main())
