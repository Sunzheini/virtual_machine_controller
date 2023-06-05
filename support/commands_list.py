# main
import virtualbox   # import the package
vbox = virtualbox.VirtualBox()  # create an instance of the VirtualBox object
session = virtualbox.Session()  # create an instance of the Session object
print([m.name for m in vbox.machines])  # list all the VMs
machine = vbox.find_machine('WinDev2305Eval')   # find the VM
progress = machine.launch_vm_process(session, "gui", [])  # launch the VM in a new window
session.console.keyboard.put_keys("q\n")    # send the letter q to the VM, I use it to go to the enter pass form
session.console.keyboard.put_keys("pass\n")    # send the password to the VM
session.console.power_button()    # send the ACPI power button event (use this not the hard shutdown)

# support
print(machine.state)    # print the current state of the VM
print(session.state)    # print the current state of the session
session.unlock_machine()    # unlock the session
machine.lock_machine(session, virtualbox.library.LockType.shared)   # lock the session
session.console.power_down()    # hard power down the VM (not good for the VM)
