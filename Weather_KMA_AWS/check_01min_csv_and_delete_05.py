'''-*- coding: utf-8 -*-
 Auther guitar79@naver.com

#import numpy as np
'''
import os
from datetime import datetime

#import time

start_time=str(datetime.now())

#base directory
drbase = '/media/guitar79/8T/KMA_AWS/01min/'

error_file = open(drbase+'01min_error_file_list.log', 'a')
#read the list of csv files
for year in range(2010,2018):
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
                        os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".error")
                        error_file.write("%s %s.error file is created" %(datetime.now(),i))
            except UnicodeDecodeError as unicode_err:
                print(drbase+str(year)+"/"+i+" is UnicodeDecodeError. rename the file name.")
                os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".error")
                error_file.write("%s %s.error file is created" %(datetime.now(),i))
error_file.close()
        
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)

