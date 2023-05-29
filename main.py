import virtualbox
import time


class VirtualMachine:
    def __init__(self):
        self.vbox = virtualbox.VirtualBox()
        self.session = virtualbox.Session()
        self.machine = None

    def list_of_machines(self):
        return [m.name for m in self.vbox.machines]

    def find_machine(self, name):
        self.machine = self.vbox.find_machine(name)
        return self.machine

    def start_machine(self):
        # try:
        #     # Check if the machine is already running
        #     if self.machine.state != virtualbox.library.MachineState.running:
        #         progress = self.machine.launch_vm_process(self.session, "gui", [])
        #         progress.wait_for_completion()
        #
        # finally:
        #     # Close the session before exiting the program
        #     if self.session.state == virtualbox.library.SessionState.locked:
        #         try:
        #             self.session.unlock_machine()
        #             while self.session.state != virtualbox.library.SessionState.unlocked:
        #                 time.sleep(1)
        #         except virtualbox.library.VBoxErrorObjectNotFound:
        #             pass

        if self.machine.state != virtualbox.library.MachineState.running:
            progress = self.machine.launch_vm_process(self.session, "gui", [])
            progress.wait_for_completion()


    def stop_machine(self):
        try:
            # Check if the machine is already running
            if self.machine.state == virtualbox.library.MachineState.running:
                progress = self.machine.launch_vm_process(self.session, "gui", [])
                progress.wait_for_completion()

        finally:
            # Close the session before exiting the program
            if self.session.state == virtualbox.library.SessionState.locked:
                try:
                    self.session.unlock_machine()
                    while self.session.state != virtualbox.library.SessionState.unlocked:
                        time.sleep(1)
                except virtualbox.library.VBoxErrorObjectNotFound:
                    pass

    def power_down_machine(self):
        self.session.console.power_down()

    def close_session(self):
        if self.session.state == virtualbox.library.SessionState.locked:
            try:
                self.session.unlock_machine()
                while self.session.state != virtualbox.library.SessionState.unlocked:
                    time.sleep(1)
            except virtualbox.library.VBoxErrorObjectNotFound:
                pass

    def send_command(self):
        self.session.console.keyboard.put_keys("daniel\n")


vm_instance = VirtualMachine()
print(vm_instance.list_of_machines())
print()

print(f"Before find_machine: {vm_instance.session.state}") # at this point session.state shows Unlocked
print()

machine = vm_instance.find_machine("openSUSE")     # return machine object, if found.
time.sleep(5)
vm_instance.start_machine()
print(f"After find_machine and start_machine: {vm_instance.session.state}") # at this point session.state shows Locked
print()


time.sleep(60)

vm_instance.send_command()


# vm_instance.stop_machine()
# print(f"After stop_machine: {vm_instance.session.state}")  # at this point session.state shows Locked
# print()
#
#
# time.sleep(20)
#
#
# vm_instance.power_down_machine()
# print(f"After power_down_machine: {vm_instance.session.state}")  # at this point session.state shows Locked
# print()
#
#
# time.sleep(20)
#
#
# vm_instance.close_session()
# time.sleep(20)
# print(f"After close_session: {vm_instance.session.state}")                # at this point session.state shows Unlocked
