#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random

class co:
    BLACK = '\033[30m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    WHITE = '\033[37m'
    END = '\033[0m'
    
endnum = 0
a0 = input("＞名前を入力")
print("エンターを押してシャーロちゃんとじゃんけんをしよう！！")
a1 = input("＞")

# トリガーは以下の通り。
if a1 in ["!じゃんけんしよ","!じゃんけん","！じゃんけんしよ","！じゃんけん",""]:
    while True:
        print("----------------------------------------------------------------------")
        print("＞",a0,"は何を出す？")
        e = input("1:グー, 2:チョキ, 3:パー")
        # おんそくさんが出す手（1:グー, 2:チョキ, 3:パー）を乱数で生成
        f = random.randint(1,3)
        # プレイヤーがグーを出した場合
        if e in ["1","１","グー","1:グー"]:
            print("...")
            print(a0,"は",co.BLUE+"グー"+co.END,"を出した。")
            # おんそくさんがグーだった場合
            if f == 1:
                print("...")
                print("シャーロちゃんと拳がぶつかり合った！！その拳は",co.RED+"グー"+co.END,"の形で強く握られていた！！")
                print("...")
                print("結果：あいこ")
                # おんそくさんがチョキだった場合
            elif f == 2:
                print("...")
                print("シャーロちゃんは「勝利の...",co.RED+"チョキ"+co.END,"...」と言いながら地面に伏し、力尽きたのであった...。")
                print("...")
                print("結果：",a0,"の勝ち")
                # おんそくさんがパーだった場合
            elif f == 3:
                print("...")
                print("シャーロちゃんの",co.RED+"パー"+co.END,"に開かれた手から繰り出される平手打ちになすすべはなかった...。")
                print("...")
                print("結果：",a0,"の負け")
        # プレイヤーがチョキを出した場合
        elif e in ["2","２","チョキ","2:チョキ"]:
            print("...")
            print(a0,"は",co.BLUE+"チョキ"+co.END,"を出した。")
            if f == 1:
                print("...")
                print("シャーロちゃんに",co.RED+"グー"+co.END,"で思いっきり殴られた...。")
                print("...")
                print("結果：",a0,"の負け")
            elif f == 2:
                print("...")
                print("お互いが掲げた",co.RED+"チョキ"+co.END,"は世界の平和(ピース)を願ったものだった！！争いがまた次の争いを生むことを二人は理解していた！！")
                print("...")
                print("結果：あいこ")
            elif f == 3:
                print("...")
                print("酒を飲んでしまったシャーロちゃんはあっぱら",co.RED+"パー"+co.END,"なってしまった！！")
                print("...")
                print("結果：",a0,"の勝ち")
            # プレイヤーがパーを出した場合
        elif e in ["3",",３","パー","3:パー"]:
            print("...")
            print(a0,"は",co.BLUE+"パー"+co.END,"を出した。")
            if f == 1:
                print("...")
                print("シャーロちゃん専属調教師となった",a0,"はシャーロちゃんを正座させ、手をお膝に",co.RED+"グー"+co.END,"で置かせた後、思いっきり頬に平手打ちした。")
                print("...")
                print("結果：",a0,"の勝ち")
            elif f == 2:
                print("...")
                print("「勝利の",co.RED+"チョキ"+co.END,"！！」とシャーロちゃんが言う頃には自分の体にはハサミによる刺し傷が28か所にも及んでいた。")
                print("...")
                print("結果：",a0,"の負け")
            elif f == 3:
                print("...")
                print("気が付けば",a0,"はシャーロちゃんとハイタッチをしていた。そこには",co.RED+"パー"+co.END,"をした手と笑顔、そして奇妙な運命があった。")
                print("...")
                print("結果：あいこ")
        # 規定された文字以外の入力がされたときの処理
        else:
            print("エラーが発生しました。")
            print("入力が無効です。")
            print("入力は[1,2,3]または[グー,チョキ,パー]のみ有効です。")
        print("...")
        endnum = input(">1.続ける, 2.終了")
        if endnum in ["1","１","続ける","1.続ける"]:
            print("...")
            continue
        elif endnum in ["2","２","終了","2.終了"]:
            print("終了します。")
            break
        else:
            print("無効な入力です。終了します。")
elif a1 == "!help" :
    print("よく気が付きましたね。",a0,"さん!!")
    print("あいにくですが、今のところヘルプはありません。")
    print("遊んでくれてありがとう！！")
    
# 規定された文字以外の入力がされたときの処理    
else:
    print("エラーが発生しました。")
    print("入力が無効です。")
    print("入力は[!じゃんけんしよ","!じゃんけん","！じゃんけんしよ","！じゃんけん","エンター]のみ有効です。")


# In[ ]:




