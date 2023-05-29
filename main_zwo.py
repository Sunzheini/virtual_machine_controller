
# works in the pycharm console now make it look good


import virtualbox
import time
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
print([m.name for m in vbox.machines])
machine = vbox.find_machine('openSUSE')
print(machine.state)	# PoweredOff
print(session.state)	# Unlocked

progress = machine.launch_vm_process(session, "gui", [])	# starts the window
time.sleep(60)

print(machine.state)	# Paused
print(session.state)	# Locked

session.console.keyboard.put_keys("daniel\n")
session.console.keyboard.put_keys("Maimun06\n")
session.console.keyboard.put_keys("ls\n")
print(machine.state)	# Paused
print(session.state)	# Locked



session.unlock_machine()
print(machine.state)	# Paused
print(session.state)	# Unlocked


machine.lock_machine(session, virtualbox.library.LockType.shared)
print(machine.state)	# Paused
print(session.state)	# Locked


session.console.power_down()    # closed window