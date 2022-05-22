#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-5.環境温度を取得して1秒ごとにコマンドラインに表示しましょう。
ヒント1: Q2-1を参考に、get()関数を使ってM5の値を取得しましょう。
         返り値の'temperature'の項目から温度が読めます。
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
    # Ctrl + Cで終了するまでループし続ける
    while(True):
        result, m5_data = """(M5から値を取得する関数)"""
        # データが取得できた場合(result=True)の場合は温度表示。
        # 失敗した場合(result=False)の場合はエラー文を表示。
        if(result):
            """(温度をコマンドラインに表示する処理)"""
        else:
            print("データ取得に失敗しました")
        # 1秒停止処理を入れる。
        """(1秒停止する処理)"""
    ### ここまで  ###


if __name__ == '__main__':
    main()
