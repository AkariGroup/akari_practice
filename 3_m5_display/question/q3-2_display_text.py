#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q3-2.M5のディスプレイの真中中央に"こんにちは"という文字を表示してみましょう。
ヒント1: 文字を表示するにはset_display_text()という関数を使います。
         この関数は引数が多くやや複雑です。
         まずはコメントを読みながら穴埋めをし、コードを実行してみましょう。
         その後、変数を色々変えてどう表示が変わるか試してみましょう。
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
    # textは'こんにちは'
    text = """(表示したい文字を入力)"""
    # 左右表示位置を0-320で座標指定。0が左。-999を入れると真中揃え。999を入れると右揃え
    pos_x = """(真ん中の数値を入力)"""
    # 上下表示位置を-240で座標指定。0が上。-999を入れると中央揃え。999を入れると右揃え
    pos_y = """(中央の数値を入力)"""
    # 文字サイズは3
    size = 3
    # 文字色は黒
    text_color = """(黒を指定)"""
    # 背景色は白
    back_color = """(白を指定)"""
    # 背景をリセット
    refresh = True
    # set_display_textを実行
    result = m5.set_display_text(text, pos_x, pos_y, size, text_color, back_color, refresh)
    ### ここまで  ###


if __name__ == '__main__':
    main()
