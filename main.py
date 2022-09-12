from win10toast_click import ToastNotifier
import time
import os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def validate_int_input():
    valid = False
    while not(valid):
        res = input("> ")
        try:
            res = int(res)
            if (res > 0):
                valid = True
        except:
            print("Please enter a whole number of minutes.")
    return res

def show_notif(message : str):
    toaster.show_toast(
    "Pomodoro Timer", # title
    message, # message 
    icon_path=None, # 'icon_path' 
    duration=1, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    )

num_cycles = 4
num_subcycles = 4
work_time = 25
short_break_time = 5
long_break_time = 15

editing_mode = True
os.system('cls' if os.name == 'nt' else 'clear')
while (editing_mode):
    print(" ╔══════════════════════╗")
    print(" ║    Pomodoro Timer    ║")
    print(" ╚══════════════════════╝")
    print(color.UNDERLINE + "     Current Settings      " + color.END)
    print(f"  1. Num of Subcycles: {num_subcycles}")
    print(f"  2. Work Time:    {work_time} m  ")
    print(f"  3. Short Break:  {short_break_time} m  ")
    print(f"  4. Long Break:   {long_break_time} m  ")
    print(f"  5. Num of Cycles:  {num_cycles}  ")

    valid_res = False
    while not(valid_res):
        res = input("Enter corresponding number to edit, 6 to edit all sequentially, or 0 to start timer\n> ").strip()
        if (res == "1"):
            valid_res = True
            print("Enter new subcycle length.")
            num_subcycles = validate_int_input()
        elif (res == "2"):
            valid_res = True
            print("Enter new work time in minutes.")
            work_time = validate_int_input()
        elif (res == "3"):
            valid_res = True
            print("Enter new short break time in minutes.")
            short_break_time = validate_int_input()
        elif (res == "4"):
            valid_res = True
            print("Enter new long break time in minutes.")
            long_break_time = validate_int_input()
        elif (res == "5"):
            valid_res = True
            print("Enter new number of cycles.")
            num_cycles = validate_int_input()
        elif (res == "6"):
            valid_res = True
            print("Enter new subcycle length.")
            num_subcycles = validate_int_input()
            print("Enter new work time in minutes.")
            work_time = validate_int_input()
            print("Enter new short break time in minutes.")
            short_break_time = validate_int_input()
            print("Enter new long break time in minutes.")
            long_break_time = validate_int_input()
            print("Enter new number of cycles.")
            num_cycles = validate_int_input()
        elif (res == "0"):
            editing_mode = False
            valid_res = True
        else:
            print("Please enter a valid number:")
    os.system('cls' if os.name == 'nt' else 'clear')

toaster = ToastNotifier()
cycle_count = 0
subcycle_count = 0
total_subcycles = 0
time_left = work_time
mode = "true"
show_notif("It's now time to work!")
while (True):

    print("(Program is Running)")
    
    print(f"Current Cycle: {cycle_count + 1}")
    print(f"Current Subcycle: {subcycle_count + 1}")
    if (mode):
        print(f"Work Time Left: {time_left}")
    else:
        print(f"Break Time Left: {time_left}")
    print("=======================================")
    time.sleep(60)
    time_left -= 1
    if time_left <= 0:
        mode = not(mode)
        if (mode):
            subcycle_count += 1
            if (cycle_count >= num_cycles):
                break
            if ((subcycle_count) / num_subcycles == 1):
                print("Reseting cycle!")
                subcycle_count = 0
                cycle_count += 1
            print("Work Time!")
            show_notif("It's now time to work!")
            time_left = work_time
        else:
            if ((subcycle_count + 1) == num_subcycles):
                print("Long Break time!")
                show_notif("Time to take a long break!")
                time_left = long_break_time
            else:
                print("Short Break time!")
                show_notif("Time to take a short break!")
                time_left = short_break_time
print("Finished!")
quit()
    
