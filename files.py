# coding=UTF-8
import os
import re


def eliminatename(path , old):
  name_list = os.listdir(path)
  for name in name_list:
    os.chdir(path)
    file_name = os.path.abspath(name)
    src =file_name
    print(name)
    dst = file_name.replace(old ,'')
    print(dst)
    try:
      os.rename(src,dst)
    except:
      continue
path = '/Users/tal/Downloads/5500考研单词新东方'
eliminatename(path,'_')
