# import glob
# import os
 
# # 拡張子.txtのファイルを取得する
# path = './cell-count-data/train/*.txt'
# i = 1
 
# # txtファイルを取得する
# flist = glob.glob(path)
# print('変更前')
# print(flist)
 
# # ファイル名を一括で変更する
# for file in flist:
#   os.rename(file, './cell-count-data/train/cell' + str(i) + '.txt')
#   i+=1
 
# list = glob.glob(path)
# print('変更後')
# print(list)