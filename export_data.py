import os
import time
import argparse
from getmac import get_mac_address as gma
from pythonosc import udp_client

MAC_ADDRESS = gma()

OSC_RECEIVER_IP = "192.168.173.152"
OSC_RECEIVER_PORT = 5005

DATESTAMP_FORMAT = "%d-%m-%Y"
TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M:%S"
FILEPATH = "/home/foss/data/"
FLUSHING_THRESHOLD = 10

def create_csv_filename():
	"""
	Creating a unique name for the new measurement file
	in the pattern of <file_path><date>(<seq_nr>).csv.
	"""
	name = FILEPATH + time.strftime(DATESTAMP_FORMAT)
	nr = 1
	while os.path.isfile(name + ".csv"): # file with this name already exists
		name = "{0}({1})".format(name.split('(')[0], nr)
		nr = nr + 1
	return (name + ".csv")

def write_to_csv(file, data, line_counter):
	"""
	Appending the current measurement as a new line into the CSV file.
	Flushing the output after a certain amount of lines (flushing_threshold),
	so the user can follow the real time data on his device.
	This also has the advantage, that a maximum of |flushing_threshold-1| lines
	of measurement are lost, in the event of a sudden power outage.
	Each line has the format: <timestamp>, <measured_value>, <unit>, <item_name>, <mac_address>.
	"""
	file.write("{0},{1}\n".format(
    	time.strftime(TIMESTAMP_FORMAT),",".join(str(d) for d in data)))
	line_counter = line_counter + 1
	if line_counter >= FLUSHING_THRESHOLD: # flushing (aka updating) the csv now
		file.flush()
		line_counter = 0
	return line_counter
  
def init_osc_connection():
    """
    Initiating the OSC client and enabling it send data to the osc server at
    the specified ip address and port.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=OSC_RECEIVER_IP,
            help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=OSC_RECEIVER_PORT,
            help="The port the OSC server is listening on")
    options, unknown = parser.parse_known_args()
    return udp_client.SimpleUDPClient(options.ip, options.port)

    
def share_via_osc(osc_client, data):
    """
    Sending the current measurement via the OSC protocol to the specified receiver.
    Each OSC message has the format: /<item_name> <measured_value>, <unit>, <timestamp>, <mac_address>.
    """
    osc_client.send_message("/{0}".format(data[2]),
            "{0} {1} {2} {3}".format(str(data[0]), data[1], data[3], time.strftime(TIMESTAMP_FORMAT)))

def export(connection):
	"""
	Initiating a file and osc connecting, then updating those two storage/ sharing
	methods for every incoming measurement in real time.
	"""
	osc_client = init_osc_connection()
	with open(create_csv_filename(), "a") as file:
		line_counter = 0
		while True:
			data = connection.recv()
			data.append(MAC_ADDRESS)
			if data is None: # no more measurements incoming
				break
			line_counter = write_to_csv(file, data, line_counter)
			share_via_osc(osc_client, data)