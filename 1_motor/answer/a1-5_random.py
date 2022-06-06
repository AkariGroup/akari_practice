#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q1-5. 3秒に1回パン、チルトで-0.5rad~0.5radのランダムな角度を２つ作り、その方向を向くコードを書きましょう。
ヒント1: Q4を参考に、while文の中の処理を書き直しましょう。
ヒント2: ランダムな関数を生成するには、random.uniform()という関数を使います。
            import random
            val = random.uniform(min,max)
         でmin以上max以下の乱数が生成され、valとして返ってきます。
         これを2回使って、パンとチルトの角度を作りましょう。
"""
### ここから問題  ###
from typing import Any
# モータ制御の際はakari_controllerのライブラリをインポートする
from akari_controller.akari_controller import AkariController
# sleep関数を使うためにtimeのライブラリをインポートする。
import time
# 乱数生成用のライブラリをインポートする。
import random


def main() -> None:
    """
    メイン関数
    """

    # AkariControllerのインスタンスを作成する。
    akari = AkariController()
    while(True):
        # -0.5~0.5のランダムな角度をpan,tiltそれぞれ生成
        pan_angle = random.uniform(-0.5, 0.5)
        tilt_angle = random.uniform(-0.5, 0.5)
        # 問題文に指定はないが、一応print。
        print("pan: " + str(pan_angle) + "tilt: " + str(tilt_angle))
        # 生成したランダムな方向を向く
        dict1: Any = {}
        dict1["joint_names"] = ["pan", "tilt"]
        dict1["values"] = [pan_angle, tilt_angle]
        akari.set_goal_position(dict1)
        # 3秒停止する
        time.sleep(3)


if __name__ == '__main__':
    main()

### ここまで  ###
