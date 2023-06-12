# Connecting a User Device (PC or Phone) to the File Server 

After the PSLab sensor box is connected to electricity, the WiFi Hotspot is automatically initialized. Once the users PC/ Phone is now connected to this WiFi Hotspot, a data transfer network connection can be initialized to access the file server.

## General Disclaimers

1. You probably need to wait a minute or two after starting the PSLab sensor box, until the WiFi Hotspot is successfully initialized.
2. It is essential to **stay connected** to the WiFi Hotspot in order to access the data, even though your device might complain about "no internet access". This connection may need to be ensured by re-connecting manually.
3. The file server is supposed to be accessed **anonymously**, as a **"guest user"**, without username or password.
4. The connection name can be chosen arbitrarily. Just make sure, that different names are assigned to the different PSLabs, in order for them not to be mixed up.

## On Windows
1. Open the file explorer.
2. Right click on "This PC" and select "Add Network Address".
3. Choose to add a user defined network address and enter "\\\\10.42.0.1\data" as this address.
4. Assign a name to this new connection.
5. Finish the wizard. The PSLab is now available as a network device under "This PC" > "Network Addresses".

## On Mac

1. Hit Command+K and look for "Connect to Server".
2. Enter "smb://10.42.0.1/data" as the server address and click "Connect".
3. Confirm the action be entering your login details.

## On Linux

1. Open a terminal.
2. Execute "sudo apt-get install samba".
3. Open the file explorer.
4. The new device “PSLab” should automatically appear in the network section (else, refresh the page). Connect to this device.

## On iPhone

1. Open the "Files" app.
2. Select "Browse" > "Connect to Server".
3. Enter "smb://10.42.0.1/data" as the network address and click "Connect".

## On Android Phone

Depending on the type of phone, the device's preinstalled file explorer may or may not support connections to network devices. In case they are not supported, there are several external applications available in the Play Store, that support this feature. One of them is for example ["EX File Manager"](https://play.google.com/store/apps/details?id=com.ace.ex.file.manager). Here the shared data of the PSLab Sensor
Box can be accessed by entering the app, opening the menu in the top left corner,
selecting "Network" > "LAN" and clicking on "+" > "Scan".