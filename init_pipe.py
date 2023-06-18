import sys
import multiprocessing

from measure import experiment_options, get_data_pslab
from store_data import write_to_csv
from osc_sharing import transmit_data

"""
Ensures valid starting conditions and manages the parallel workflow of measuring & writing to the csv.
Requires the type of experiment (co2, oxygen, light or temp) as an additional input parameter.
"""

export_method = transmit_data

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
    Spawns one process to retrieve new data and one to export this data either
    by sharing it via OSC or by saving it into a CSV file.
    """
    conn1, conn2 = multiprocessing.Pipe()
    measuring = multiprocessing.Process(target=get_data_pslab,
        args=(conn2, experiment_type))
    measuring.start()
    exporting = multiprocessing.Process(target=export_method,
        args=(conn1, experiment_type))
    exporting.start()

    # waiting for the processes to terminate
    measuring.join()
    exporting.join()

if __name__ == "__main__":
    experiment_type = check_args()
    if experiment_type is not None:
        run_pipes(experiment_type)