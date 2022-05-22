#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-4. 下40°を向く→3秒待つ→上20°を向く→３秒待つ→下40°を向く…という動作を繰り返すコードを書きましょう。
ヒント1: while(True):の中に書かれたコードはループします。この中に１周期分の処理を書きましょう。
ヒント2: 処理を停止するにはtime.sleep(sec)関数を使います。secに秒数を入れるとその時間だけ処理が停止します。
"""

# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController
# sleep関数を使うためにtimeのライブラリをインポートする。
import time

def main(args=None):
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()
    # 両方のモータ速度を5rad/sに変更する。
    akari.set_profile_velocity({"joint_names": ["pan", "tilt"],
                            "values": [5, 5]})
    ### ここから問題  ###
    while(True):
        # 下40°を向く
        dict1 = {}
        dict1["joint_names"] = ["tilt"]
        dict1["values"] = [-0.698]
        akari.set_goal_position(dict1)
        # 3秒停止する
        time.sleep(3)
        # 上20°を向く
        dict1 = {}
        dict1["joint_names"] = ["tilt"]
        dict1["values"] = [0.349]
        akari.set_goal_position(dict1)
        # 3秒停止する
        time.sleep(3)
    ### ここまで  ###


if __name__ == '__main__':
    main()
