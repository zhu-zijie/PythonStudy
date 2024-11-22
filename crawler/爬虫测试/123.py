import tkinter as tk
from tkinter import simpledialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.root.geometry("400x300")
        self.center_window()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_main_menu()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="请输入歌手的姓名：").pack(pady=10)
        self.singer_entry = tk.Entry(self.main_frame)
        self.singer_entry.pack(pady=10)
        tk.Button(self.main_frame, text="确定", command=self.get_music_list).pack(pady=10)

    def get_music_list(self):
        singer_name = self.singer_entry.get()
        self.song_list = self.fetch_music_list(singer_name)
        self.create_choice_menu()

    def create_choice_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="请输入歌曲id（0.结束任务！）：").pack(pady=10)
        self.song_id_entry = tk.Entry(self.main_frame)
        self.song_id_entry.pack(pady=10)
        tk.Button(self.main_frame, text="确定", command=self.handle_song_choice).pack(pady=10)

    def handle_song_choice(self):
        song_id = int(self.song_id_entry.get())
        if song_id == 0:
            self.show_message("感谢您的使用！")
            self.root.quit()
        else:
            for song in self.song_list:
                if song['id'] == song_id:
                    self.create_action_menu(song)
                    return
            self.show_message("您输入的歌曲id有误！")
            self.create_choice_menu()

    def create_action_menu(self, song):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text=f"歌曲名：{song['name']}").pack(pady=10)
        options = {0: "取消任务", 1: "下载歌曲", 2: "获取热评", 3: "下载歌词"}
        self.choice_var = tk.IntVar()
        for key, value in options.items():
            tk.Radiobutton(self.main_frame, text=value, variable=self.choice_var, value=key).pack(anchor=tk.W)
        tk.Button(self.main_frame, text="确定", command=lambda: self.handle_action_choice(song)).pack(pady=10)

    def handle_action_choice(self, song):
        choice = self.choice_var.get()
        if choice == 0:
            self.create_choice_menu()
        elif choice == 1:
            self.download_music(song['id'], song['name'])
        elif choice == 2:
            self.get_comments(song['id'])
        elif choice == 3:
            self.get_lyric(song['id'], song['name'])
        else:
            self.show_message("输入有误！")
            self.create_action_menu(song)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def fetch_music_list(self, singer):
        # Mock function to simulate fetching music list
        return [{'id': 1, 'name': 'Song 1'}, {'id': 2, 'name': 'Song 2'}]

    def download_music(self, song_id, song_name):
        # Mock function to simulate downloading music
        self.show_message(f"歌曲 {song_name} 下载完成！")
        self.create_choice_menu()

    def get_comments(self, song_id):
        # Mock function to simulate getting comments
        self.show_message(f"获取歌曲 {song_id} 的热评！")
        self.create_choice_menu()

    def get_lyric(self, song_id, song_name):
        # Mock function to simulate getting lyrics
        self.show_message(f"歌词 {song_name} 下载完成！")
        self.create_choice_menu()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()