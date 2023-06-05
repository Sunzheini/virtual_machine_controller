from time import sleep

from support.server_communicator import ServerCommunicator
from support.the_gui import MyGui
from support.vb_controller import VBController


machine_name = 'WinDev2305Eval'
machine_ip = '192.168.0.115'


# with gui
if __name__ == '__main__':
    # objects
    vbc = VBController(machine_name)
    srv = ServerCommunicator(machine_ip)

    gui_window = MyGui(vbc, srv)  # create gui and pass the vm object to the gui
    gui_window.start()      # start the gui
