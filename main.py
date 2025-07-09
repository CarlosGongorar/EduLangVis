import tkinter as tk
from compiler import Compiler
from sintactic import ParserError

class EduLangVisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EduLangVis Console")

        # Text input
        self.input_text = tk.Text(root, height=15, width=80, font=("Courier", 10))
        self.input_text.pack(padx=10, pady=10)

        # Compile button
        self.compile_btn = tk.Button(root, text="Compilate and Visualize", command=self.compile_code, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.compile_btn.pack(pady=5)

        # Output (console-like)
        self.output_console = tk.Text(root, height=12, width=80, font=("Courier", 10), bg="black", fg="lime", state="disabled")
        self.output_console.pack(padx=10, pady=(5, 10))

    def write_to_console(self, message):
        self.output_console.configure(state="normal")
        self.output_console.insert(tk.END, message + "\n")
        self.output_console.see(tk.END)
        self.output_console.configure(state="disabled")

    def clear_console(self):
        self.output_console.configure(state="normal")
        self.output_console.delete(1.0, tk.END)
        self.output_console.configure(state="disabled")

    def compile_code(self):
        code = self.input_text.get("1.0", tk.END)
        #self.clear_console()
        compiler = Compiler()
        success = compiler.compile(code)
        self.write_to_console(compiler.message_log)
        if success:
            compiler.execute_visualization()

if __name__ == "__main__":
    root = tk.Tk()
    app = EduLangVisGUI(root)
    root.mainloop()