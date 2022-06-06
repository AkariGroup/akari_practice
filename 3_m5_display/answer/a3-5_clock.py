#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q3-5. M5のディスプレイに時:分:秒を表示する時計を作りましょう。
ヒント1: 現在時刻を返す独自関数 get_time() を作成してあります。これを使ってみましょう。
         返り値として時:分:秒の文字列が得られます。
ヒント2: Q3-4を参考に書いてみましょう。
         背景の色、文字の色やサイズ、ループのあとの停止時間をどれくらいにするか、などで見栄えの良さが
         変わります。少し難しいですが、よりかっこいいアプリを目指して色々試してみましょう。
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする
from m5serial_server_py.m5serial_server_py import M5SerialServer
# sleep関数を使うためにtimeのライブラリをインポートする。
import time
# 時刻取得に必要なライブラリをインポートする。
import datetime
import locale
# M5SerialServerのインスタンスを作成する。
m5 = M5SerialServer()


def get_time() -> str:
    """
    現在時刻を返す独自関数
    引数:なし
    返り値: 時:分:秒の文字列
    """
    # 現在時刻を取得。
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    dt_now = datetime.datetime.now()
    # 時:分:秒を返す。
    return (dt_now.strftime('%H:%M:%S'))

### ここから問題  ###


def main() -> None:
    """
    メイン関数
    """
    # M5のディスプレイの背景色を黒にする
    m5.set_display_color("black")
    while(True):
        # 表示する時刻は、独自関数を呼び出して取得する。
        text = get_time()
        # 左右表示位置は真中揃え
        pos_x = -999
        # 上下表示位置は中央揃え
        pos_y = -999
        # 文字サイズは4にする
        size = 4
        # 文字色は白
        text_color = 'white'
        # 背景色は黒
        back_color = 'black'
        # 背景をリセットしない
        refresh = False
        # set_display_textを実行
        result = m5.set_display_text(
            text, pos_x, pos_y, size, text_color, back_color, refresh)
        # 0.3秒停止
        time.sleep(0.3)


if __name__ == '__main__':
    main()
### ここまで  ###
