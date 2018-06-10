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

incompleted_files = []
read_err_files = []
#read the list of csv files
for year in range(2007,2008):
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
                        incompleted_files.append("%s"+i %(datetime.now()))
                        os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".incompleted")
            except:
                print(drbase+str(year)+"/"+i+" is error. rename the file name.")
                read_err_files.append("%s"+i %(datetime.now()))
                os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".read_err")
                
incompleted = open(drbase+'60min_incompleted.txt', 'a')
for incompleted_file in incompleted_files:
    incompleted.write("%s\n" % incompleted_file)
read_err = open(drbase+'60min_read_err.txt', 'a')
for read_err_file in read_err_files:
    incompleted.write("%s\n" % read_err_file)
        
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)
#print(finish_rows)
