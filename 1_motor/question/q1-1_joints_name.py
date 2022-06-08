#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-1.ヘッドの２軸の関節名を取得して、コマンドラインに表示してみましょう。

ヒント: get_joint_names (void)という関数を使うと、list型で名前が返ってきます。
        このlistをprintしてみましょう。
"""

# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController


def main(args=None):
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()

    ### ここから問題  ###
    joints_name = """(関節角を取得する式)"""
    """(joints_nameをコマンドラインに出力する処理)"""
    ### ここまで  ###


if __name__ == '__main__':
    main()
