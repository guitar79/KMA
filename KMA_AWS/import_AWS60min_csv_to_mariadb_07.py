'''-*- coding: utf-8 -*-
 Auther guitar79@naver.com
 
 CREATE TABLE `KMA_AWS`.`60min_vc` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `ocode` INT(6) NOT NULL , 
    `otiem` INT(12) NOT NULL , 
    `oname` VARCHAR(20) NULL , 
    `preci_now` VARCHAR(20) NULL , 
    `preci_15` VARCHAR(20) NULL , 
    `preci_60` VARCHAR(20) NULL , 
    `preci_6H` VARCHAR(20) NULL , 
    `preci_12H` VARCHAR(20) NULL , 
    `preci_24H` VARCHAR(20) NULL , 
    `temperature` VARCHAR(20) NULL , 
    `wind_deg1` VARCHAR(20) NULL , 
    `wind_dir1` VARCHAR(20) NULL , 
    `wind_spd1` VARCHAR(20) NULL , 
    `wind_deg10` VARCHAR(20) NULL , 
    `wind_dir10` VARCHAR(20) NULL , 
    `wind_spd10` VARCHAR(20) NULL , 
    `RH` VARCHAR(20) NULL , 
    `Air_P` VARCHAR(20) NULL , 
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;
 
'''
#import numpy as np
import os
import pymysql
from datetime import datetime
#import time

start_time=str(datetime.now())

#mariaDB info
db_host = '10.114.0.121'
db_user = 'modis'
db_pass = 'rudrlrhkgkrrh'
db_name = 'KMA_AWS'
tb_name = '60min_vc'

#base directory
drbase = '/media/guitar79/8T/KMA_AWS/60min/'
#query_file='sql.txt'
#db connect
conn= pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,\
                      charset='utf8mb4', local_infile=1, cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
#delete all data in the table
print("TRUNCATE TABLE %s;" %(tb_name))
cur.execute("TRUNCATE TABLE %s;" %(tb_name))
conn.commit()

#log file
insert_log = open(drbase+'60min_insert_result.log', 'a')
error_log = open(drbase+'60min_insert_error.log', 'a')

#read the list of csv files
for year in range(2007,2017):
    #if not os.path.exists(drbase+str(year)+"/inserted"):
        #os.makedirs(drbase+str(year)+"/inserted")
        
    for i in sorted(os.listdir(drbase+str(year)+"/")):
        try :
            #read csv files
            if i[-4:] == '.csv':
                read_file = open(drbase+str(year)+"/"+i,'r')
                raw_lists = read_file.read()
                #print(raw_lists)
                raw_lists = raw_lists.split('\n')
                for j in range(1,(len(raw_lists)-1)):
                    #print(raw_lists[j])
                    row = raw_lists[j].split(',')
                    #print(row)
                    '''
                    print("INSERT INTO %s.%s\
                              (`id`, `ocode`, `otime`, `oname`, `preci_now`, \
                              `preci_15`, `preci_60`, `preci_6H`, `preci_12H`, `preci_24H`, \
                              `temperature`, `wind_deg1`, `wind_dir1`, `wind_spd1`, `wind_deg10`, \
                              `wind_dir10`, `wind_spd10`, `RH`, `Air_P`) \
                              VALUES ('NULL', %s, %s, 'NULL', '%s', \
                              '%s', '%s', '%s', '%s', '%s', \
                              '%s', '%s', '%s', '%s', '%s', \
                              '%s', '%s', '%s', '%s');"\
                              %(db_name, tb_name, \
                                row[0], i[-16:-4], row[3], \
                                row[4], row[5], row[6], row[7], row[8], \
                                row[9], row[10], row[11], row[12], row[13], \
                                row[14], row[15], row[16], row[17]))
                    '''
                    print(i,j)
                    
                    cur.execute("INSERT INTO %s.%s\
                          (`id`, `ocode`, `otime`, `oname`, `preci_now`, \
                          `preci_15`, `preci_60`, `preci_6H`, `preci_12H`, `preci_24H`, \
                          `temperature`, `wind_deg1`, `wind_dir1`, `wind_spd1`, `wind_deg10`, \
                          `wind_dir10`, `wind_spd10`, `RH`, `Air_P`) \
                          VALUES ('NULL', '%s', '%s', 'NULL', '%s', \
                          '%s', '%s', '%s', '%s', '%s', \
                          '%s', '%s', '%s', '%s', '%s', \
                          '%s', '%s', '%s', '%s');"\
                          %(db_name, tb_name, \
                            row[0], i[-16:-4], row[3], \
                            row[4], row[5], row[6], row[7], row[8], \
                            row[9], row[10], row[11], row[12], row[13], \
                            row[14], row[15], row[16], row[17]))
                    conn.commit()
                #os.rename(drbase+str(year)+"/"+i, drbase+str(year)+"/inserted/"+i)
                insert_log.write(drbase+str(year)+"/"+i+" is inserted to the %s - %s, %s\n"\
                         %(tb_name, datetime.now(), j))
            
        except :
            error_log.write(drbase+str(year)+"/"+i+" is error : %s - %s\n"\
                             %(tb_name, datetime.now()))
insert_log.close()
error_log.close()
cur.close()

end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)


'''
 aa=a.split(']')

aa
Out[16]: ['[,123456,,11,22,33,44,55,66', '']

aaa=aa[0].split('[')

aaa
Out[18]: ['', ',123456,,11,22,33,44,55,66']

aaaa=aaa[1].split(',')

aaaa
Out[20]: ['', '123456', '', '11', '22', '33', '44', '55', '66']
'''