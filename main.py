import time

from support.the_gui import MyGui
from support.vb_controller import VBController


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def linux_test_sequence():
        machine_name = 'openSUSE'
        vbc = VBController()

        vbc.select_machine(machine_name)
        time.sleep(1)
        vbc.check_states()                  # PoweredOff / Unlocked

        vbc.start_machine_in_window()       # starts the window
        time.sleep(60)
        vbc.check_states()                  # Paused    / Locked

        vbc.send_command("daniel")
        time.sleep(3)
        vbc.send_command("Maimun06")
        time.sleep(3)
        vbc.send_command("ls")
        time.sleep(3)
        vbc.check_states()                  # Paused    / Locked

        vbc.unlock_session()
        time.sleep(10)
        vbc.check_states()                  # Paused    / Unlocked

        vbc.lock_session()
        time.sleep(5)
        vbc.check_states()                  # Paused    / Locked

        vbc.power_down()                    # close window
        time.sleep(5)
        vbc.check_states()                  # PoweredOff / Locked

    def win_test_sequence(self):
        machine_name = 'WinDev2305Eval'
        vbc = VBController()

        vbc.select_machine(machine_name)
        time.sleep(1)
        vbc.check_states()                  # PoweredOff / Unlocked

        vbc.start_machine_in_window()       # starts the window
        time.sleep(180)
        vbc.check_states()                  # Paused    / Locked

        vbc.send_command("ipconfig")
        time.sleep(30)

        vbc.send_command("shutdown /s /t 0")
        time.sleep(60)
        #
        # vbc.check_states()                  # Paused    / Locked
        # vbc.power_down()                    # close window
        # time.sleep(5)
        # vbc.check_states()                  # PoweredOff / Locked


# with gui
# if __name__ == '__main__':
#     mc = MainController()
#
#     professional_window = MyGui(mc)
#     professional_window.start()


# no gui
if __name__ == '__main__':
    mc = MainController()
    mc.win_test_sequence()
