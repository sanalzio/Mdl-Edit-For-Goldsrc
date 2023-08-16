def wo(output_widget, message):
    output_widget.insert(tk.END, str(message) + '\n')
    output_widget.see(tk.END)
