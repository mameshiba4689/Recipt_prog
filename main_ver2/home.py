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


class GenerateHome:
    """ホーム画面(Welcome画面)の生成"""

    # クラス変数    ※他のクラスからも使用する可能性のある変数のため
    frame_root = None
    mnHeight = menu.GenerateMenu.mnHeight

    def __init__(self, parent, nextFrame):
        """ここでインスタンス変数の宣言や部品の生成をしている\n
        ※インスタンス時に必ず親フレームの変数名を入れる"""
        # インスタンス変数
        self.parent = parent
        self.nextFrame = nextFrame
        # self.graph_frame = graph_frame

        # 画面の作成
        self.create_widget()

    def create_widget(self):
        """画面作成"""
        # 部品(ウィジェット)の定義
        ## フレーム ------------------------------------
        self.frame_root = tk.Frame(
            self.parent,
            background="white",
        )
        ## ボタン ------------------------------------
        btn_regist = tk.Button(
            self.frame_root,
            text="レシートを\n登録",
            font=("HGｺﾞｼｯｸE", 32),
            background="#FECD21",
            foreground="#302600",
            activebackground="#7886A8",
            activeforeground="#101F45",
            cursor="plus",
            relief="flat",  # ボタン外枠の種類
            padx=55,
            pady=65,
            command=lambda: self.nextFrame.tkraise(),
        )
        btn_graph = tk.Button(
            self.frame_root,
            text="レポートの\n確認",
            font=("HGｺﾞｼｯｸE", 32),
            background="#FECD21",
            foreground="#302600",
            activebackground="#7886A8",
            activeforeground="#101F45",
            cursor="plus",
            relief="flat",  # ボタン外枠の種類
            padx=55,
            pady=65,
            # command=lambda: change_frame(regist_frame),
        )
        ## ラベル ------------------------------------
        label_welcome = tk.Label(
            self.frame_root,
            text="ようこそ、レシート読取アプリへ！！",
            font=("HGｺﾞｼｯｸE", 32),
            foreground="#35265E",
            background="white",
        )
        label_selctTsk = tk.Label(
            self.frame_root,
            text="以下からタスクをお選びください",
            font=("HGｺﾞｼｯｸE", 32),
            foreground="#35265E",
            background="white",
        )
        # 部品(ウィジェット)の配置
        ## フレーム ------------------------------------
        self.frame_root.propagate(False)
        self.frame_root.place(x=0, y=self.mnHeight, relwidth=1.0, relheight=1.0)
        ## ボタン ------------------------------------
        btn_regist.place(x=200, y=330)
        btn_graph.place(x=730, y=330)
        ## ラベル ------------------------------------
        label_welcome.place(x=280, y=130)
        label_selctTsk.place(x=310, y=190)
