#take cli arguments: port, ip, message buffer byte size (default 1024)
#referenced from: https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python#4033743

import udp_server
import sys

udp_args = sys.argv

#template command: python3 run_udp_server.py host port byte_buffer

#example command:
# python3 /home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/UDP/run_udp_server.py localhost 1234 1024

#list indices offset by 1 since filename is argument 0
udp_server_lib.udp_server(host=str(udp_args[1]),
                                    port=int(udp_args[2]),
                                    byte_buffer=int(udp_args[3]),
                                    )
