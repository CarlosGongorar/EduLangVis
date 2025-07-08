import tkinter as tk
from tkinter import ttk
import time
import threading

class SortVisualizer:
    def __init__(self, states, array, algorithm):
        self.states = states
        self.array = array
        self.algorithm = algorithm
        self.delay = 300  # Default speed
        self.playing = False

        # Principal Window
        self.window = tk.Tk()
        self.window.title("EduLangVis")
        self.window.configure(bg="#f2f2f2")

        # Frame
        self.frame = tk.Frame(self.window, bg="#f2f2f2", padx=10, pady=10)
        self.frame.pack()

        # Header
        self.title_label = tk.Label(self.frame, text="EduLangVis", fg="blue", bg="#f2f2f2", font=("Arial", 14, "underline"), cursor="hand2")
        self.title_label.grid(row=0, column=0, sticky="w")

        # Array and algorithm
        info_text = f"Array: {self.array}   Algorithm: {self.algorithm.replace("_", " ").capitalize()}"
        self.info_label = tk.Label(self.frame, text=info_text, bg="#f2f2f2", font=("Arial", 12))
        self.info_label.grid(row=1, column=0, sticky="w", pady=(5, 10))

        # Speed slider
        self.speed_label = tk.Label(self.frame, text="Speed:", bg="#f2f2f2", font=("Arial", 10))
        self.speed_label.grid(row=0, column=1, sticky="e", padx=(20, 5))
        self.speed_slider = tk.Scale(self.frame, from_=50, to=1000, orient=tk.HORIZONTAL, command=self.update_speed, showvalue=0, length=150)
        self.speed_slider.set(self.delay)
        self.speed_slider.grid(row=0, column=2, sticky="w")

        # Play button
        self.play_button = tk.Button(self.frame, text="Play", font=("Arial", 12), width=10, bg="#dddddd", command=self.start_animation)
        self.play_button.grid(row=1, column=2, padx=10)

        # Canva
        self.canvas_width = 700
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(padx=10, pady=10)

    """Fuction to update speed"""
    def update_speed(self, val):
        self.delay = int(val)

    def draw_state(self, state):
        self.canvas.delete("all")
        if not state:
            return
        bar_width = self.canvas_width / len(state)
        max_val = max(state)
        for i, val in enumerate(state):
            x0 = i * bar_width + 2
            y0 = self.canvas_height - (val / max_val * self.canvas_height)
            x1 = (i + 1) * bar_width - 2
            y1 = self.canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#a040ff", outline="#8000a0")

    """Animation"""
    def animate(self):
        for state in self.states:
            if not self.playing:
                break
            self.draw_state(state)
            time.sleep(self.delay / 1000)

    """Start Animation"""
    def start_animation(self):
        if self.playing:
            return  # If is running
        self.playing = True
        threading.Thread(target=self.animate, daemon=True).start()

    def run(self):
        self.window.mainloop()