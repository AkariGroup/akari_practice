#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-3.テストヘッドのdout0のLEDを2秒ごとにONOFFするコードを書きましょう。
ヒント1: set_dout (int pin_id, bool val)という関数でdoutの出力を制御できます。
         pin_idは0、valにTrue,Falseを入れることでON,OFFできます。
ヒント2: 処理を停止するにはtime.sleep(sec)関数を使います。secに秒数を入れるとその時間だけ処理が停止します。
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
    while(True):
        # dout0をON
        m5.set_dout(0, True)
        # 2秒停止する
        time.sleep(2)
        # dout0をOFF
        m5.set_dout(0, False)
        # 2秒停止する
        time.sleep(2)
    ### ここまで  ###


if __name__ == '__main__':
    main()
