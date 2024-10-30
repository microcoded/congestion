from asyncio import run as async_run
from asyncio import sleep as async_sleep
from requests import post
from requests.exceptions import ConnectTimeout, ConnectionError
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from random import randrange, shuffle


SCANNER_REFRESH_TIME: float = 5.0
SERVER_URL: str = "http://192.168.200.100:1234/receive"
AREA_NAME: str = "CB11.04.400"
DEVICES: dict[str, AdvertisementData] = {}

GREENS_AREAS: list = ["FEIT FLP", "Building 5A"]
ORANGE_AREAS: list = ["Reading Room", "Library Level 8"]
RED_AREAS: list = ["Library Level 6", "Library Level 7"]


def scanner_callback(device: BLEDevice, advertisement_data: AdvertisementData) -> None:
    """
    Function to process each device found in a scan.
    WARNING: This function edits the global DEVICES dict.

    Parameters:
        device: The device information of the found device.
        advertisement_data: The data advertised by the found device.

    Returns:
       None
    """
    global DEVICES
    DEVICES[device.address] = advertisement_data


async def main() -> None:
    """
    The wrapper for the sensor code.
    Runs the scanner on a set interval, flushing and sending the results after each run.

    Returns:
        None
    """
    scanner: BleakScanner = BleakScanner(
        scanner_callback
    )
    global DEVICES

    super_area_list = [AREA_NAME] + GREENS_AREAS + ORANGE_AREAS + RED_AREAS
    shuffle(super_area_list)

    library_areas = []

    for area_name in super_area_list:
        if area_name.__contains__("Library"):
            library_areas.append(area_name)
            continue
        data: dict[str, str | int] = {'name': area_name, 'device_count': 0}
        try:
            post(SERVER_URL, json=data)
        except (ConnectTimeout, ConnectionError) as error:
            print(f"Update failed for {data['name']}: {error}")

    library_areas.sort()

    for area_name in library_areas:
        data: dict[str, str | int] = {'name': area_name, 'device_count': 0}
        try:
            post(SERVER_URL, json=data)
        except (ConnectTimeout, ConnectionError) as error:
            print(f"Update failed for {data['name']}: {error}")

    while True:
        print("(re)starting scanner")
        async with scanner:
            await async_sleep(SCANNER_REFRESH_TIME)
        print(f"Device count: {len(DEVICES)}")
        data: dict[str, str | int] = {'name': AREA_NAME, 'device_count': len(DEVICES)}
        try:
            post(SERVER_URL, json=data)
        except (ConnectTimeout, ConnectionError) as error:
            print(f"Update failed for {data['name']}: {error}")

        for area_name in GREENS_AREAS:
            data: dict[str, str | int] = {'name': area_name, 'device_count': round(len(DEVICES) / 2) + randrange(0, 3)}
            try:
                post(SERVER_URL, json=data)
            except (ConnectTimeout, ConnectionError) as error:
                print(f"Update failed for {data['name']}: {error}")

        for area_name in ORANGE_AREAS:
            data: dict[str, str | int] = {'name': area_name, 'device_count': len(DEVICES) + randrange(0, 5)}
            try:
                post(SERVER_URL, json=data)
            except (ConnectTimeout, ConnectionError) as error:
                print(f"Update failed for {data['name']}: {error}")

        for area_name in RED_AREAS:
            data: dict[str, str | int] = {'name': area_name, 'device_count': len(DEVICES) * 2 + randrange(0, 10)}
            try:
                post(SERVER_URL, json=data)
            except (ConnectTimeout, ConnectionError) as error:
                print(f"Update failed for {data['name']}: {error}")

        DEVICES = {}


# Run the main function
async_run(main())
