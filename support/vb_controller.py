import virtualbox


class VBController:
    def __init__(self):
        self.vbox = virtualbox.VirtualBox()
        self.session = virtualbox.Session()
        self.machine = None
        self.current_operation_name = None

    def _change_current_operation_name(self, name):
        self.current_operation_name = name

    def print_all_vms(self):
        print([m.name for m in self.vbox.machines])

    def select_machine(self, name):
        self._change_current_operation_name(f"{self.select_machine.__name__}")
        self.machine = self.vbox.find_machine(name)

    def check_states(self):
        current_machine_state = self.machine.state
        current_session_state = self.session.state
        print("----------------------------------------------------")
        print(f"After execution of: {self.current_operation_name}")
        print(f"Machine state: {current_machine_state}, Session state: {current_session_state}")
        print("----------------------------------------------------")
        print()

    def start_machine_in_window(self):
        self._change_current_operation_name(f"{self.start_machine_in_window.__name__}")
        progress = self.machine.launch_vm_process(self.session, "gui", [])

    def send_command(self, command):
        self._change_current_operation_name(f"{self.send_command.__name__}")
        self.session.console.keyboard.put_keys(command + "\n")

    def unlock_session(self):
        self._change_current_operation_name(f"{self.unlock_session.__name__}")
        self.session.unlock_machine()

    def lock_session(self):
        self._change_current_operation_name(f"{self.lock_session.__name__}")
        self.machine.lock_machine(self.session, virtualbox.library.LockType.shared)

    def power_down(self):
        self._change_current_operation_name(f"{self.power_down.__name__}")
        self.session.console.power_down()
