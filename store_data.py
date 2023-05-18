import os
import time

from measure import experiment_options

DATESTAMP_FORMAT = "%d-%m-%Y"
TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M:%S"
FILEPATH = "/home/foss/data/"
FLUSHING_THRESHOLD = 10

def create_filename():
	""" Creating a unique name for the new measurement file in the pattern of <file_path><date>(<seq_nr>).csv. """
	name = FILEPATH + time.strftime(DATESTAMP_FORMAT)
	nr = 1
	while os.path.isfile(name + ".csv"): # file with this name already exists
		name = "{0}({1})".format(name.split('(')[0], nr)
		nr = nr + 1
	return (name + ".csv")

def write_to_csv(connection, experiment_type):
	"""
	Writing the measurements line by line into a csv.
	Flushing this output after a certain amount of lines (flushing_threshold),
	so the user can follow the real time data on his device.
	This also has the advantage, that a maximum of flushing_threshold-1 lines
	of measurement are lost in the event of a sudden power outage.
	Each line has the format: <timestamp>, <measured_value>, <unit>, <item_name>.
	"""
	with open(create_filename(), "a") as f:
		line_counter = 0
		while True:
			data = connection.recv()
			if data is None: # no more measurements incoming
				break
			f.write("{0},{1},{2},{3}\n".format(
				time.strftime(TIMESTAMP_FORMAT),
				str(data),
				experiment_options[experiment_type][1],
				experiment_type
				))
			line_counter = line_counter + 1
			if line_counter >= FLUSHING_THRESHOLD:
				f.flush()
				line_counter = 0
