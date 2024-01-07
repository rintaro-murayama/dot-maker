import os, tkinter, tkinter.filedialog, tkinter.messagebox
from os.path import basename
import sys

def main(shrink_coef):
    # print("shrink_coef is: " + str(shrink_coef))

    typ = [("","*.png")]
    dir = os.path.abspath(os.path.dirname(__file__))

    files = tkinter.filedialog.askopenfilenames(filetypes=typ, initialdir=dir)

    out_dir = "./out/"

    # 各ファイル毎にドット化を実行
    # フィルタ部
    for f in files:

        # ドットの荒さ係数(縮小倍率を定義)
        shrink_rate = (1 / shrink_coef) * 100
        expand_rate = shrink_coef * 100

        # 新ファイル名の策定
        f_splt = basename(f).split(".")
        out_name = out_dir + f_splt[0] + "_" + str(shrink_coef) + "." + f_splt[1]

        # strip処理のために、一度コピーを作成しておく
        cp_cmd = "cp {0} {1}".format(f, out_dir + basename(f))
        # print(cp_cmd)
        os.system(cp_cmd)
        # 名前を変更
        mv_cmd = "mv {0} {1}".format(out_dir + basename(f), out_name)
        os.system(mv_cmd)

        #pngのstrip処理
        strip_cmd = "convert {0} -strip {1}".format(out_name, out_name)
        # print(strip_cmd)
        os.system(strip_cmd)

        shrink_cmd = "convert -filter box -resize {0}%% {1} {2}".format(shrink_rate, out_name, out_name)
        os.system(shrink_cmd)

        expand_cmd = "convert -filter box -resize {0}%% {1} {2}".format(expand_rate, out_name, out_name)
        os.system(expand_cmd)

if __name__ == "__main__":
    args = sys.argv

    if 2 == len(args):
        if args[1].isdecimal():
            main(int(args[1]))
        else:
            main(10)
    else:
        main(10)




