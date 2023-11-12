import tkinter as tk
from tkinter import filedialog
import sys


def _open_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, content)


# ファイルをダブルクリックして開く
def open_file_from_file():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        _open_file(file_path)


# ファイルを選択して開く
def open_file_from_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a file", filetypes=[("Lab note", "*.ln")])
    if file_path:
        _open_file(file_path)


# GUIのセットアップ
root = tk.Tk()
root.title("Lab Note")

# テキスト表示エリア
text = tk.Text(root, wrap="word", width=40, height=10)
text.pack(padx=10, pady=10)

open_file_from_file()

# ファイルを開くボタン
open_button = tk.Button(root, text="Open File", command=open_file_from_dialog)
open_button.pack(pady=10)

# ウィンドウを表示
root.mainloop()
