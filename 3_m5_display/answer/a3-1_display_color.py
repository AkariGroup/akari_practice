#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q3-1.M5のディスプレイの背景色を赤→黄→青に変えてみましょう。
ヒント1: 色を変えるにはset_display_color(str color)という関数を使います。
         colorに色の名前を入れるとその色に背景色が変わります。赤は"red",黄色は"yellow",青は"blue"を入れます。
         例:
            m5.set_display_color("red")
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする。
from m5serial_server_py.m5serial_server_py import M5SerialServer
# sleep関数を使うためにtimeのライブラリをインポートする。
import time


def main() -> None:
    """
    メイン関数
    """

    # M5SerialServerのインスタンスを作成する。
    m5 = M5SerialServer()

    ### ここから問題  ###
    # M5のディスプレイの色を赤にする
    m5.set_display_color("red")
    # 2秒停止処理を入れる。
    time.sleep(2)
    # M5のディスプレイの色を赤にする
    m5.set_display_color("yellow")
    # 2秒停止処理を入れる。
    time.sleep(2)
    # M5のディスプレイの色を赤にする
    m5.set_display_color("blue")
    # 2秒停止処理を入れる。
    time.sleep(2)
    ### ここまで  ###


if __name__ == '__main__':
    main()
