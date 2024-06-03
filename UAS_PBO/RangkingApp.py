import tkinter as tk
from tkinter import ttk

from . import MenuApp as app_menu

class RankingApp:
    def __init__(self, root, ranking_data):
        self.root = root
        self.root.title("Peringkat")
        self.ranking_data = ranking_data

        # Membuat frame utama dan menempatkannya di tengah jendela
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True)

        # Membuat frame untuk menampilkan peringkat
        self.rank_frame = tk.Frame(self.main_frame)
        self.rank_frame.pack(pady=20)

        # Membuat label judul
        self.title_label = tk.Label(self.rank_frame, text="Peringkat", font=("Futura", 16))
        self.title_label.grid(row=0, columnspan=2)

        # Membuat tabel untuk menampilkan peringkat
        self.rank_tree = ttk.Treeview(self.rank_frame, columns=("Username", "Points"), show="headings")
        self.rank_tree.heading("Username", text="Username")
        self.rank_tree.heading("Points", text="Points")
        self.rank_tree.grid(row=1, columnspan=2)

        # Menampilkan peringkat
        self.show_ranking()

        # Tombol keluar
        self.exit_button = tk.Button(self.main_frame, text="Kembali", command=self.exit_app, font=("Futura", 14))
        self.exit_button.pack(pady=10)

    def show_ranking(self):
        # Urutkan data peringkat berdasarkan poin (diurutkan dari besar ke kecil)
        sorted_ranking = sorted(self.ranking_data.items(), key=lambda x: x[1], reverse=True)

        # Menambahkan data peringkat ke dalam tabel
        for i, (user, points) in enumerate(sorted_ranking):
            self.rank_tree.insert("", "end", values=(user, points))

    def exit_app(self):
        self.root.destroy()
        app_menu.start()

# Data peringkat (contoh)
ranking_data = {
    "User1": 100,
    "User2": 90,
    "User3": 80,
    "User4": 70,
    "User5": 60
}

def start():
    # Inisialisasi Tkinter
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    app = RankingApp(root, ranking_data)

    # Menempatkan frame utama di tengah jendela
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    root.mainloop()

global root
