import asyncio
from bleak import BleakScanner

DEVICE_COUNT = 0


def simple_callback(device, advertisement_data):
    global DEVICE_COUNT
    DEVICE_COUNT += 1
    name = advertisement_data.local_name if advertisement_data.local_name else None
    print(f"{device.address}: {name}")

    print(f"    Tx Power: {advertisement_data.rssi} dBm")

    if advertisement_data.manufacturer_data:
        for manufacturer_id, value in advertisement_data.manufacturer_data.items():
            print(f"    Manufacturer ID: {manufacturer_id}")
            print(f"    Manufacturer data: {value.hex()}")

    if advertisement_data.service_uuids:
        print(f"    Service UUID: {advertisement_data.service_uuids}")
    if advertisement_data.service_data:
        print(f"    Service data: {advertisement_data.service_data}")


async def main():
    scanner = BleakScanner(
        simple_callback
    )
    global DEVICE_COUNT
    for i in range(0, 5):
        print("(re)starting scanner")
        async with scanner:
            await asyncio.sleep(5.0)
        print(f"Devices in scan: {DEVICE_COUNT}")
        DEVICE_COUNT = 0


asyncio.run(main())
