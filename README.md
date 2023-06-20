# virtual_machine_controller
 
1. pip install pywin32

2. use this guide: https://pypi.org/project/virtualbox/#:~:text=Go%20to%20VirtualBox's%20downloads%20page,install%20using%20your%20system%20Python.

3. (installed sdk in the desktop folder?)

4.  made a virtual machine in Oracle VirtualBox with official microsoft windows11 image.
    made a shared folder and installed twincat 
    added the password 'pass' to the account 'User'
    using task scheduler created a task to start cmd.exe at startup
    First the resources were set to 4gb ram / 2 cpu, and later doubled to 8gb ram / 4 cpu

5. need admin rights for "progress = machine.launch_vm_process(session, "gui", [])" to work

6. make a (pycharm) project and inherited global site packages from python 3.11

7. finished script0 as per the .pptx

# (-- not done on other pc --)
8. install python v3.10.7 on virtual machine, update pip, flask
9. install vs code and python extension
9. add a delay of 1min for the cmd.exe in the scheduler
10. add a shortcut of cmd

11. set Bridged Adapter mode in virtualbox network settings
12. disabled firewall
13. enabled network discovery from advanced network settings
14. now can ping 192.168.0.115 <--> 192.168.0.1
15. create a folder server_code on the desktop and inside main.py, where you put the code from server_code.py

