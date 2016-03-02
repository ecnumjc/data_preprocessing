#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

import json
import os
from snownlp import SnowNLP

rootdir = "./raw_data"  # ָ�����������ļ���
filename = "./raw_sentences/raw_sents.txt"
fout = open(filename,'w')
error=0

for parent,dirnames,filenames in os.walk(rootdir): #�����������ֱ𷵻�1.��Ŀ¼ 2.�����ļ������֣�����·���� 3.�����ļ�����
        for filename in filenames:                     #����ļ���Ϣ
            sourceDir = os.path.join(parent,filename)  #����ļ�·����Ϣ
            print sourceDir
            fjson = file(sourceDir)
            sent = json.load(fjson)

            if not sent["article"]:
                error = error + 1
                continue
            articlestr = SnowNLP(sent["article"].decode('utf-8'))#�ĵ���Դ��utf-8���룬Ҳ�п�����gbk,Ҫ�ȼ��һ��
            for i in range(len(articlestr.sentences)):
                try:
                    print articlestr.sentences[i]
                    if len(articlestr.sentences[i])>4:
                        fout.write(articlestr.sentences[i]+'\n')
                except:
                    print 'error!\n'

            titlestr = SnowNLP(sent["title"].decode('utf-8'))#�ĵ���Դ��utf-8���룬Ҳ�п�����gbk,Ҫ�ȼ��һ��
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



    



