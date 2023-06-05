import virtualbox
from time import sleep


class VBController:
    def __init__(self, machine_name):
        self.machine_name = machine_name

        self.vbox = None
        self.session = None
        self._create_vbox_object_and_session()

        self.machine_object = None
        self._create_machine_object()

        self.progress = None

    def _create_vbox_object_and_session(self):
        self.vbox = virtualbox.VirtualBox()
        self.session = virtualbox.Session()
        sleep(1)

    def print_list_of_vms(self):
        print([m.name for m in self.vbox.machines])

    def _create_machine_object(self):
        try:
            self.machine_object = self.vbox.find_machine(self.machine_name)
        except virtualbox.library.VBoxErrorObjectNotFound:
            print(f"Machine {self.machine_name} not found")
        sleep(1)

    def check_states(self):
        current_machine_state = self.machine_object.state
        current_session_state = self.session.state
        print("----------------------------------------------------")
        print(f"Machine state: {current_machine_state}, Session state: {current_session_state}")
        print("----------------------------------------------------")
        print()

    def start_machine_in_window(self):
        self.progress = self.machine_object.launch_vm_process(self.session, "gui", [])

        self.progress.wait_for_completion(timeout=-1)  # -1 means wait indefinitely
        if self.progress.result_code != 0:
            raise Exception(f'Failed to start machine: {self.progress.error_info.text}')

    def send_keyboard_command(self, command):
        self.session.console.keyboard.put_keys(command + "\n")
        sleep(2)

    def send_keyboard_command_for_log_in(self):
        self.send_keyboard_command("q\n")
        sleep(2)
        self.send_keyboard_command("pass\n")
        sleep(2)

    def unlock_session(self):
        self.session.unlock_machine()

    def lock_session(self):
        self.machine_object.lock_machine(self.session, virtualbox.library.LockType.shared)

    def power_down(self):
        # self.session.console.power_down()

        # Send ACPI power button event
        self.session.console.power_button()

        while self.machine_object.state != virtualbox.library.MachineState.powered_off:
            sleep(1)

        self.unlock_session()
