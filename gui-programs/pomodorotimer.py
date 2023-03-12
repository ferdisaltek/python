import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.minutes = 25
        self.seconds = 0
        self.count = 0
        self.paused = False

        self.time_display = tk.Label(self.master, text=f"{self.minutes:02}:{self.seconds:02}", font=("Arial", 60))
        self.time_display.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start", font=("Arial", 16), command=self.start_timer)
        self.start_button.pack(pady=5)

        self.pause_button = tk.Button(self.master, text="Pause", font=("Arial", 16), state="disabled", command=self.pause_timer)
        self.pause_button.pack(pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", font=("Arial", 16), state="disabled", command=self.reset_timer)
        self.reset_button.pack(pady=5)

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.reset_button.config(state="normal")

        self.count += 1
        if self.count % 2 == 1:
            self.minutes = 25
            self.seconds = 0
        else:
            self.minutes = 5
            self.seconds = 0

        self.update_display()

        while self.minutes >= 0 and not self.paused:
            self.master.update()
            time.sleep(1)
            if self.seconds == 0:
                self.seconds = 59
                self.minutes -= 1
            else:
                self.seconds -= 1
            self.update_display()

    def pause_timer(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.start_timer()

    def reset_timer(self):
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        self.reset_button.config(state="disabled")

        self.minutes = 25
        self.seconds = 0
        self.count = 0
        self.paused = False

        self.update_display()

    def update_display(self):
        self.time_display.config(text=f"{self.minutes:02}:{self.seconds:02}")

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
