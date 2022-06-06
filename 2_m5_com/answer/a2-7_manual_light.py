#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q2-7.ボタンAを押すとテストヘッドのpwmout0のLEDの明るさを10上げて、
     ボタンBを押すと10下げる手動ライトを作りましょう。
     pwmout0にセットする値は0-250の範囲内に収まるようにしてください。
ヒント1: ボタン操作はQ2-1、pwmoutはQ2-4を参考にしましょう。
ヒント2: LEDの明るさ値の変数を初期値を0で作成して,
         ボタンが押されていたら明るさ値を変化→pwmout0にセットする、というループ処理を書きましょう。
ヒント3: ループの最後に停止処理を入れないと処理が間に合いませんが、停止処理が長すぎると使い勝手が悪いです。
         停止時間を調整して、安定かつ使いやすいアプリを目指してみましょう。
"""

### ここから問題  ###

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

    # pwmout0の明るさの変数を初期値0で作成。
    pwmout0_val = 0
    # Ctrl + Cで終了するまでループし続ける。
    while(True):
        m5_data = m5.get()
        # ボタンAが押されていて、かつpwmout0_valが240以下の場合、pwmout0を+10。
        if(m5_data['button_a'] and pwmout0_val <= 240):
            pwmout0_val += 10
        # ボタンBが押されていて、かつpwmout0_valが10以上の場合、pwmout0を-10。
        if(m5_data['button_b'] and pwmout0_val >= 10):
            pwmout0_val -= 10
        # pwmout0の値をコマンドラインに出力。
        print("今の明るさは" + str(pwmout0_val) + "です。")
        # pwmout0を指令
        m5.set_pwmout(0, pwmout0_val)
        # 0.1秒停止処理を入れる。ここは各自調整！
        time.sleep(0.1)


if __name__ == '__main__':
    main()

### ここまで  ###
