import time

from support.the_gui import MyGui
from support.vb_controller import VBController


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def test_sequence():
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


if __name__ == '__main__':
    mc = MainController()

    professional_window = MyGui(mc)
    professional_window.start()
