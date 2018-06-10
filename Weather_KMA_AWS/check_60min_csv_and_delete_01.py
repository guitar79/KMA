'''-*- coding: utf-8 -*-
 Auther guitar79@naver.com
'''
#import numpy as np
import os
from datetime import datetime

#import time

start_time=str(datetime.now())

#base directory
drbase = '/media/guitar79/8T/KMA_AWS/60min/'

incompleted = []
#read the list of csv files
for year in range(2007,2018):
    for i in sorted(os.listdir(drbase+str(year)+"/")):
        #read csv files
        if i[-4:] == '.csv':
            read_file = open(drbase+str(year)+"/"+i,'r')
            raw_lists = read_file.read()
            #print(raw_lists)
            raw_lists = raw_lists.split('\n')
            for j in range(1,(len(raw_lists)-1)):
                row = raw_lists[j].split(',')
                if len(row) < 20:
                    print(drbase+str(year)+"/"+i+" is incompleted. rename the file name.")
                    incompleted.append(i)
                    os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/"+i+".incompleted")
                else:
                    print(i,j)
    
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)
#print(finish_rows)

'''
            try:
                print(i, j)
                cur.execute("INSERT INTO %s.%s\
                      (`id`, `ocode`, `oname`, `otime`, `SO2`, `CO`, `O3`, `NO2`, `PM10`, `PM2.5`) \
                      VALUES ('NULL', %s, %s, %s, %s, %s, %s, %s, %s, %s);"\
                      %(db_name, tb_name, row[1], row[2], row[3], row[4],\
                        row[5], row[6], row[7], row[8], row[9]))
                cur.close()
                conn.commit()
                finish_rows = finish_rows + len(raw_lists)
            except MySQLdb.Error, e:
                print "Transaction failed, rolling back. Error was:"
                print e.args
                try:  # empty exception handler in case rollback fails
                    conn.rollback ()
                except:
                    pass

'''
