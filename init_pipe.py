import sys
import multiprocessing
import serial
import time

from measure import experiment_options, get_data_pslab
from store_data import write_to_csv
from osc_sharing import transmit_data

"""
Ensures valid starting conditions and manages the parallel workflow of measuring & writing to the csv.
Requires the type of experiment (co2, oxygen, light or temp) as an additional input parameter.
"""

osc_receiver_ip = "10.42.0.160"
osc_receiver_port = 5005

def check_args():
    """ Ensures that the script runs with a valid experiment type parameter. """
    if len(sys.argv) > 1:
        experiment_type = sys.argv[1]
        if experiment_type in experiment_options.keys():
            return experiment_type
        else:
            print("Experiment type not available.")
            return None
    else:
        print("Please provide experiment type.")
        return None

def run_pipes(experiment_type):
    """
    Spawns one process to retrieve new data, one to share this data via the OSC
    protocol and one process to store it in an CSV file.
    """
    conn1, conn2 = multiprocessing.Pipe()
    measuring = multiprocessing.Process(target=get_data_pslab,
        args=(conn2, experiment_type))
    measuring.start()
    sharing = multiprocessing.Process(target=transmit_data,
        args=(conn1, experiment_type, osc_receiver_ip, osc_receiver_port))
    sharing.start()
    storing = multiprocessing.Process(target=write_to_csv,
        args=(conn1, experiment_type))
    storing.start()

    # waiting for the processes to terminate
    measuring.join()
    sharing.join()
    storing.join()

if __name__ == "__main__":
    experiment_type = check_args()
    if experiment_type is not None:
        run_pipes(experiment_type)