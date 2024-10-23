import simplepyble

if __name__ == "__main__":
    adapter = simplepyble.Adapter.get_adapters()[0]

    print(f"Selected adapter: {adapter.identifier()} [{adapter.address()}]")

    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))

    # Scan for 5 seconds
    adapter.scan_for(5000)

    peripherals = adapter.scan_get_results()
    print("The following peripherals were found:")
    for peripheral in peripherals:
        connectable_str = "Connectable" if peripheral.is_connectable() else "Non-Connectable"
        print(f"{peripheral.identifier()} [{peripheral.address()}] - {connectable_str}")
        print(f'    Address Type: {peripheral.address_type()}')
        print(f'    Tx Power: {peripheral.tx_power()} dBm')

        manufacturer_data = peripheral.manufacturer_data()
        for manufacturer_id, value in manufacturer_data.items():
            print(f"    Manufacturer ID: {manufacturer_id}")
            print(f"    Manufacturer data: {value.hex()}")

        services = peripheral.services()
        for service in services:
            print(f"    Service UUID: {service.uuid()}")
            print(f"    Service data: {service.data().hex()}")

    print(f"A total of {len(peripherals)} were found.")