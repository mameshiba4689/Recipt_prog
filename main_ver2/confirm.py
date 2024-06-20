import tkinter as tk
import menu


# 部品を作成するときの "命名ルール" ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
## 関数名
### 画面を作成するときは「create_widget()」関数の中に記述する

## フレーム
### そのクラスの中の最上位フレームの変数名は「frame_root」とする
### 以後のフレームは階層が深くなるごとに「frame_second」,「frame_third」と数字を挙げていく
### もし、同じ階層内に複数のフレームを作りたいときは、「frame_second01,02,03...」と数字を挙げていく

## ボタン,ラベルなど
###「btn_■■」,「label_■■」のように、頭に部品の種類を付ける
### ■■ はその部品のテキストや役割に応じた名前を付ける


# コードの説明 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
## __init__:Javaのコンストラクタと同じもの
## self : そのクラス自体を表している 「self.■■」でそのクラスに変数を追加できる
##  例)__init__()の中で「self.parent」と宣言するのと、
##     クラス変数の中で「parent」と宣言するのはほとんど同じ意味になる
##       なので、使用するときはインスタンス変数もクラス変数も「self.■■」と指定する


# 関数やプロパティ、変数の説明 ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
## 変数
### frame_root : そのクラスの全てのフレームの中で最上位に位置するフレーム
###                 画面の大枠のようなもの main.pyのroot_frameの子に該当する
### parent または self.parent :
###     main.pyでインスタンス化した時の第一引数で指定されたもの 親フレームを指す


class GenerateConfirm:
    """レシート画像確認画面の生成"""

    # クラス変数    ※他のクラスからも使用する可能性のある変数のため
    frame_root = None
    mnHeight = menu.GenerateMenu.mnHeight
    canvas_prev = None
    infoText = None

    def __init__(self, parent, root):
        """ここでインスタンス変数の宣言や部品の生成をしている\n
        ※インスタンス時に必ず親フレームの変数名を入れる"""
        # インスタンス変数
        self.parent = parent
        self.root = root

        # 画面の作成
        self.create_widget()

    def create_widget(self):
        """画面の作成"""
        # label_infoで使用するテキストの変数
        self.infoText = tk.StringVar(self.root)
        self.infoText.set("読み取りを開始しますか？")

        # 部品(ウィジェット)の定義
        ## フレーム ------------------------------------
        self.frame_root = tk.Frame(
            self.parent,
            background="white",
        )
        ## ボタン ------------------------------------
        btn_back = tk.Button(
            self.frame_root,
            text="戻る",
            font=("HGｺﾞｼｯｸE", 32),
            background="#FECD21",
            foreground="#302600",
            activebackground="#ffa98e",
            activeforeground="#962400",
            cursor="plus",
            relief="flat",  # ボタン外枠の種類
            padx=20,
            pady=10,
            # command=lambda: read_button_func(),
        )
        btn_start = tk.Button(
            self.frame_root,
            text="開始",
            font=("HGｺﾞｼｯｸE", 32),
            background="#FECD21",
            foreground="#302600",
            activebackground="#7886A8",
            activeforeground="#101F45",
            cursor="plus",
            relief="flat",  # ボタン外枠の種類
            padx=20,
            pady=10,
            # command=lambda: read_button_func(),
        )
        ## ラベル ------------------------------------
        label_imgPreview = tk.Label(
            self.frame_root,
            text="画像のプレビュー",
            font=("HGｺﾞｼｯｸE", 32),
            foreground="#302600",
            background="#ffda58",
            padx=110,
            pady=5,
        )
        label_info = tk.Label(
            self.frame_root,
            textvariable=self.infoText,
            font=("HGｺﾞｼｯｸE", 32),
            foreground="#35265E",
            background="white",
        )
        ## キャンバス ------------------------------------
        self.canvas_prev = tk.Canvas(self.frame_root, width=550, height=700, bg="gray")

        # 部品(ウィジェット)の配置
        ## フレーム ------------------------------------
        self.frame_root.propagate(False)
        self.frame_root.place(x=0, y=self.mnHeight, relwidth=1.0, relheight=1.0)
        ## ボタン ------------------------------------
        btn_back.place(x=720, y=450)
        btn_start.place(x=1020, y=450)
        ## ラベル ------------------------------------
        label_imgPreview.place(x=660, y=100)
        label_info.place(x=685, y=280)
        ## キャンバス ------------------------------------
        self.canvas_prev.place(x=50, y=25)

