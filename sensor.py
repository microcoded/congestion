from asyncio import run as async_run
from asyncio import sleep as async_sleep
from requests import post
from requests.exceptions import ConnectTimeout
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData


SCANNER_REFRESH_TIME = 5.0
SERVER_URL = "http://172.19.119.30:1234/receive"
AREA_NAME = "CB11.04.400"
DEVICES = {}


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
    scanner = BleakScanner(
        scanner_callback
    )
    global DEVICES
    while True:
        print("(re)starting scanner")
        async with scanner:
            await async_sleep(SCANNER_REFRESH_TIME)
        print(f"Device count: {len(DEVICES)}")
        data = {'name': AREA_NAME, 'device_count': len(DEVICES)}
        try:
            post(SERVER_URL, json=data)
        except ConnectTimeout as error:
            print(f"Update failed for {data['name']}: {error}")
        DEVICES = {}


# Run the main function
async_run(main())
