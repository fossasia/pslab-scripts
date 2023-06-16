import argparse
from pythonosc import udp_client

from measure import experiment_options

osc_receiver_ip = "192.168.1.255"
osc_receiver_port = 5005

def transmit_data(connection, experiment_type):
    """
    This OSC client sends the current measurement data to the osc server at
    the specified ip address and port.
    First sets up the udp connection and then sends over any incoming
    measurements in real time.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=osc_receiver_ip,
            help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=osc_receiver_port,
            help="The port the OSC server is listening on")
    options, unknown = parser.parse_known_args()
    client = udp_client.SimpleUDPClient(options.ip, options.port)

    while True:
        data = connection.recv()
        if data is None: # no more measurements incoming
            break
        client.send_message("/{0}".format(experiment_type),
            "{0} {1}".format(data, experiment_options[experiment_type][1]))