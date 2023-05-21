# Connecting a User Device (PC or Phone) to the File Server 

After the PSLab Sensorbox is connected to electricity, the WiFi Hotspot is automatically initialized. Once the users PC/ Phone is now connected to this WiFi Hotspot, a formal network connection can be initialized to access the PSLab Sensorbox' file server.

Some general disclaimers:
1. It is essential to **stay connected** to the WiFi Hotspot, even though your device might complain about "no internet access". This might need to be ensured by re-connecting manually
2. The file server is supposed to be accessed **anonymously** as a guest user without username or passwort
3. The connection name can be chosen arbitrarily. Just take care, that you assign different names to the different PSLabs, in order not to mix them up too much later on

## On Windows
1. Open the file explorer
2. Right click on "This PC" and select "Add Network Address"
3. Choose to add a user defined network address and enter "\\\\10.42.0.1\data" as this address
4. Assign a name to this new connection 
5. Finish the wizard. The PSLab is now available as a network device under "This PC" > "Network Addresses"

## On Mac

1. Hit Command+K and look for "Connect to Server"
2. Enter "smb://10.42.0.1/data" as the server address and click "Connect"
3. Confirm the action be entering your login details

## On Linux

1. Open the file explorer
2. The new device “PSLab” should automatically appear in the network section (else, refresh the page). Connect to this device

## On iPhone

1. Open the "Files" app
2. Select "Browse" > "Connect to Server"
3. Enter "smb://10.42.0.1/data" as the network address

## On Android Phone

Depending on the type of phone, the internal file explorer may or may not support connections to network devices. In case it is not supported, there are several external apps available in the Play Store that support this feature. 