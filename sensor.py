import asyncio
import requests
from bleak import BleakScanner

SERVER_URL = "http://172.19.119.30:1234/receive"
AREA_NAME = "CB11.04.400"
DEVICES = {}


def simple_callback(device, advertisement_data):
    global DEVICES
    DEVICES[device.address] = True


async def main():
    scanner = BleakScanner(
        simple_callback
    )
    global DEVICES
    while True:
        print("(re)starting scanner")
        async with scanner:
            await asyncio.sleep(5.0)
        print(f"Device count: {len(DEVICES)}")
        data = {'name': AREA_NAME, 'device_count': len(DEVICES)}
        try:
            requests.post(SERVER_URL, json=data)
        except requests.exceptions.ConnectTimeout as error:
            print(f"Update failed for {data['name']}")
        DEVICES = {}


asyncio.run(main())
