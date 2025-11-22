import tkinter as tk

# This function updates the timer every second
def countdown(time_left):
    if time_left >= 0:
        timer_label.config(text=str(time_left))
        root.after(1000, countdown, time_left - 1)   # wait 1 second then run again
    else:
        timer_label.config(text="Time's up!")

# This function starts the countdown
def start():
    user_input = seconds_entry.get()

    if user_input.isdigit():          # check if the user typed a number
        countdown(int(user_input))    # start the countdown
    else:
        timer_label.config(text="Please enter a number")

# Create window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Ask the user for seconds
message_label = tk.Label(root, text="Enter seconds:", font=("Arial", 12))
message_label.pack(pady=5)

# Box where user types a number
seconds_entry = tk.Entry(root, font=("Arial", 12))
seconds_entry.pack(pady=5)

# Button starts countdown
start_button = tk.Button(root, text="Start", font=("Arial", 12), command=start)
start_button.pack(pady=10)

# Label shows the timer
timer_label = tk.Label(root, text="", font=("Arial", 20))
timer_label.pack(pady=20)

root.mainloop()
