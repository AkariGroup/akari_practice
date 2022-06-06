#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-2.テストヘッドのdin0ボタン入力があったときにコマンドラインに「din0がONです」と表示されるようにしましょう
ヒント1: Q1を参考にしましょう。'button_a'の代わりに'din0'の値を使います。
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする
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
    while(True):
        m5_data = m5.get()
        if(m5_data['din0']):
            print("din0がONです")
        time.sleep(0.1)
    ### ここまで  ###


if __name__ == '__main__':
    main()
