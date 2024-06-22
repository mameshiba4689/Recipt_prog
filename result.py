import tkinter as tk
import menu


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
        self.content_Height = 0  # インスタンス変数としてcontent_Heightを定義  

        # 画面の作成
        self.create_widget()

    def create_widget(self):
        """画面の作成"""
        # 部品(ウィジェット)の定義
        background_color = "#FFFDD9"  # 統一する背景色

        ## フレーム ------------------------------------
        self.frame_root = tk.Frame(
            self.parent,
            background=background_color,
        )
        
        sub_frame_root = tk.Frame(
            self.frame_root,
            background=background_color,
        )

        #商品詳細表示関数-------------------------------
        def for_tekito(cnt):
            self.content_Height=cnt*50
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
                frame,
                background=cur_color,
                width=980,
                height=50,
            )

            #商品詳細表示
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
            Content_frame1.place(x=0,y=0+self.content_Height)
            Content_label1.place(x=30,y=3)
            Content_label2.place(x=250,y=3)
            Content_label3.place(x=820+keta,y=3)
            

        #スクロール実装において必要なキャンバスとフレームの設定
        canvas = tk.Canvas(sub_frame_root, background=background_color, highlightthickness=0)
        frame = tk.Frame(canvas, background=background_color)

        #合計桁数調べ-----------------------------------
        gokei_hen = 100
        gokei_nedan = str(gokei_hen)
        gokei_keta = -28 * (len(gokei_nedan)-3)

        
        #タイトル表示-----------------------------------
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
        
        #ボタン設定-------------------------------------
        content_Button1 = tk.Button(
            self.frame_root,
            text="戻る",
            font=("UD デジタル 教科書体 NK-B", 30),
            background="#FFC702",
            foreground="#302600",
            relief="flat",
            padx=20,
            pady=10,
            command=lambda: self.home_frame.tkraise(),

        )
        
        content_Button2 = tk.Button(
            self.frame_root,
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
        
        resultCheck_dateFrame.place(x=150, y=120)
        resultCheck_dateLabel1.place(x=30, y=2.5)
        resultCheck_dateLabel2.place(x=190, y=2.5)
        resultCheck_dateLabel3.place(x=370, y=2.5)
        resultCheck_dateLabel4.place(x=650, y=2.5)
        resultCheck_dateLabel5.place(x=820 + gokei_keta, y=2.5)


        content_Button1.place(x=300, y=620)
        content_Button2.place(x=800, y=620)
        
        #商品数分追加------------------------------------
        for i in range(0, 8):
            for_tekito(i)


        #スクロール実装----------------------------------
        # 商品の個数によってsub_frame_rootの大きさ変更
        sub_frame_root.place(x=150, y=170, width=980, height=400)

        #商品数が8個以上の時だけスクロールバーを表示するif文
        if self.content_Height > 400:
            # Canvasを親とした縦方向のScrollbar
            scrollbar = tk.Scrollbar(
                canvas, orient=tk.VERTICAL, command=canvas.yview
            )

            # スクロールの設定
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # スクロールできる範囲指定
            canvas.configure(scrollregion=(0, 0, 980, self.content_Height + 50))

            # 諸々を配置
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.pack(expand=True, fill=tk.BOTH)

        # Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
        canvas.create_window((0, 0), window=frame, anchor="nw", width=980, height=self.content_Height + 50)



