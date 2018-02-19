'''
-*- coding: utf-8 -*-
 Auther guitar79@naver.com
 
'''
#import numpy as np
import os
import pymysql
from datetime import datetime
#import time

start_time=str(datetime.now())

#mariaDB info
db_host = '10.114.0.126'
db_user = 'modis'
db_pass = 'rudrlrhkgkrrh'
db_name = 'KMA_AWS'
tb_name = '01min'

#base directory
drbase = '/media/guitar79/8T/KMA_AWS/01min/'
#query_file='sql.txt'
#db connect
conn= pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,\
                      charset='utf8mb4', local_infile=1, cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

cur.execute("SET SQL_MODE = \"NO_AUTO_VALUE_ON_ZERO\";\
            SET time_zone = \"+00:00\";")

cur.execute("DROP TABLE IF EXISTS `%s`;" %(tb_name))

cur.execute("CREATE TABLE IF NOT EXISTS `Obs_info` (\
            `Ocode` int(6) NOT NULL,\
            `Oname` varchar(12) DEFAULT NULL,\
            `Region` varchar(20) DEFAULT NULL,\
            `Address` varchar(500) DEFAULT NULL,\
            `Lat` float DEFAULT NULL,\
            `Lon` float DEFAULT NULL,\
            `Alt` float DEFAULT NULL,\
            `Remarks` char(255) DEFAULT NULL,\
            PRIMARY KEY (`Ocode`))\
            ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")

cur.execute("CREATE TABLE IF NOT EXISTS `%s` (\
            `Ocode` int(6) NOT NULL,\
            `Otime` DATETIME NOT NULL,\
            `preci_now` int(1) DEFAULT NULL,\
            `preci_15` float DEFAULT NULL,\
            `preci_60` float DEFAULT NULL,\
            `preci_6H` float DEFAULT NULL,\
            `preci_12H` float DEFAULT NULL,\
            `preci_24H` float DEFAULT NULL,\
            `Temperature` float DEFAULT NULL,\
            `wind_deg1` float DEFAULT NULL,\
            `wind_dir1` varchar(4) DEFAULT NULL,\
            `wind_spd1` float DEFAULT NULL,\
            `wind_deg10` float DEFAULT NULL,\
            `wind_dir10` varchar(4) DEFAULT NULL,\
            `wind_spd10` float DEFAULT NULL,\
            `RH` float DEFAULT NULL,\
            `Air_P` float DEFAULT NULL,\
            `id` int(11) NOT NULL\
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"\
             %(tb_name))

cur.execute("ALTER TABLE `%s` \
            ADD PRIMARY KEY (`id`);" %(tb_name))

cur.execute("ALTER TABLE `%s`\
            MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;"  %(tb_name))

#delete all data in the table
print("TRUNCATE TABLE %s;" %(tb_name))
cur.execute("TRUNCATE TABLE %s;" %(tb_name))
conn.commit()


#log file
insert_log = open(drbase+'10min_import_result.log', 'a')
error_log = open(drbase+'10min_import_error.log', 'a')


#read the list of csv files
for year in range(2012,2017):
    #if not os.path.exists(drbase+str(year)+"/inserted"):
        #os.makedirs(drbase+str(year)+"/inserted")

    for i in sorted(os.listdir(drbase+str(year)+"/")):
        for Mo in (["%.2d" % Moi for Moi in range(1,13)]):
            #AWS-01min_201501010016.csv
             #define day numbers of each month
            if year%4==0 : D=[0,31,29,31,30,31,30,31,31,30,31,30,31]
            else : D=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            #for Da in range(1,D[Mo]+1):
            for Da in (["%.2d" % Dai for Dai in range(1,(D[int(Mo)]+1))]):

                print(i)
                for Hr in (["%.2d" % Hri for Hri in range(0,24)]):
                    output = ''

                    if i[-4:] == '.csv' and i[14:16] == Mo and i[16:18] == Da and i[18:20] == Hr:
                        #read csv files
                        read_file = open(drbase+str(year)+"/"+i,'r')
                        raw_lists = read_file.read()
                        #print(raw_lists)
                        raw_lists = raw_lists.split('\n')
                        for j in range(1,(len(raw_lists)-1)):
                            #print(raw_lists[j])
                            row = raw_lists[j].split(',')
 
                            for k in range(len(row)):
                                if row[3]=='○' : row[3]=-1
                                if row[3]=='●' : row[3]=-2
                                if row[3]=='-' : row[3]=-3
                                if row[11]=='\xa0' : row[11]='NULL'
                                if row[14]=='\xa0' : row[14]='NULL'
                                if row[k]=='\xa0' : row[k]=-999
                                if len(str(row[k]))==0 : row[k]=-999
                                if row[k]=='.' : row[k]=-998
                                if row[k]=='-' : row[k]=-997
                                
                            #print(i,j)  
                                              

                            output += "INSERT INTO %s.%s\
                                      (`Ocode`, `Otime`, `preci_now`, `preci_15`, `preci_60`, \
                                      `preci_6H`, `preci_12H`, `preci_24H`, `Temperature`, \
                                      `wind_deg1`, `wind_dir1`, `wind_spd1`,\
                                      `wind_deg10`, `wind_dir10`, `wind_spd10`, `RH`, `Air_P`, `id`) \
                                      VALUES (%s, '%s-%s-%s %s:%s:00',\
                                      '%s', '%s', '%s', \
                                      '%s', '%s', '%s', '%s', \
                                      '%s', '%s', '%s',\
                                      '%s', '%s', '%s', '%s', '%s', NULL);\n"\
                                      %(db_name, tb_name, \
                                        row[0], i[-16:-12], i[-12:-10], i[-10:-8], i[-8:-6], i[-6:-4],\
                                        row[3], row[4], row[5],\
                                        row[6], row[7], row[8], row[9], \
                                        row[10], row[11], row[12], \
                                        row[13], row[14], row[15], row[16], row[17])                    
                            #print(row)
                            '''
                            print("INSERT INTO %s.%s\
                                      (`Ocode`, `Otime`, `preci_now`, `preci_15`, `preci_60`, \
                                      `preci_6H`, `preci_12H`, `preci_24H`, `Temperature`, \
                                      `wind_deg1`, `wind_dir1`, `wind_spd1`,\
                                      `wind_deg10`, `wind_dir10`, `wind_spd10`, `RH`, `Air_P`, `id`) \
                                      VALUES ('%s', '%s-%s-%s %s:%s:00',\
                                      '%s', '%s', '%s', \
                                      '%s', '%s', '%s', '%s', \
                                      '%s', '%s', '%s',\
                                      '%s', '%s', '%s', '%s', '%s', NULL);\n"\
                                      %(db_name, tb_name, \
                                        row[0], i[-16:-12], i[-12:-10], i[-10:-8], i[-8:-6], i[-6:-4],\
                                        row[3], row[4], row[5],\
                                        row[6], row[7], row[8], row[9], \
                                        row[10], row[11], row[12], \
                                        row[13], row[14], row[15], row[16], row[17]))
                            cur.execute("INSERT INTO %s.%s\
                                      (`Ocode`, `Otime`, `preci_now`, `preci_15`, `preci_60`, \
                                      `preci_6H`, `preci_12H`, `preci_24H`, `Temperature`, \
                                      `wind_deg1`, `wind_dir1`, `wind_spd1`,\
                                      `wind_deg10`, `wind_dir10`, `wind_spd10`, `RH`, `Air_P`, `id`) \
                                      VALUES (%s, '%s-%s-%s %s:%s:00',\
                                      %s, '%s', '%s', \
                                      '%s', '%s', '%s', '%s', \
                                      '%s', '%s', '%s',\
                                      '%s', '%s', '%s', '%s', '%s', NULL);"\
                                      %(db_name, tb_name, \
                                        row[0], i[-16:-12], i[-12:-10], i[-10:-8], i[-8:-6], i[-6:-4],\
                                        row[3], row[4], row[5],\
                                        row[6], row[7], row[8], row[9], \
                                        row[10], row[11], row[12], \
                                        row[13], row[14], row[15], row[16], row[17]))
                            conn.commit()
                            '''
                        cur.execute(output)
                        conn.commit()
                        insert_log.write(drbase+str(year)+"/"+i+" is inserted to the %s - %s, %s\n"\
                                 %(tb_name, datetime.now(), j))
                    
                        with open(drbase+'sql/'+str(year)+Mo+Da+Hr+'.sql', 'w') as f:
                            f.write(output)
                
            
    print("CHECK TABLE %s.%s;" %(db_name, tb_name))
    cur.execute("CHECK TABLE %s.%s;" %(db_name, tb_name))
    conn.commit()
    print("ALTER TABLE %s.%s ENGINE = InnoDB;" %(db_name, tb_name))
    cur.execute("ALTER TABLE %s.%s ENGINE = InnoDB;" %(db_name, tb_name))
    conn.commit()
    print("OPTIMIZE TABLE %s.%s;" %(db_name, tb_name))
    cur.execute("OPTIMIZE TABLE %s.%s;" %(db_name, tb_name))
    conn.commit()
    '''
    print("FLUSH TABLE %s.%s;" %(db_name, tb_name))
    cur.execute("FLUSH TABLE %s.%s;" %(db_name, tb_name))
    conn.commit()
        '''
    
insert_log.close()
error_log.close()

cur.close()

end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)
