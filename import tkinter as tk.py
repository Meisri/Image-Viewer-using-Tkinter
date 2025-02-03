import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((500, 500), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

# Create main window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x600")

# Button to open image
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)

# Label to display image
label = tk.Label(root)
label.pack()

# Run the application
root.mainloop()
