import asyncio
import requests
import random
import threading
from bleak import BleakScanner

SERVER_URL = "http://172.19.119.30:1234/receive"
AREA_NAME = "CB11.04.400"
DEVICES = {}


def simple_callback(device, advertisement_data):
    global DEVICES
    DEVICES[device] = "found"
    # name = advertisement_data.local_name if advertisement_data.local_name else None
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
    global DEVICES
    while True:
        print("(re)starting scanner")
        async with scanner:
            await asyncio.sleep(5.0)
        fire_and_forget(SERVER_URL, json={'name': AREA_NAME, 'device_count': len(DEVICES)})
        DEVICES = {}


asyncio.run(main())
