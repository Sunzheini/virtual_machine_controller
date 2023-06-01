import virtualbox
import time
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
print([m.name for m in vbox.machines])
# machine = vbox.find_machine('openSUSE')
machine = vbox.find_machine('WinDev2305Eval')
print(machine.state)	# PoweredOff
print(session.state)	# Unlocked

progress = machine.launch_vm_process(session, "gui", [])    	# starts the window
print(machine.state)	# Paused
print(session.state)	# Locked

session.console.keyboard.put_keys("daniel\n")
session.console.keyboard.put_keys("Maimun06\n")

session.console.keyboard.put_keys("q\n")
session.console.keyboard.put_keys("pass\n")
session.console.keyboard.put_keys("dir\n")
session.console.keyboard.put_keys("cls\n")
print(machine.state)	# Paused
print(session.state)	# Locked

session.unlock_machine()
print(machine.state)	# Paused
print(session.state)	# Unlocked


machine.lock_machine(session, virtualbox.library.LockType.shared)
print(machine.state)	# Paused
print(session.state)	# Locked


session.console.power_down()    # closed window


gs = session.console.guest.create_session('User', 'pass')
gs.directory_exists("C:\\Windows\\System32")
gs.fs_obj_exists("C:\\Windows\\System32\\cmd.exe", False)
print(gs.user())

gs.directory_open("C:\\Windows\\System32")
gs.file_open("C:\\Windows\\System32\\cmd.exe", 2, 0, 0)

process_a = gs.process_create("C:\\Windows\\System32\\cmd.exe", ['/C', 'tasklist'], [], [], 0)


# error here
process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['/C', 'tasklist'])
print(stdout)
print(stderr)
print(process)



# ----------------------------
session.console.keyboard.put_keys("ipconfig\n")
"""
try this:
gs = session.console.guest.create_session('User', 'pass')
<virtualbox.library_ext.guest_session.IGuestSession object at 0x000001E310C0DDE0>
gs.directory_exists("C:\\Windows")
1

process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['/C','tasklist'])
print(stdout)

print(gs.directory_exists("C:\\Windows"))


virtualbox.library.IKeyboard.SCANCODES.keys()

process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe')
"""

# start twincat
session.console.keyboard.put_keys("C:\\TwinCAT\\3.1\\Target\\x64\\TcXaeShell.exe\n")
session.console.keyboard.put_keys("C:\\Program Files (x86)\\Beckhoff\\TcXaeShell\\Common7\\IDE\n")
# C:\TwinCAT\3.1\Target\StartMenuAdmin\TwinCAT.lnk

session.console.keyboard.put_keys("C:\\TwinCAT\\3.1\\Target\\StartMenuAdmin\\TwinCAT.lnk\n")
