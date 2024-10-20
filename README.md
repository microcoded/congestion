# Study Area Congestion Tracker

This project aims to provide a dashboard through a web interface that displays congestion levels of student study areas around a university campus.

## Components

### Sensor Nodes
Each node needs to have Bluetooth and Wi-Fi capability, specifically a Wi-Fi interface that supports [monitor mode](https://en.wikipedia.org/wiki/Monitor_mode).

Bluetooth module is used to poll for unique devices within the range of the node, and Wi-Fi is used to also monitor for unique devices. This data is then sent to a processing server through an internet connection.

The topology of this program is centralised; there is one server that each node connects to, and the nodes do not connect to each other.

### Server
#### Processing Server
This component collates the data from each sensor node to produce an estimated density measure in a human–readable qualitative format.

#### Web Server
The Web Server is implemented on the same server where the processing occurs. It provides a web interface to this project that is a dashboard of density estimates for each area nodes are deployed.