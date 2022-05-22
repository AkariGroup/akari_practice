#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q3-3.M5のディスプレイに'あか''きいろ''あお'と縦に3つ並べて表示してみましょう。
     文字の色はそれぞれの字と同じ色('あか'なら赤)にしましょう。
ヒント1: 前の文字を消さずに次の文字を表示する必要があります。
    　　 set_display_textの引数refreshをFalseにすると、前の表示を消さずに重ねて表示します。
ヒント2: 文字と背景の色は、画面の色変更と同じように黒なら'black'、白なら'white'を入れればOKです。
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする
from m5serial_server_py.m5serial_server_py import M5SerialServer
# sleep関数を使うためにtimeのライブラリをインポートする。
import time

def main(args=None):
    """
    メイン関数
    """

    # M5SerialServerのインスタンスを作成する。
    m5 = M5SerialServer()

    ### ここから問題  ###
    # 'あか'を表示
    # textは'あか'
    text = """(表示したい文字を入力)"""
    # 左右表示位置は真中揃え
    pos_x = -999
    # 上下表示位置は30
    pos_y = 30
    # 文字サイズは3
    size = 3
    # 文字色は赤
    text_color = """(表示したい色を入力)"""
    # 背景色は白
    back_color = 'white'
    # 最初の１つ目は背景をリセットする
    refresh = """(TrueかFalseを入力)"""
    # set_display_textを実行
    result = m5.set_display_text(text, pos_x, pos_y, size, text_color, back_color, refresh)
    # 0.5秒停止
    time.sleep(0.5)

    # 'きいろ'を表示
    # textは'きいろ'
    text = """(表示したい文字を入力)"""
    # 左右表示位置は真中揃え
    pos_x = -999
    # 上下表示位置は90
    pos_y = 90
    # 文字サイズは3
    size = 3
    # 文字色は黄色
    text_color = """(表示したい色を入力)"""
    # 背景色は白
    back_color = 'white'
    # 前の文字を消さないために、背景はリセットしない。
    refresh = """(TrueかFalseを入力)"""
    # set_display_textを実行
    result = m5.set_display_text(text, pos_x, pos_y, size, text_color, back_color, refresh)
    # 0.5秒停止
    time.sleep(0.5)

    # 'あお'を表示
    # textは'あお'
    text = """(表示したい文字を入力)"""
    # 左右表示位置は真中揃え
    pos_x = -999
    # 上下表示位置は150
    pos_y = 150
    # 文字サイズは3
    size = 3
    # 文字色は青
    text_color = """(表示したい色を入力)"""
    # 背景色は白
    back_color = 'white'
    # 前の文字を消さないために、背景はリセットしない。
    refresh = """(TrueかFalseを入力)"""
    # set_display_textを実行
    result = m5.set_display_text(text, pos_x, pos_y, size, text_color, back_color, refresh)
    # 0.5秒停止
    time.sleep(0.5)

    ### ここまで  ###


if __name__ == '__main__':
    main()
