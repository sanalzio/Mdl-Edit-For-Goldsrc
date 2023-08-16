#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import mdledit_support
import utils.compile
import utils.decompile
import utils.smdcut
import utils.smdreverse
import utils.smdcompress

class outclas:
    def wo(output_widget, message):
        output_widget.insert(tk.END, str(message) + '\n')
        output_widget.see(tk.END)

class Toplevel1:
    def __init__(self, top=None):
        top.geometry("600x450+340+90")
        top.minsize(120, 1)
        top.maxsize(1284, 701)
        top.resizable(1, 1)
        top.title("MdlTools")
        top.configure(background="#d9d9d9")

        self.top = top

        self.menubar = tk.Menu(top, font="TkMenuFont")
        top.configure(menu=self.menubar)

        self.create_menu("Compile", utils.compile)
        self.create_decompile_menu("Decompile")
        self.create_cut_menu("SmdCut")
        self.create_compress_menu("SmdCompress")
        self.create_menu("SmdReverse", utils.smdreverse)

    def create_menu(self, menu_name, action_func):
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=menu_name, menu=menu)

        file_path_var = tk.StringVar()
        file_path_label = tk.Label(menu, text="File Path:")
        file_path_label.pack(side=tk.LEFT, padx=10)
        file_path_entry = tk.Entry(menu, textvariable=file_path_var)
        file_path_entry.pack(side=tk.LEFT, padx=10)

        file_select_button = tk.Button(menu, text="...", command=lambda: self.select_file(file_path_var))
        file_select_button.pack(side=tk.LEFT, padx=10)

        if menu_name == "Decompile":
            clear_qc = tk.BooleanVar()
            clear_qc_checkbox = tk.Checkbutton(menu, text="Clear .qc", variable=clear_qc)
            clear_qc_checkbox.pack(side=tk.LEFT, padx=10)

        output_text = tk.Text(self.top, height=10, width=50)
        output_text.pack(side=tk.LEFT, padx=10, pady=10)

        execute_button = tk.Button(menu, text=menu_name, command=lambda: self.execute_action(action_func, file_path_var, output_text, clear_qc if menu_name == "Decompile" else None))
        execute_button.pack(side=tk.LEFT, padx=10)

    # ... (other methods are unchanged)

    def execute_action(self, action_func, file_path_var, output_text, clear_qc=None):
        file_path = file_path_var.get()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Executing...\n")
        if action_func == utils.compile:
            action_func(output_text, outclas, repr(file_path))
        elif action_func == utils.smdcut:
            max_triangles = self.max_triangles.get()
            action_func(output_text, repr(file_path), max_triangles, outclas)
        elif action_func == utils.smdcompress:
            divide_value = self.divide_value.get()
            action_func(output_text, repr(file_path), divide_value, outclas)
        elif action_func == utils.smdreverse:
            action_func(output_text, repr(file_path), outclas)

    # ... (other methods are unchanged)

if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()
