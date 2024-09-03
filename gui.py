import tkinter as tk
from tkinter import ttk
import ttkthemes as tts
from tkinter import filedialog, Label, messagebox
from PIL import Image, ImageTk
from rembg import remove

def upload_file():
    global filepath
    filepath = filedialog.askopenfilename(
        title="Pilih File Gambar", 
        filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.gif"), ("All files", "*.*"))
    )
    if filepath:
        global res
        img = Image.open(filepath)
        res = img.size
        img.thumbnail((300, 400))  # Sesuaikan ukuran gambar
        img_display = ImageTk.PhotoImage(img)

        left_image_label.config(image=img_display, width=300, height=400)
        left_image_label.image = img_display
        upload_path.config(text=f"File upload: {filepath}")
        save_button.config(state=tk.NORMAL)

        global current_image_path
        current_image_path = filepath

def save_file():
    if not output_name:
        messagebox.showerror("Error", "Tidak ada file yang terbuka.")
        return
    
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")),
        initialdir="/removebg",
        initialfile=output_name
    )
    if filepath:
        output.save(filepath)

        # Tampilkan gambar di kotak kanan
        img_display = ImageTk.PhotoImage(output)
        right_image_label.config(image=img_display, width=300, height=400)
        right_image_label.image = img_display

        upload_path.config(text=f"File gambar disimpan: {filepath}")

def view_upload_file():
    if not current_image_path:
        messagebox.showerror("Error", "Tidak ada file yang terbuka.")
        return
    
    img = Image.open(current_image_path)
    img.show()
    
def view_output_file():
    if not output_path:
        messagebox.showerror("Error", "Tidak ada file yang terbuka.")
        return
    
    img = Image.open(output_path)
    img.show()

def remover_bg():
    img = Image.open(current_image_path)
    img.thumbnail((res[0],res[1]))
    
    global output
    output = remove(img)
    
    path = filepath.split("\\")
    headpath = path[0]
    for i in path[1:len(path)-1]:
        headpath += "/" + i

    filename = path[-1]

    # Store path of the output image in the variable output_path 
    global output_name, output_path
    output_path = filename.split(".")[0] + "_rbg." + filename.split(".")[1]
    output_name = filename.split(".")[0] + "_rbg." + filename.split(".")[1]
    
    img_display = ImageTk.PhotoImage(output)
    

    right_image_label.config(image=img_display, width=300, height=400)
    right_image_label.image = img_display
    return_path.config(text=f"Output: {output_name}")


# Inisialisasi GUI
root = tts.ThemedTk(theme="aqua")
root.title("Image Uploader")

root.set_theme("yaru")
root.geometry("900x600")


style = ttk.Style(root)
style.configure('TButton', font=('Poppins', 10), padding=5)
style.configure('TLabel', font=('Poppins', 14), background='#ffffff', foreground='#333333')

# Menambahkan frame dengan style modern
frame = ttk.Frame(root, padding=(10, 10, 10, 10))
frame.pack(fill="both", expand=True, padx=5, pady=5)


# Label untuk menampilkan gambar di kiri 
left_image_label = Label(frame, text="Pratinjau Kiri", width=50, height=25)
left_image_label.pack(pady=10, side=tk.LEFT)

arrowimg = Image.open("./arrow.png")
arrowimg.thumbnail((25,25))
arrow_display = ImageTk.PhotoImage(arrowimg)
arrow = ttk.Button(frame, width=1, image=arrow_display)
arrow.pack(pady=10, side=tk.LEFT, padx=50)
# left_image_label.grid(row=0, column=0, padx=10, pady=1

# Label untuk menampilkan gambar di kanan
right_image_label = Label(frame, text="Pratinjau Kanan", width=50, height=25)
right_image_label.pack(pady=10, side=tk.RIGHT)
# right_image_label.grid(row=0, column=1, padx=10, pady=10)

frame2 = ttk.Frame(root, padding=(10, 10, 10, 10))
frame2.pack(fill="both", expand=True, padx=5, pady=5)
# Label status

upload_path = Label(frame2, text="Tidak ada file yang terbuka.")
# upload_path.grid(row=2, column=0, padx=5, pady=5)
upload_path.pack(side=tk.LEFT, fill=tk.X, pady=5)

# Tombol untuk melihat gambar
view_upload_button = ttk.Button(frame2, text="Lihat Gambar", command=view_upload_file)
view_upload_button.pack(side=tk.LEFT)
# view_upload_button.grid(row=1, column=0, padx=5, pady=5)



# Tombol untuk melihat gambar
view_output_button = ttk.Button(frame2, text="Lihat Gambar", command=view_output_file)
view_output_button.pack(side=tk.RIGHT)
# view_upload_button.grid(row=1, column=0, padx=5, pady=5)

# Tombol untuk mengunggah file gambar
upload_button = ttk.Button(root, text="Unggah Gambar", command=upload_file)
upload_button.pack(side=tk.LEFT, padx=10, pady=10)


# Tombol untuk mengunggah file gambar
removebg_button = ttk.Button(root, text="Remove Background", command=remover_bg)
removebg_button.pack(side=tk.LEFT, padx=10, pady=10)

# Tombol untuk menyimpan gambar
save_button = ttk.Button(root, text="Simpan Gambar", state=tk.DISABLED, command=save_file)
save_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Label status
return_path = Label(root, text="")
# upload_path.grid(row=2, column=0, padx=5, pady=5)
return_path.pack(side=tk.RIGHT, fill=tk.X, pady=5)




# Jalankan aplikasi
current_image_path = None
root.mainloop()
