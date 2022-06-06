#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-3. AKARIが動いたあとの、現在位置を取得してコマンドラインに表示しましょう。
ヒント1: get_present_position (list(str) joint_name_list)という関数を使います。
         Q2で使っているので、参考にしてください。
"""

# sleep関数を使うためにtimeのライブラリをインポートする。
import time
# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController


def main() -> None:
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()
    # 両方のモータ速度を5rad/sに変更する。
    akari.set_profile_velocity({"joint_names": ["pan", "tilt"],
                                "values": [5, 5]})
    # AKARIを目標位置に移動する。
    akari.set_goal_position({"joint_names": ["pan", "tilt"],
                             "values": [-0.5, 0.2]})
    # 1秒待つ
    time.sleep(1)
    ### ここから問題  ###
    position = akari.get_present_position(["pan", "tilt"])
    print(position)
    ### ここまで  ###


if __name__ == '__main__':
    main()
