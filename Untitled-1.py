import tkinter as tk
from tkinter import simpledialog, messagebox
import winsound

def main():
    root = tk.Tk()
    root.withdraw()
    
    while True:
        path = simpledialog.askstring("made by mrflamflam", "Do you wish to run this?:")
        if path is None:
            break
        
        try:
            winsound.PlaySound(path, winsound.SND_FILENAME)
            messagebox.showinfo("Info", f"Running... {path}...")
        except Exception as e:
            messagebox.showerror("Error", f"PlaySound failed: {e}")
        
        response = simpledialog.askstring("Continue", "Type 'exit' or close the window to stop")
        if response == "exit":
            break
    
    root.destroy()

if __name__ == "__main__":
    main()
    import tkinter as tk
import time

def flash_colors():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white']
    
    for color in colors:
        root.config(bg=color)
        root.update()
        time.sleep(0.5)
    
    # Loop continuously
    root.after(100, flash_colors)

root = tk.Tk()
root.title("Color Flasher")
root.geometry("400x400")

label = tk.Label(root, text="Computer Hacked!", font=("Arial", 24), fg="Red")
label.pack(expand=True)

# Start the flashing
root.after(100, flash_colors)

root.mainloop()
import tkinter as tk
import time

def flash_colors():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white']
    
    for color in colors:
        root.config(bg=color)
        root.update()
        time.sleep(0.5)
    
    # Loop continuously
    root.after(100, flash_colors)

root = tk.Tk()
root.title("Color Flasher")
root.attributes('-fullscreen', True)

label = tk.Label(root, text="Computer Hacked!", font=("Arial", 24), fg="Red")
label.pack(expand=True)

# Press ESC to exit full screen
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Start the flashing
root.after(100, flash_colors)

root.mainloop()
loopstart=True

