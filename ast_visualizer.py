import tkinter as tk
from tkinter import Canvas

class ASTVisualizer:
    def __init__(self, root, ast):
        self.canvas = Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        self.draw_ast(ast, 300, 50, 150)

    def draw_ast(self, node, x, y, offset):
        if node is None:
            return
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
        self.canvas.create_text(x, y, text=node.type, font=("Arial", 10))

        if node.left:
            self.canvas.create_line(x, y+20, x-offset, y+70)
            self.draw_ast(node.left, x-offset, y+100, offset//2)
        if node.right:
            self.canvas.create_line(x, y+20, x+offset, y+70)
            self.draw_ast(node.right, x+offset, y+100, offset//2)
