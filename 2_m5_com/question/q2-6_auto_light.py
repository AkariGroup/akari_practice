#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-6.環境明るさの取得値をコマンドラインに表示し、
     3000以上の場合のみ、テストヘッドのdout0のLEDをONにする自動ライトを作りましょう。
ヒント1: Q2-3とQ2-5を参考にしましょう。
         get関数の返り値の'brightness'の項目から明るさが読めます。
ヒント2: AKARIのボディー部の、AKARIから見て右側面に明るさセンサがついています。
         ここに光を当てたり、指で覆ったりするとbrightnessの値が0-4095で変化します。
         暗くなるほどbrightnessの値は大きくなります。
ヒント3: 3000未満の時はLED0は消しましょう。
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする。
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
            # 取得した明るさをコマンドラインに表示。
            """(明るさ値をコマンドラインに表示する処理)"""
            # 3000以上ならdout0をONにする。
            """(明るさ3000以上ならdout0をON、3000未満ならOFFにする処理)"""
        else:
            print("データ取得に失敗しました")
        # 0.5秒停止処理を入れる。
        time.sleep(0.5)
    ### ここまで  ###


if __name__ == '__main__':
    main()
