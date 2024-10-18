# Study Room Density Tracker

The goal of this project is a dashboard accessible over the web that displays how busy different study areas around campus are.

## Components

### Sensor Units

Each sensor unit needs to be bluetooth and Wi-Fi enabled. It will use the bluetooth functionality to poll all nearby devices. This is the data that will be used to approximate density. The component requires Wi-Fi to then post its results to the server.

### Estimator (could be separate or inside the sensor units)

The estimator is what will take the data from the polling and produce an estimated density. This will need to be tuned with real world testing in order to ensure it is accurate. This could be implemented on the sensor devices, or alternatively it can be deployed elsewhere and read in the events.

### Web Server

The Web Server takes the final data and makes it accessible to students. It should be available on the public internet or the UTS student intranet.