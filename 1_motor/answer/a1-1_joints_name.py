#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-1.ヘッドの２軸の関節名を取得して、コマンドラインに表示してみましょう。

ヒント: get_joint_names (void)という関数を使うと、list型で名前が返ってきます。
        このlistをprintしてみましょう。
"""

# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController


def main() -> None:
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()

    ### ここから問題  ###
    joints_name = akari.get_joint_names()
    print(joints_name)
    ### ここまで  ###


if __name__ == '__main__':
    main()
