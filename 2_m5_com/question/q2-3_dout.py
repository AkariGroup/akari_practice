#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-3.テストヘッドのdout0のLEDを2秒ごとにONOFFするコードを書きましょう。
ヒント1: set_dout (int pin_id, bool val)という関数でdoutの出力を制御できます。
         pin_idは0、valにTrue,Falseを入れることでON,OFFできます。
ヒント2: while(True):の中に書かれたコードはループします。この中に１周期分の処理を書きましょう。
ヒント3: 処理を停止するにはtime.sleep(sec)関数を使います。secに秒数を入れるとその時間だけ処理が停止します。
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
        """ (処理を書く)"""
    ### ここまで  ###


if __name__ == '__main__':
    main()
