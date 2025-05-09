from suggestions import suggest_correction
import tkinter.messagebox as messagebox
import tkinter as tk
from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from ast_visualizer import ASTVisualizer

class MiniCompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Compiler with AST Visualizer")

        self.entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.focus_set() 
        self.entry.bind("<Return>", lambda event: self.compile())


        self.button = tk.Button(root, text="Compile", command=self.compile)
        self.button.pack(pady=5)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack()

        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
        self.result_label.pack()
        

    def clear_canvas(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

    def compile(self):
        expression = self.entry.get()

        # Tokenization
        try:
            tokens = tokenize(expression)
        except SyntaxError as e:
            self.result_label.config(text=f"Syntax Error: {e}", fg="red")
            self.clear_canvas()
            suggestions = suggest_correction(expression)
            if suggestions:
                messagebox.showinfo("AI Helper Suggestions", "\n".join(suggestions))
            return

        # Parsing
        try:
            parser = Parser(tokens)
            ast = parser.parse()
        except SyntaxError as e:
            self.result_label.config(text=f"Syntax Error: {e}", fg="red")
            self.clear_canvas()
            suggestions = suggest_correction(expression)
            if suggestions:
                messagebox.showinfo("AI Helper Suggestions", "\n".join(suggestions))
            return

        # Evaluation
        try:
            result = evaluate(ast)
            self.result_label.config(text=f"Result: {result}", fg="green")
        except Exception as e:
            self.result_label.config(text=f"Evaluation Error: {e}", fg="red")
            self.clear_canvas()
            return

        # Visualize AST
        self.clear_canvas()
        ASTVisualizer(self.canvas_frame, ast)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniCompilerApp(root)
    root.mainloop()
