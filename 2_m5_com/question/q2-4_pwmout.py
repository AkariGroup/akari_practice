#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-4.テストヘッドのpwmout0のLEDを0-250まで10刻みで明るくしていく処理を書きましょう。
   明るさを変化させるごとに0.5秒停止する処理をいれてください。
   250になったら明るさを0にしてから終了してください。
ヒント1: set_pwmout (int pin_id, int val)という関数でpwmoutの出力を制御できます。
         pin_idは0、valに値を入れることでON,OFFできます。
ヒント2: for文を使って0-250まで10ずつ値を変化させるループ処理を書いてみましょう。
         書き方はいくつかありますが、
            for i in range(start, end, step):
         を使うのがいいでしょう。これは数値iがstartからendまで、stepずつ増加するループ処理です。
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
    """(処理を書く)"""
    ### ここまで  ###


if __name__ == '__main__':
    main()
