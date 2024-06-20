import tkinter as tk


import requests
import base64

import menu, home, regist, confirm,result


def adjustScreen(cur_root):
    "アプリの画面をモニター中央に表示する関数"
    # モニターサイズ取得
    mn_width = int(cur_root.winfo_screenwidth())
    mn_height = int(cur_root.winfo_screenheight())

    # ウィンドウを中央表示するための計算
    c_width = int((mn_width - APP_WIDTH) / 2)
    c_height = int((mn_height - APP_HEIGHT) / 2)

    # モニターの中央に表示
    cur_root.geometry(
        "{}x{}+{}+{}".format(APP_WIDTH, APP_HEIGHT, c_width, c_height - 25)
    )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("tkinter application")

    # ウィンドウサイズと位置
    APP_WIDTH = 1280
    APP_HEIGHT = 820
    adjustScreen(root)

    # 最上位フレーム
    root_frame = tk.Frame(
        root,
        background="pink",  # 完成時はwhiteに変更
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )
    root_frame.propagate(False)
    root_frame.pack()

    # 各画面の生成 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ## ■■.frame_root:画面遷移のため
    
    # レシート画像確認画面の生成
    res1 = result.GenerateResult(root_frame, root)
    # レシート画像確認画面の生成
    c1 = confirm.GenerateConfirm(root_frame, root)

    # レシート登録画面の生成
    ## canvas_prev:confirmのキャンバスに画像を表示するため
    ## info_text:confirmのlabel_infoの内容を変更するため
    r1 = regist.GenerateRegist(root_frame, c1.frame_root, c1.canvas_prev, c1.infoText)

    # ホーム画面の生成
    h1 = home.GenerateHome(root_frame, r1.frame_root)

    # メニューバーの生成
    m1 = menu.GenerateMenu(root_frame, h1.frame_root, r1.frame_root)

    res1.frame_root.tkraise()

    root.mainloop()
