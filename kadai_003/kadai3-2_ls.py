# -*- coding: utf-8 -mport os

import sys
import stat
import pwd
import grp
import datetime
import os

def ls(path, options=''):
    file_list = []
    files = os.listdir(path)

# -aオプションの動作を規定する部分
    if 'a' in options:
        file_list = files
    else:
        for file in files:
            if file[0] == '.':
                pass
            else:
                file_list.append(file)

    for target in file_list:
        stat_status = os.lstat(path + "/" + target)
        result = []
        result.append(target)
        file_info_list = []
        stat_mode = stat_status[stat.ST_MODE]

# -lオプションを規定する部分
        if 'l' in options:
# 更新日時の表示を規定する部分
            last_modified = stat_status.st_mtime
            dt = datetime.datetime.fromtimestamp(last_modified)
            tmp_time = dt.strftime("%H:%M")
            tmp_manth = dt.strftime("%b")
            tmp_date = dt.strftime("%d")
            result.insert(0, tmp_time)
            result.insert(0, tmp_date)
            result.insert(0, tmp_manth)

# バイト数の表示を規定する部分
            result.insert(0, os.path.getsize(path + "/" + target))

# 対象の所有者表示を規定する部分
            uid = pwd.getpwuid(stat_status[4]).pw_name
            gid = grp.getgrgid(stat_status[5]).gr_name
            result.insert(0, gid)
            result.insert(0, uid)

# リンク数を規定する部分
            link_cnt = stat_status[3]
            result.insert(0, link_cnt)


# 対象の種類(ファイル/ディレクトリ/リンク)を識別する部分
            tmp_data = ''
            if stat.S_ISLNK(stat_mode):
                tmp_data = 'l'
            elif stat.S_ISDIR(stat_mode):
                tmp_data = 'd'
            elif stat.S_ISREG(stat_mode):
                tmp_data = '-'

# 実行権限について規定する部分
            for level in "OTH", "GRP", "USR":
                for param in "X", "W", "R":
                    if stat_mode & getattr(stat, "S_I"+param+level):
                        tmp_data = tmp_data + param.lower()
                    else:
                        tmp_data = tmp_data + '-'

            result.insert(0, tmp_data)


# inode出力を規定する部分
        if 'i' in options:
            inode = stat_status[1]
            result.insert(0, inode)

        str_result = map(str, result)
        print(" ".join(str_result))


def arg_parse(args, argc):
# lsの対象をカレントディレクトリに指定する
    target_dir = os.getcwd()

    op_list = []

    if argc == 0:
# カレントディレクトリの構成を出力する
        ls(target_dir)
    elif argc == 1:
# 引数が1つでハイフンから始まる場合の動作を規定する
        check_hyphen = args[0]
        if check_hyphen[0] == '-':
            for op in check_hyphen[1:]:
                op_list.append(op)

            ls(target_dir, op_list)
# 引数が1つでハイフンから始まらない場合の動作を規定する
        else:
            target_dir = args[0]
            ls(target_dir)
# 引数が2つある場合の動作を規定する
    else:
        check_hyphen = args[0]
        for op in check_hyphen[1:]:
            op_list.append(op)

        target_dir = args[1]
        ls(target_dir, op_list)

curt_dir = os.getcwd() # カレントディレクトリの情報を取得する
argvs = sys.argv       # コマンドライン引数を格納したリストの情報を取得する
del argvs[0]
argc = len(argvs)      # 引数の個数を取得する

arg_parse(argvs, argc)


# お題： Unixのlsコマンドの基本機能相当のls.pyを書いてください。
# 要件1：コマンドライン引数で対象パス名を指定できるようにしてください。
# 要件2:対象パス名が省略されたときはカレントのディレクトリを対象パス名にしてください。
# 要件3:-l，-a，-i程度のオプションは実装してください。
# 要件4:os.system()でのlsコマンドの起動以外の実装をしてください。



