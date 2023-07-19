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
        if experiment_type in experiment_options.keys() or experiment_type == "all":
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
    
    TODOs for the use case of connecting multiple parallel sensors:
    - Modify the pin connections of light, o2 and temperature sensor: change the
    input channels physically and as variables in the code, set and use additional voltage outputs.
    - When dealing wit connection issues with the PSLab: break all measurements and
    reconnect in a unified manner.
    """
    conn1, conn2 = multiprocessing.Pipe(duplex=False)
    
    if experiment_type == "all":
        measuring = [multiprocessing.Process(target=get_data_pslab,
            args=(conn2, list(experiment_options)[i])) for i in range(4)] 
    else:
        measuring = [multiprocessing.Process(target=get_data_pslab,
            args=(conn2, experiment_type))]
    for m in measuring:
        m.start()
    
    sharing = multiprocessing.Process(target=export,
        args=(conn1,))
    sharing.start()
    
    for m in measuring:
        m.join()
    sharing.join()
    conn1.close()
    conn2.close()

if __name__ == "__main__":
    experiment_type = check_args()
    if experiment_type is not None:
        run_pipes(experiment_type)