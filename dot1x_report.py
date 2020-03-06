#!/usr/local/bin/python3
'''
This script is used to upgrade software on Cisco Catalyst 3750 and 3650 switch stacks.
'''

import os, sys, time
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
import matplotlib.pyplot as plt
from pywaffle import Waffle


# Run show commands on each switch
def run_commands(task):
    print(f'{task.host}: running show comands.')
    # run "show version" on each host
    sh_dot1x = task.run(
        task=netmiko_send_command,
        command_string="show dot1x all",
        use_textfsm=True,
    )

    print(sh_dot1x.result)




def main():
  
    # initialize The Norn
    #nr = InitNornir()
    # filter The Norn
    #nr = nr.filter(platform="cisco_ios")
    # run The Norn run commands
    #nr.run(task=run_commands)
    


    wafflez = plt.figure(
        FigureClass=Waffle,
        rows=5,
        columns=10,
        values={'switch stacks with\ndot1x enabled': 20, 'switch stacks with\ndot1x disabled': 10},
        legend={'loc': 'lower left','bbox_to_anchor': (0, -0.3),'ncol': 2},
        icons=['lock','lock-open'],
        font_size=25,
        colors=["#008000", "#F51B00"]
    )

    plt.show(wafflez)

if __name__ == "__main__":
    main()