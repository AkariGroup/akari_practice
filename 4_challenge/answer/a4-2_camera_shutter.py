#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q4-2.キーボードで特定のキーを入力した際に写真を撮影して保存するアプリを作りましょう。
このアプリの実行には、別ターミナルでakari_main/src/depthai_uvc/depthai_uvc_rgb.pyを起動しておく必要があります。
ヒント1: take_photo()という関数が用意してあるのでこれを使いましょう。
         この関数はファイル名を引数として渡すと、その名前の写真を保存してくれます。
         1枚目は001,2枚目は002...となるようにファイル名を渡してあげましょう。
ヒント2: キーボード入力を取得するにはinput()という関数を使います。
            val = input()
         というようにすると、入力した文字がvalとして得られます。
         文字入力後エンターを押すとvalに渡されます。
ヒント3: zfill()を使うと文字列をゼロ埋めします。
         zfillの引数はゼロ埋めする桁数です。下記のように使います。
            num = 1
            num_after = str(num).zfill(3)
            print(num_after)
            # '001'とプリントされる
"""

# M5と通信する際はm5serial_server_pyのライブラリをインポートする。
from m5serial_server_py.m5serial_server_py import M5SerialServer
# openCVのライブラリをインポート
import cv2
# osのインポート
import os

# depthaiの仮想カメラのID20番を指定
DEVICE_ID = 20


def take_photo(name: str) -> bool:
    """
    写真を撮って保存する関数。
    保存先はoutputディレクトリ以下。
    Args:
        name (str): 保存する画像ファイル名
    Returns:
        Bool: True なら成功, False なら失敗.

    """
    # カメラ画像の取得
    cap = cv2.VideoCapture(DEVICE_ID)
    ret, frame = cap.read()
    cap.release()
    # 取得に失敗した場合、Falseを返す
    if not ret:
        print('画像取得に失敗しました。')
        return False
    else:
        file_name = 'output/' + name + '.jpg'
        cv2.imwrite(file_name, frame)
        print('ファイル名' + file_name + 'を保存しました。')
        return True


def main() -> None:
    """
    メイン関数
    """
    # 'output'というディレクトリを作成
    os.makedirs('output', exist_ok=True)
    ### ここから問題  ###
    # ファイル名の通し番号
    num = 0
    # Ctrl + Cで終了するまでループし続ける
    while(True):
        print('cを入力後エンターを押すと写真を撮影します。')
        # キーボード入力待ち
        val = input()
        # cが入力されていた場合写真を撮る。
        if(val == 'c'):
            # numを3桁に0埋めしてtake_photo()に渡す。
            take_photo(str(num).zfill(3))
            # 写真を撮ったらnumを+1する。
            num += 1
    ### ここまで  ###


if __name__ == '__main__':
    main()
