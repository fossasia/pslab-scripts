import sys
import multiprocessing

from measure import experiment_options, get_data_pslab
from export_data import export

"""
Ensures valid starting conditions and manages the parallel workflow of measuring & sharing the data.
Requires the type of experiment (co2, oxygen, light or temp) as an additional input parameter.
"""

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
    Spawns one process to retrieve new data and one to export this data, both
    by sharing it via OSC, and by saving it into a CSV file.
    """
    conn1, conn2 = multiprocessing.Pipe(duplex=False)
    
    measuring = multiprocessing.Process(target=get_data_pslab,
        args=(conn2, experiment_type))
    measuring.start()
    
    sharing = multiprocessing.Process(target=export,
        args=(conn1,))
    sharing.start()
    
    measuring.join()
    sharing.join()
    conn1.close()
    conn2.close()

if __name__ == "__main__":
    experiment_type = check_args()
    if experiment_type is not None:
        run_pipes(experiment_type)