import tkinter as tk
import menu
import tkinter.filedialog as fd
from PIL import Image, ImageTk


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


class GenerateRegist:
    """レシート登録画面の生成"""

    # クラス変数    ※他のクラスからも使用する可能性のある変数のため
    frame_root = None
    mnHeight = menu.GenerateMenu.mnHeight
    img01 = None
    image_path = None

    def __init__(self, parent, nextFrame, canvas_prev, infoText):
        """ここでインスタンス変数の宣言や部品の生成をしている\n
        ※インスタンス時に必ず親フレームの変数名を入れる"""
        # インスタンス変数
        self.parent = parent
        self.nextFrame = nextFrame
        self.canvas_prev = canvas_prev
        self.infoText = infoText

        # 画面の作成
        self.create_widget()

    def create_widget(self):
        """画面の作成"""
        # 部品(ウィジェット)の定義
        ## フレーム ------------------------------------
        self.frame_root = tk.Frame(
            self.parent,
            background="white",
        )
        ## ボタン ------------------------------------
        btn_openFolder = tk.Button(
            self.frame_root,
            text="フォルダ―を開く",
            font=("HGｺﾞｼｯｸE", 32),
            background="#FECD21",
            foreground="#302600",
            activebackground="#7886A8",
            activeforeground="#101F45",
            cursor="plus",
            relief="flat",  # ボタン外枠の種類
            padx=180,
            pady=130,
            command=lambda: self.open_button_func(),
        )
        ## ラベル ------------------------------------
        label_selectRecipt = tk.Label(
            self.frame_root,
            text="レシート画像を選択してください",
            font=("HGｺﾞｼｯｸE", 32),
            foreground="#35265E",
            background="white",
        )
        # 部品(ウィジェット)の配置
        ## フレーム ------------------------------------
        self.frame_root.propagate(False)
        self.frame_root.place(x=0, y=self.mnHeight, relwidth=1.0, relheight=1.0)
        ## ボタン ------------------------------------
        btn_openFolder.place(x=265, y=270)
        ## ラベル ------------------------------------
        label_selectRecipt.place(x=310, y=120)


    def get_path(self):
        """画像選択＆画像の絶対パスを取得"""
        # ファイル選択ダイアログの表示
        file_path = fd.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if len(file_path) != 0:  # 画像が選択されたとき
            self.nextFrame.tkraise()
            return file_path
        else:  # 画像が選択されなかった/×ボタン(close)が押されたとき
            return ""

    def open_button_func(self):
        "フォルダーを開いて画像を表示"
        # ファイルを読み込み
        self.image_path = self.get_path()
        # print(img_path, "文字数:" + str(len(img_path)))  # パスが指定されてるかの確認用

        # 表示中の画像があれば削除
        self.canvas_prev.delete("previewIMG")

        # 画像を画面に描画
        if len(self.image_path):
            self.img01 = Image.open(self.image_path)
            self.img01 = self.img01.resize(size=(550, 700))
            self.img01 = ImageTk.PhotoImage(self.img01)  # 表示するイメージを用意
            self.canvas_prev.create_image(  # キャンバス上にイメージを配置
                0,  # x座標
                0,  # y座標
                image=self.img01,  # 配置するイメージオブジェクトを指定
                tag="previewIMG",  # タグで引数を追加する。
                anchor="nw",  # 配置の起点となる位置を左上隅に指定
            )
            self.infoText.set("読み取りを開始しますか？")
            self.nextFrame.tkraise()  # imgConfirm_frameを表示
        else:
            print("画像が指定されていません")  # 画像が選択されなかった時の処理
            self.infoText.set("画像を選択してください。")
            # imgConfirm_label2.config(foreground="#e06c75",bg="#282c34")
            # imgConfirm_frame.config(bg="#282c34")
