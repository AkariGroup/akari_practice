#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q3-4.M5のディスプレイに圧力センサの値を表示しましょう。
ヒント1: 圧力センサの値を返す独自関数 get_pressure() を作成してあります。これを使ってみましょう。
         返り値として圧力値が文字列で得られます。
ヒント2: コメントを参考に、引数を穴埋めしましょう。
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする。
from m5serial_server_py.m5serial_server_py import M5SerialServer
# sleep関数を使うためにtimeのライブラリをインポートする。
import time
# M5SerialServerのインスタンスを作成する。
m5 = M5SerialServer()


def get_pressure() -> str:
    """
    圧力センサの値を返す独自関数
    引数:なし
    返り値: 圧力値の文字列
    """
    m5_data = m5.get()
    # 圧力センサ値を小数点以下２桁にして、単位hPaを付けて返す。
    return (str(round(m5_data['pressure'] / 100, 2)) + 'hPa')


def main() -> None:
    """
    メイン関数
    """
    # M5のディスプレイの背景色を黒にする
    m5.set_display_color("black")

    ### ここから問題  ###
    while(True):
        # 表示する圧力センサ値は、独自関数を呼び出して取得する。
        text = get_pressure()
        # 左右表示位置は真中揃え
        pos_x = -999
        # 上下表示位置は中央揃え
        pos_y = -999
        # 文字サイズは3にする
        size = 3
        # 文字色は白
        text_color = 'white'
        # 背景色は黒
        back_color = 'black'
        # 背景をリセットする
        refresh = True
        # set_display_textを実行
        result = m5.set_display_text(
            text, pos_x, pos_y, size, text_color, back_color, refresh)
        # 1秒停止
        time.sleep(1)
    ### ここまで  ###


if __name__ == '__main__':
    main()
