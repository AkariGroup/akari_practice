#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-2. Q1-1で取得した関節名を使って、ヘッドを左に45°向かせてみましょう。
ヒント1: set_goal_position (dict)という関数を使います。
         引数にはdict1を使いましょう。dict1には動かしたい関節名のリストと、目標角度のリストを入れます。
ヒント2: 関節角度はradで入れます。45°をラジアンに変換した値を入れましょう。
"""

# sleep関数を使うためにtimeのライブラリをインポートする。
import time
from typing import Any
# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController


def main() -> None:
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()

    ### ここから問題  ###
    dict1: Any = {}
    dict1["joint_names"] = ["pan"]
    dict1["values"] = [0.785]
    akari.set_goal_position(dict1)
    ### ここまで  ###
    # 1秒待つ
    time.sleep(1)
    # 現在位置を取得してコマンドラインに表示
    position = akari.get_present_position(["pan", "tilt"])
    print("現在位置は" + str(position) + "です。")


if __name__ == '__main__':
    main()
