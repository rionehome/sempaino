#!/usr/bin/env python
# coding: utf-8

from sono import ittan
import time

if __name__=='__main__':
    i = ittan(angular=1.0)
    time.sleep(1)
    
    i.forword()
    i.left()
    i.right()
    i.linear = 0.1
    i.time = 2.0
    i.back()
    
"""
初めの方はプログラムを書く前段階のやつが多く、難しいです。そういうものという認識でOK。
詳しくは、頼りになる先輩たちに聞いてください。きっと答えられるでしょう!

    1行目は、シバン(シェバン)といい、コマンドラインから実行できるようにする魔法です。
    2行目は、このコードの中で、日本語を使えるようにしています。
    このコメントアウトを日本語で書けているのもこれのおかげです。
    
    4行目は、僕の書いたクラスをこのプログラム内で使えるようにしています。
    クラスittanを使用できているのはこのおかげです。
    5行目は、timeライブラリをインポートしています。
    このおかげで、9行目の「1秒待つ」という動作ができています。
    
    7行目は、このプログラムがmainとして実行されたときの条件分岐です。魔法です。
    
    
ここから下が、書いてもらうプログラムに直結する部分になります。
文章だけでは限界があるので、分からないところは、遠慮なく聞いてください。

    クラスは、初期化(インスタンス化)しないと使えません。
    その初期化が、8行目です。
    変数iがインスタンスです。(インスタンスについては先輩へ)
    このクラスは、ittan(linear, angular, time)で定義されています。
        第1引数linearは、直線成分の速さです。
        第2引数angularは、回転成分の速さです。
        第3引数timeは、動作時間です。
    値を指定しない場合は、適当な値(linear=0.2, angular=0.5, time=1.0)に自動でセットされます。
    なので、この初期化の仕方は次のような例があります。
        ittan()                         -> linear=0.2, angular=0.5, time=1.0
        ittan(0.1, 1.0, 2.0)            -> linear=0.1, angular=1.0, time=2.0
        ittan(0.1, time=2.0)            -> linear=0.1, angular=0.5, time=2.0
        ittan(angular=1.0)              -> linear=0.2, angular=1.0, time=1.0
        ittan(linear=0.1, angular=1.0)  -> linear=0.1, angular=1.0, time=1.0
    
    9行目は、1秒プログラムを一時停止しています。
    これは、ロボットを動かすときの諸事情で必要です。
    
    11行目は、ittanクラスのメソッドを呼び出しています。
    ittanクラスは、以下のメソッドを持っています。
        forword()   : 前方へ1秒間移動する
        back()      : 後方へ1秒間移動する
        left()      : 上から見て半時計回りへ1秒間回転する
        right()     : 上から見て時計回りへ1秒間回転する
        custom()    : 指定した値で動作する
    この移動する速さや、回転する速さをlinearやangularで調整できます。
    custom()については、敢えて説明は書きませんので、どういう仕様か試してみてください。
    
    14,15行目は、ittanクラスのプロバティ(変数)を変更しています。
    このプログラムで使用するittanクラスのプロパティは以下です。
        linear  : 直線成分の速さ(-2.0〜2.0が安全な値です)
        angular : 回転成分の速さ(-1.0〜1.0が安全な値です)
        time    : 動作時間(s)
    この値は、インスタンス化するときにも設定できますが、14,15行目のように後から変更も出来ます。
    Turtlebotでは、速さを負の値にするとどうなるか、実験してみてください。
    
    以上を踏まえて、このプログラムの動作は、以下のようになります。
        1. 0.2の速さで、1秒直進
        2. 0.5の速さで、1秒左回転
        3. 0.5の速さで、1秒右回転
        4. 0.1の速さで、2秒後退
        
    以上がサンプルコードの説明になります。
    先輩たちは、たくさん聞いてほしいそうなので、ぜひ聞いてあげてください!
    もちろん、集団で開発していくことになるので、1年生同士での話し合いもどんどんやってください!
"""