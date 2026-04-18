import os
import sys
import numpy as np
import cv2
import random
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# ファイル選択ダイアログの表示
root = tk.Tk()
root.withdraw()

fTyp = [("","*")]

iDir = os.path.expanduser("~")

#iDir = os.path.abspath(os.path.dirname(__file__))

messagebox.showinfo('画像読込','処理画像を選択してください')

# ファイル選択ダイアログ
file = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
if not file:
    messagebox.showwarning("キャンセル", "ファイルが選択されませんでした")
    root.destroy()
    exit()

# 処理ファイル名の出力
messagebox.showinfo('画像読込',file)

# ドットの大きさを調整, スケールを入力
scale = simpledialog.askfloat(
    "入力",
    "スケールを入力してください(0~1)",
    minvalue=0,
    maxvalue=1
)
if scale is None:
    messagebox.showwarning("キャンセル", "入力がキャンセルされました")
    root.destroy()
    exit()

# 画像をグレースケールで読み込み
gray = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

# height, width = binary.shape

small = cv2.resize(gray, (0, 0), fx=scale, fy=scale)  # 縮小

# 大津の2値化
_, small_bin = cv2.threshold(small, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

small_h, small_w = small_bin.shape

# 出力画像
share1_small = np.zeros((small_h, small_w), dtype=np.uint8)
share2_small = np.zeros((small_h, small_w), dtype=np.uint8)

# ランダム0/1行列
x = np.random.randint(0, 2, size=(small_h, small_w), dtype=np.uint8)

# share1_small（0 or 255）
share1_small = x * 255

# pixelが黒かどうか
is_black = (small_bin == 0)

# share2の計算
# xとpixelの条件を組み合わせる
share2_small = np.where(
    is_black,
    (1 - x) * 255,  # 元画像が黒ならshare1_smallを反転
    x * 255         # 白なら同じ色
)

# シェアの画像を元の大きさに戻す
share1 = cv2.resize(share1_small, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_NEAREST)  # 拡大
share2 = cv2.resize(share2_small, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_NEAREST)

save_dir = os.path.dirname(file)

cv2.imwrite(os.path.join(save_dir, "share1.png"), share1)
cv2.imwrite(os.path.join(save_dir, "share2.png"), share2)

# 重ねた画像
overlay = cv2.bitwise_and(share1, share2)
cv2.imwrite(os.path.join(save_dir, "overlay.png"), overlay)

messagebox.showinfo("完了", f"保存先:\n{save_dir}")