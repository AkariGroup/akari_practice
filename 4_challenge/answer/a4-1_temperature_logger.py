#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q4-1.現在時刻と環境温度を10秒ごとに取得して、csvファイルに追記し続けるコードを書きましょう。
ヒント1: 時刻の取得はQ3-5,温度の取得はQ2-5を参考にしましょう。
ヒント2: csvへの書き込みはcsv.writerを使います。
         最初の行にインデックスを書き込んで、以降取得した値を追記していきましょう。
         下記がlog.csvというファイルを作って'時刻','温度'という行を書き込むサンプルです。
         ファイル作成先はpythonを実行した場所となります。
         openの第二引数を'w'にすると新規作成、'a'にすると既存のファイルに追記します。
         import csv
         with open('log.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['時刻','温度'])
ヒント3: logを取る間隔を変える、logの内容を増やす、logのファイル名や保存場所を変えるなど
         色々試してみましょう！
"""

### ここから問題  ###
# M5と通信する際はam5serial_server_pyのライブラリをインポートする
from m5serial_server_py.m5serial_server_py import M5SerialServer
# sleep関数を使うためにtimeのライブラリをインポートする。
import time
# 時刻取得に必要なライブラリをインポートする。
import datetime
# csvの読み書き用ライブラリをインポートする。
import csv

# logファイルの名前を定義
FILE_NAME = 'log.csv'


def main() -> None:
    """
    メイン関数
    """
    # M5SerialServerのインスタンスを作成する。
    m5 = M5SerialServer()
    # log.csvを作成して、インデックス行を書き込む
    with open(FILE_NAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['時刻', '温度'])
    # Ctrl + Cで終了するまでループし続ける
    while(True):
        m5_data = m5.get()
        # 温度を取得
        cur_temperature = m5_data['temperature']
        # 時刻を取得
        dt_now = datetime.datetime.now()
        # 時:分:秒の形に変換
        cur_time = dt_now.strftime('%H:%M:%S')
        print('[' + cur_time + '] temperature: ' +
              str(cur_temperature) + ' [deg]')
        # logファイルを開いて取得した時刻、温度を最終行に追記
        with open(FILE_NAME, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([cur_time, cur_temperature])
        # 10秒停止処理を入れる。
        time.sleep(10)


if __name__ == '__main__':
    main()
### ここまで  ###
