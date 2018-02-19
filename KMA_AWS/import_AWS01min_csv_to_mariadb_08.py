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
db_host = '10.114.0.121'
db_user = 'modis'
db_pass = 'rudrlrhkgkrrh'
db_name = 'KMA_AWS'
tb_name = '01min_vc'

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

cur.execute("CREATE TABLE IF NOT EXISTS `%s` (\
            `Ocode` varchar(6) NOT NULL,\
            `Oname` varchar(20) DEFAULT NULL,\
            `Altitude` varchar(20) DEFAULT NULL,\
            `preci_now` varchar(20) DEFAULT NULL,\
            `preci_15` varchar(20) DEFAULT NULL,\
            `preci_60` varchar(20) DEFAULT NULL,\
            `preci_6H` varchar(20) DEFAULT NULL,\
            `preci_12H` varchar(20) DEFAULT NULL,\
            `preci_24H` varchar(20) DEFAULT NULL,\
            `Temperature` varchar(20) DEFAULT NULL,\
            `wind_deg1` varchar(20) DEFAULT NULL,\
            `wind_dir1` varchar(20) DEFAULT NULL,\
            `wind_spd1` varchar(20) DEFAULT NULL,\
            `wind_deg10` varchar(20) DEFAULT NULL,\
            `wind_dir10` varchar(20) DEFAULT NULL,\
            `wind_spd10` varchar(20) DEFAULT NULL,\
            `RH` varchar(20) DEFAULT NULL,\
            `Air_P` varchar(20) DEFAULT NULL,\
            `Address` varchar(100) DEFAULT NULL,\
            `otime` varchar(12) NOT NULL,\
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
insert_log = open(drbase+'01min_import_result.log', 'a')
error_log = open(drbase+'01min_import_error.log', 'a')

for year in range(2007,2017):
    
    for i in sorted(os.listdir(drbase+str(year)+"/")):
        try :
            #read csv files
            if i[-4:] == '.csv':
                #make data frame from reading csv files (like table)
                print(i)
                print("LOAD DATA LOCAL \
                      INFILE '%s%s/%s' \
                      INTO TABLE %s.%s \
                      FIELDS TERMINATED BY ',' \
                      ENCLOSED BY '\"' \
                      LINES TERMINATED BY '\\n'\
                      IGNORE 1 LINES\
                      set otime= '%s';"\
                      %(drbase,str(year),i,db_name,tb_name, i[10:22]))
        
                cur.execute("LOAD DATA LOCAL \
                            INFILE '%s%s/%s' \
                            INTO TABLE %s.%s \
                            FIELDS TERMINATED BY ',' \
                            ENCLOSED BY '\"' \
                            LINES TERMINATED BY '\\n'\
                            IGNORE 1 LINES\
                            set otime= '%s';"\
                            %(drbase,str(year),i,db_name,tb_name, i[10:22]))
                conn.commit()
                insert_log.write(drbase+str(year)+"/"+i+" is inserted to the %s - %s\n"\
                                 %(tb_name, datetime.now()))
        except :
            error_log.write(drbase+str(year)+"/"+i+" is error : %s - %s\n"\
                             %(tb_name, datetime.now()))
insert_log.close()
error_log.close()
cur.close()

end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)


 
#place and date(1day)
'''

-- phpMyAdmin SQL Dump
-- version 4.4.7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 14, 2017 at 12:31 PM
-- Server version: 10.1.25-MariaDB-
-- PHP Version: 7.0.22-0ubuntu0.17.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `KMA_AWS`
--

-- --------------------------------------------------------

--
-- Table structure for table `60min_vc_test`
--

CREATE TABLE IF NOT EXISTS `60min_vc_test` (
  `id` int(11) NOT NULL,
  `ocode` int(6) NOT NULL,
  `otime` int(8) NOT NULL,
  `oname` varchar(20) DEFAULT NULL,
  `preci_now` varchar(20) DEFAULT NULL,
  `preci_15` varchar(20) DEFAULT NULL,
  `preci_60` varchar(20) DEFAULT NULL,
  `preci_6H` varchar(20) DEFAULT NULL,
  `preci_12H` varchar(20) DEFAULT NULL,
  `preci_24H` varchar(20) DEFAULT NULL,
  `temperature` varchar(20) DEFAULT NULL,
  `wind_dir1` varchar(20) DEFAULT NULL,
  `wind_spd1` varchar(20) DEFAULT NULL,
  `wind_dir10` varchar(20) DEFAULT NULL,
  `wind_spd10` varchar(20) DEFAULT NULL,
  `RH` varchar(20) DEFAULT NULL,
  `Air_P` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `60min_vc_test`
--
ALTER TABLE `60min_vc_test`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `60min_vc_test`
--
ALTER TABLE `60min_vc_test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;




-*- coding: utf-8 -*-
 Auther guitar79@naver.com


import os
import pymysql
from datetime import datetime

start_time=str(datetime.now())

#mariaDB info
db_host = '10.114.0.121'
db_user = 'modis'
db_pass = 'rudrlrhkgkrrh'
db_name = 'AirKorea_parks'
tb_name = 'hourly_vc'

#base directory
drbase = '/home/guitar79/AK/'
#query_file='sql.txt'
#db connect
conn= pymysql.connect(host=db_host, user=db_user, password=db_pass, db=db_name,\
                      charset='utf8mb4', local_infile=1, cursorclass=pymysql.cursors.DictCursor)

#all ocode read!!
cur = conn.cursor()
print("TRUNCATE TABLE %s;" %(tb_name))
cur.execute("TRUNCATE TABLE %s;" %(tb_name))

for i in sorted(os.listdir(drbase)):
    #read csv files
    if i[-4:] == '.csv':
        #make data frame from reading csv files (like table)
        print(i)
        print("LOAD DATA LOCAL \
              INFILE '%s%s' \
              INTO TABLE %s.%s \
              FIELDS TERMINATED BY ',' \
              ENCLOSED BY '\"' \
              LINES TERMINATED BY '\\n'\
              IGNORE 0 LINES;"\
              %(drbase,i,db_name,tb_name))

        cur.execute("LOAD DATA LOCAL \
                    INFILE '%s%s' \
                    INTO TABLE %s.%s \
                    FIELDS TERMINATED BY ',' \
                    ENCLOSED BY '\"' \
                    LINES TERMINATED BY '\\n'\
                    IGNORE 0 LINES;"\
                    %(drbase,i,db_name,tb_name))
        conn.commit()
#cur.close()

end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)

'''