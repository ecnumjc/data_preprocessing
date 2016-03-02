#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

import json
import os
from snownlp import SnowNLP

rootdir = "./raw_data"  # 指明被遍历的文件夹
filename = "./raw_sentences/raw_sents.txt"
fout = open(filename,'w')
error=0

for parent,dirnames,filenames in os.walk(rootdir): #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:                     #输出文件信息
            sourceDir = os.path.join(parent,filename)  #输出文件路径信息
            print sourceDir
            fjson = file(sourceDir)
            sent = json.load(fjson)

            if not sent["article"]:
                error = error + 1
                continue
            articlestr = SnowNLP(sent["article"].decode('utf-8'))#文档来源是utf-8编码，也有可能是gbk,要先检查一下
            for i in range(len(articlestr.sentences)):
                try:
                    print articlestr.sentences[i]
                    if len(articlestr.sentences[i])>4:
                        fout.write(articlestr.sentences[i]+'\n')
                except:
                    print 'error!\n'

            titlestr = SnowNLP(sent["title"].decode('utf-8'))#文档来源是utf-8编码，也有可能是gbk,要先检查一下
            for j in range(len(titlestr.sentences)):
                try:
                    print titlestr.sentences[j]
                    if len(titlestr.sentences[j])>4:
                        fout.write(titlestr.sentences[j]+'\n')
                except:
                    print 'error!\n'
                    error = error + 1

            fjson.close()

print error
fout.close()



    



