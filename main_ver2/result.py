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


class GenerateResult:
    """レシート画像確認画面の生成"""

    # クラス変数    ※他のクラスからも使用する可能性のある変数のため
    frame_root = None
    mnHeight = menu.GenerateMenu.mnHeight


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
        # 部品(ウィジェット)の定義
        ## フレーム ------------------------------------
        self.frame_root = tk.Frame(
            self.parent,
            background="#FFFDD9",
        )

        def for_tekito(cnt):
            content_Height=cnt*50
            hen = 100000
            nedan = str(hen)
            keta= -28 * (len(nedan)-3)
                
                
            color_arr = ["#FFFFFF","#D9D9D9"]
            cur_color = ""
            if cnt%2 == 0 :
                cur_color = color_arr[0]
            else :
                cur_color = color_arr[1]
            Content_frame1 = tk.Frame(
                self.frame_root,
                background=cur_color,
                width=980,
                height=50,
            )

            Content_label1 = tk.Label(
                Content_frame1,
                text="分類",
                font=("UD デジタル 教科書体 NK-B",30),
                foreground="black",
                background=cur_color,
            )

            Content_label2 = tk.Label(
                Content_frame1,
                text="商品名",
                font=("UD デジタル 教科書体 NK-B",30),
                foreground="black",
                background=cur_color,
            )

            Content_label3 = tk.Label(
                Content_frame1,
                text=nedan + "円",
                font=("UD デジタル 教科書体 NK-B",30),
                foreground="black",
                background=cur_color,
            )
            Content_frame1.propagate(False)
            Content_frame1.place(x=150,y=170+content_Height)
            Content_label1.place(x=30,y=3)
            Content_label2.place(x=250,y=3)
            Content_label3.place(x=820+keta,y=3)

        #合計桁数調べ
        gokei_hen = 100
        gokei_nedan = str(gokei_hen)
        gokei_keta = -28 * (len(gokei_nedan)-3)

        
        #タイトル表示
        resultCheck_titleLabel = tk.Label(
            self.frame_root,
            text="読み取り結果",
            font=("UD デジタル 教科書体 NK-B", 30),
            foreground="black",
            background="#FFD15C",
            padx=10,
            pady=10,
        )

        #日付のフレーム
        resultCheck_dateFrame = tk.Frame(
            self.frame_root,
            background="#FFD15C",
            width=980,
            height=50,
        )

        resultCheck_dateLabel1 = tk.Label(
            resultCheck_dateFrame,
            text="2024年",
            font=("UD デジタル 教科書体 NK-B", 28),
            foreground="black",
            background="#FFD15C",
        )
    
        resultCheck_dateLabel2 = tk.Label(
            resultCheck_dateFrame,
            text="1月  1日",
            font=("UD デジタル 教科書体 NK-B", 30),
            foreground="black",
            background="#FFD15C",
        )
        
        resultCheck_dateLabel3 = tk.Label(
            resultCheck_dateFrame,
            text="(月)",
            font=("UD デジタル 教科書体 NK-B", 30),
            foreground="black",
            background="#FFD15C",
        )
        
        resultCheck_dateLabel4 = tk.Label(
            resultCheck_dateFrame,
            text="合計",
            font=("UD デジタル 教科書体 NK-B", 30),
            foreground="black",
            background="#FFD15C",
        )
        
        resultCheck_dateLabel5 = tk.Label(
            resultCheck_dateFrame,
            text= gokei_nedan + "円",
            font=("UD デジタル 教科書体 NK-B", 30),
            foreground="black",
            background="#FFD15C",
        )
        

        content_Button1 = tk.Button(
             resultCheck_dateFrame,
            text="戻る",
            font=("UD デジタル 教科書体 NK-B", 30),
            background="#FFC702",
            foreground="#302600",
            relief="flat",
            padx=20,
            pady=10,
        )
        
        content_Button2 = tk.Button(
             resultCheck_dateFrame,
            text="送信",
            font=("UD デジタル 教科書体 NK-B", 30),
            background="#FFC702",
            foreground="#302600",
            relief="flat",
            padx=20,
            pady=10,
        )

        # 部品(ウィジェット)の配置
        ## フレーム ------------------------------------
        self.frame_root.propagate(False)
        self.frame_root.place(x=0, y=self.mnHeight, relwidth=1.0, relheight=1.0)
        
        resultCheck_titleLabel.place(x=500, y=30)
        
        resultCheck_dateFrame.place(x=150,y=120)
        resultCheck_dateLabel1.place(x=30, y=2.5)
        resultCheck_dateLabel2.place(x=190, y=2.5)
        resultCheck_dateLabel3.place(x=370, y=2.5)
        resultCheck_dateLabel4.place(x=650, y=2.5)
        resultCheck_dateLabel5.place(x=820 + gokei_keta, y=2.5)


        content_Button1.place(x=300,y=620)
        content_Button2.place(x=800,y=620)
        
        for i in range(0,8):
            for_tekito(i)




