from ttkthemes import ThemedTk
from tkinter import ttk

# Membuat root window dengan tema modern
root = ThemedTk(theme="arc")
root.title("Modern Tkinter GUI")

# Mengatur ukuran jendela
root.geometry("400x300")

# Menambahkan style kustom jika diperlukan
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 14), background='#ffffff', foreground='#333333')

# Menambahkan frame dengan style modern
frame = ttk.Frame(root, padding=(20, 20, 20, 20))
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Menambahkan label dan tombol ke dalam frame
label = ttk.Label(frame, text="Hello, this is a modern GUI!")
label.pack(pady=10)

button = ttk.Button(frame, text="Click Me")
button.pack(pady=10)

def change_theme(new_theme):
    root.set_theme(new_theme)

# Menambahkan tombol untuk mengganti tema
theme_button = ttk.Button(frame, text="Change to Radiance", command=lambda: change_theme("radiance"))
theme_button.pack(pady=10)
theme_button = ttk.Button(frame, text="Change to Radiance", command=lambda: change_theme("equilux"))
theme_button.pack(pady=10)
theme_button = ttk.Button(frame, text="Change to Radiance", command=lambda: change_theme("yaru"))
theme_button.pack(pady=10)


# Menjalankan aplikasi
root.mainloop()
