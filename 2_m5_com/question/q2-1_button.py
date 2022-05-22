#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-1.ボタンAが押されたらコマンドラインに「ボタンAが押されています」と表示されるようにしましょう。
ヒント1: get()関数を使うとM5の値が取得できます。
ヒント2: if文を使って、ボタンAが押された場合だけコマンドラインに出力するようにしましょう。
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
        # データが取得できた場合(result=True)はボタンが押されているか判定。
        # 失敗した場合(result=False)はエラー文を表示。
        if(result):
            if("""(ボタンAが押されているかの判定処理)"""):
                """(コマンドラインに出力する処理)"""
        else:
            print("データ取得に失敗しました")
        # 0.1秒停止処理を入れる。
        time.sleep(0.1)
    ### ここまで  ###


if __name__ == '__main__':
    main()
