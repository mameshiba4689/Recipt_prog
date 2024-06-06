import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk


# プログラム内で使用している関数やメソッド、プロパティなどの説明

## 作製した関数 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
### adjustScreen : アプリの画面をモニター中央に表示する関数
### change_frame(cur_frame) : 引数で与えられたフレームを最前面にする
### file_read() :ファイルを読み込む処理
### read_button_func :  画像選択ボタンが押されたときの処理

## メソッド ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
### propagate : 画面サイズの自動調整機能 True/False → ON/OFF
### tkraise : 指定したフレームを最前面にする
### place : 位置を指定して設置する
### pack(side="left") : アイテムを横並びに左から設置する
### pack(padx=70,pady=70) : アイテムの内側の余白指定(xなら左右,yなら上下)
### pack(fill="x",fill="y") : アイテムの幅や高さを画面サイズいっぱいにする(xなら幅,yなら高さ)

## プロパティ ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
### relief : ボタンの種類(見た目)を変えられる
### foreground : 文字色
### activebackground : クリック時の背景色
### activeforeground : クリック時の文字色

## その他 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
### if __name__ == "__main__"
# このif文以下は、直接ファイルを指定して実行した時のみ処理される
# このファイルを他のファイルでimportして使っていたら、if文以下は処理されない


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


def get_path():
    "画像選択"
    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename()
    if len(file_path) != 0:
        print(file_path)
        return file_path
    else:
        return ""


def read_button_func():
    "読み込みボタンが押された時の処理"
    global img1  # グローバル変数じゃないと画像が表示されない
    # ファイルを読み込み
    img_path = get_path()
    # 読み込んだ結果を画面に描画
    img1 = Image.open(img_path)
    img1 = img1.resize(size=(550, 700))
    img1 = ImageTk.PhotoImage(img1)  # 表示するイメージを用意

    imgConfirm_prev.create_image(  # キャンバス上にイメージを配置
        0,  # x座標
        0,  # y座標
        image=img1,  # 配置するイメージオブジェクトを指定
        tag="illust",  # タグで引数を追加する。
        anchor="nw",  # 配置の起点となる位置を左上隅に指定
    )

    change_frame(imgConfirm_frame)  # imgConfirm_frameを表示


def change_frame(cur_frame):
    "引数で与えられたフレームを最前面にする"
    cur_frame.tkraise()


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
        background="black",  # 完成時はwhiteに変更
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )
    root_frame.propagate(False)
    root_frame.pack()

    # ナビフレーム 開始 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ## nav_frame内で使う変数の定義
    navHeight = 70
    navFont = ("HG創英角ﾎﾟｯﾌﾟ体", 20)
    navBtnWidth = 20
    ## 部品(フレームやボタン)の定義
    nav_frame = tk.Frame(
        root_frame,
        background="#FFDA58",
        width=APP_WIDTH,
        height=navHeight,
    )

    nav_btn1 = tk.Button(
        nav_frame,
        text="ホーム",
        font=navFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",  # クリック時のbg色
        activeforeground="#101F45",  # クリック時のfg色
        relief="flat",  # ボタン外枠の種類
        width=navBtnWidth,
        command=lambda: change_frame(home_frame),
    )

    nav_btn2 = tk.Button(
        nav_frame,
        text="レシートの登録",
        font=navFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        cursor="plus",
        relief="flat",  # ボタン外枠の種類
        width=navBtnWidth,
        command=lambda: change_frame(regist_frame),
    )

    nav_btn3 = tk.Button(
        nav_frame,
        text="レポートの確認",
        font=navFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        relief="flat",  # ボタン外枠の種類
        width=navBtnWidth,
    )

    ## 部品の実体化
    nav_frame.propagate(False)
    nav_frame.pack()
    nav_btn1.pack(side="left", padx=70, fill="y")
    nav_btn2.pack(side="left", padx=70, fill="y")
    nav_btn3.pack(side="left", padx=70, fill="y")
    # ナビフレーム 終了 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    # ホームフレーム 開始 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ## home_frame内で使う変数の定義
    homeFont = ("HGｺﾞｼｯｸE", 32)
    ## 部品(フレームやボタン)の定義
    home_frame = tk.Frame(
        root_frame,
        background="white",
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )

    home_label1 = tk.Label(
        home_frame,
        text="ようこそ、レシート読取アプリへ！！",
        font=homeFont,
        foreground="#35265E",
        background="white",
    )
    home_label2 = tk.Label(
        home_frame,
        text="以下からタスクをお選びください",
        font=homeFont,
        foreground="#35265E",
        background="white",
    )

    home_btn1 = tk.Button(
        home_frame,
        text="レシートを\n登録",
        font=homeFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        cursor="plus",
        relief="flat",  # ボタン外枠の種類
        padx=55,
        pady=65,
        command=lambda: change_frame(regist_frame),
    )

    home_btn2 = tk.Button(
        home_frame,
        text="レポートの\n確認",
        font=homeFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        relief="flat",  # ボタン外枠の種類
        padx=55,
        pady=65,
    )

    ## 部品の実体化
    home_frame.propagate(False)
    home_frame.place(x=0, y=navHeight)
    home_label1.place(x=280, y=130)
    home_label2.place(x=310, y=190)
    home_btn1.place(x=200, y=330)
    home_btn2.place(x=730, y=330)
    # ホームフレーム 終了 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    # レシート登録画面 開始 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ## home_frame内で使う変数の定義
    registFont = ("HGｺﾞｼｯｸE", 32)
    img_path = ""
    ## 部品(フレームやボタン)の定義
    regist_frame = tk.Frame(
        root_frame,
        background="#50c281",  # 確認用色 本番はwhite
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )
    regist_label1 = tk.Label(
        regist_frame,
        text="レシート画像を選択してください",
        font=homeFont,
        foreground="#35265E",
        background="white",
    )
    regist_btn1 = tk.Button(
        regist_frame,
        text="フォルダ―を開く",
        font=registFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        cursor="plus",
        relief="flat",  # ボタン外枠の種類
        padx=180,
        pady=130,
        command=lambda: read_button_func(),
    )

    ## 部品の実体化
    regist_frame.place(x=0, y=navHeight)
    regist_label1.place(x=310, y=120)
    regist_btn1.place(x=265, y=270)

    # レシート登録画面 終了 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    # レシート画像確認画面 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ##  imgConfirm_frameで使う変数の定義
    imgConfirmFont = ("HGｺﾞｼｯｸE", 32)
    ## 部品(フレームやボタン)の定義
    imgConfirm_frame = tk.Frame(
        root_frame,
        background="white",  # 確認用色 本番はwhite
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )
    imgConfirm_prev = tk.Canvas(imgConfirm_frame, width=550, height=700, bg="gray")
    imgConfirm_label1 = tk.Label(
        imgConfirm_frame,
        text="画像のプレビュー",
        font=imgConfirmFont,
        foreground="#302600",
        background="#ffda58",
        padx=110,
        pady=5,
    )
    imgConfirm_label2 = tk.Label(
        imgConfirm_frame,
        text="こちらの画像を読み込みます\n読み取りを開始しますか？",
        font=imgConfirmFont,
        foreground="#35265E",
        background="white",
    )
    imgConfirm_btn1 = tk.Button(
        imgConfirm_frame,
        text="戻る",
        font=imgConfirmFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#ffa98e",
        activeforeground="#962400",
        cursor="plus",
        relief="flat",  # ボタン外枠の種類
        padx=20,
        pady=10,
        # command=lambda: read_button_func(root),
    )
    imgConfirm_btn2 = tk.Button(
        imgConfirm_frame,
        text="開始",
        font=imgConfirmFont,
        background="#FECD21",
        foreground="#302600",
        activebackground="#7886A8",
        activeforeground="#101F45",
        cursor="plus",
        relief="flat",  # ボタン外枠の種類
        padx=20,
        pady=10,
        # command=lambda: read_button_func(root),
    )
    ## 部品の実体化
    imgConfirm_frame.propagate(False)
    imgConfirm_frame.place(x=0, y=navHeight)
    imgConfirm_prev.place(x=50, y=25)
    imgConfirm_label1.place(x=660, y=100)
    imgConfirm_label2.place(x=666, y=270)
    imgConfirm_btn1.place(x=720, y=450)
    imgConfirm_btn2.place(x=1020, y=450)
    # レシート画像確認画面 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    # レシート画像確認画面 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    ##  imgConfirm_frameで使う変数の定義
    testFont = ("HGｺﾞｼｯｸE", 32)
    ## 部品(フレームやボタン)の定義
    test_frame = tk.Frame(
        root_frame,
        background="#FFFDD9",  # 確認用色 本番はwhite
        width=APP_WIDTH,
        height=APP_HEIGHT,
    )
    test_label1 = tk.Label(
        test_frame,
        text="読み取り結果",
        font=homeFont,
        foreground="black",
        background="#FFD15C",
        padx=10,
        pady=10,
    )

    test_label2 = tk.Label(
        test_frame,
        text="2024年  1月  1日  (月)         合計  1000円",
        font=homeFont,
        foreground="black",
        background="#FFE895",
        padx=10,
        pady=5,
    )

    test_Button1 = tk.Button(
        test_frame,
        text="戻る",
        font=homeFont,
        background="#F1E4FB",
        foreground="#302600",
        padx=20,
        pady=10,
    )
    test_Button2 = tk.Button(
        test_frame,
        text="送信",
        font=homeFont,
        background="#E7B2FF",
        foreground="#302600",
        padx=20,
        pady=10,
    )

    # imgConfirm_btn1 = tk.Button(
    #     imgConfirm_frame,
    #     text="戻る",
    #     font=imgConfirmFont,
    #     background="#FECD21",
    #     foreground="#302600",
    #     activebackground="#ffa98e",
    #     activeforeground="#962400",
    #     cursor="plus",
    #     relief="flat",  # ボタン外枠の種類
    #     padx=20,
    #     pady=10,
    #     # command=lambda: read_button_func(root),
    # )

    ## 部品の実体化
    test_frame.propagate(False)
    test_frame.place(x=0, y=navHeight)
    test_label1.place(x=500, y=30)
    test_label2.place(x=150, y=120)
    test_Button1.place(x=300,y=620)
    test_Button2.place(x=800,y=620)

    # test_frame.propagate(False)
    # imgConfirm_frame.place(x=0, y=navHeight)
    # imgConfirm_prev.place(x=50, y=25)
    # imgConfirm_label1.place(x=660, y=100)
    # imgConfirm_label2.place(x=666, y=270)
    # imgConfirm_btn1.place(x=720, y=450)
    # imgConfirm_btn2.place(x=1020, y=450)
    # レシート画像確認画面 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


    test_frame.tkraise()
    # アプリの起動
    root.mainloop()
