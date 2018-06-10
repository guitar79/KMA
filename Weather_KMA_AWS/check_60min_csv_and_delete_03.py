'''-*- coding: utf-8 -*-
 Auther guitar79@naver.com

#import numpy as np
'''
import os
from datetime import datetime

#import time

start_time=str(datetime.now())

#base directory
drbase = '/media/guitar79/8T/KMA_AWS/60min/'

incompleted = open(drbase+'60min_incompleted.txt', 'a')
read_err = open(drbase+'60min_read_err.txt', 'a')
#read the list of csv files
for year in range(2007,2018):
    for i in sorted(os.listdir(drbase+str(year)+"/")):
        #read csv files
        if i[-4:] == '.csv':
            try:
                read_file = open(drbase+str(year)+"/"+i,'r')
                raw_lists = read_file.read()
                #print(raw_lists)
                raw_lists = raw_lists.split('\n')
                for j in range(1,(len(raw_lists)-1)):
                    row = raw_lists[j].split(',')
                    print(i,j)
                    if len(row) < 20:
                        print(drbase+str(year)+"/"+i+" is incompleted. rename the file name.")
                        os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".incompleted")
                        incompleted.write("%s"+i %(datetime.now()))
            except:
                print(drbase+str(year)+"/"+i+" is error. rename the file name.")
                os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".read_err")
                read_err.write("%s"+i %(datetime.now()))
incompleted.close()
read_err.close()
        
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)

