"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
view-source:http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?201008262022&0&MINDB_01M&0&a
www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?201708270810&0&MINDB_10M&0&m
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import os

#processing library
import multiprocessing as proc
import sys

start_time=str(datetime.now())

prefix = 'AWS-01min'

def crawler(year, month, day, hour, minute):
    my_file = Path('%d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute))
    f = '%d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute)
    #print(f)
    if my_file.is_file():
        print ('check the File %s **********\n' % (f))
        #print ('check the File %d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute))
        read_file = open(f, 'r')
        #read_file = open('%d/%s_%d%02d%02d%02d%02d.csv', 'r' % (str(year), prefix, str(year), str(month), str(day), str(hour), str(minute)))
        raw_lists = read_file.read()
        #print(raw_lists)
        raw_lists = raw_lists.split('\n')
        er = 0
        for j in range(1,(len(raw_lists)-1)):
            #print(raw_lists[j])
            row = raw_lists[j].split(',')
            if len(row) < 3 or len(row) > 100 : 
                er = 100
            elif row[6]=='.' : er = er + 1

        if er > 40 :
            print ('delete and redownloading the File %s----------\n' % (f))
            os.remove('%d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute))
        
            try:
                url = "http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?%d%02d%02d%02d%02d&0&MINDB_01M&0&a" % (year, month, day, hour, minute)
                output =''
                soup = BeautifulSoup(urlopen(url), "html.parser")
                mytable = soup.find_all('table')
                #mytable = soup.find_all('table')
                #only mytable[1] contains weather data
                for trs in mytable[1].find_all('tr'):
                    for tds in trs.find_all('td'):
                        #print data
                        output += tds.text
                        #csv delimeter
                        output += ','
                        #csv delimeter
                    output += '\n'
                        #open output file
                with open('%d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute), 'w') as f:
                    #write
                    f.write(output)

            except:
                sys.stderr.write('Error the File %s **********\n' % (f))
                pass
        else :
            print ('No problem with the File %s ++++++++++\n' % (f))

    else:	
        while True:
            try:
                url = "http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?%d%02d%02d%02d%02d&0&MINDB_01M&0&a" % (year, month, day, hour, minute)
                output =''
                soup = BeautifulSoup(urlopen(url), "html.parser")
                mytable = soup.find_all('table')
                #mytable = soup.find_all('table')
                #only mytable[1] contains weather data
                for trs in mytable[1].find_all('tr'):
                    for tds in trs.find_all('td'):
                        #print data
                        output += tds.text
                        #csv delimeter
                        output += ','
                        #csv delimeter
                    output += '\n'
                        #open output file
                with open('%d/%s_%d%02d%02d%02d%02d.csv' % (year, prefix, year, month, day, hour, minute), 'w') as f:
                    #write
                    f.write(output)
                break
            except:
                sys.stderr.write('Error the File %s ********** \n' % (f))
                pass


q = proc.Queue()
P = []

for Yr in range(2007,2008):
    for Mo in range(1,2):
        for Da in range(1,2):
            for Ho in range(0,1):  
                for Mn in range(0,60): 
                    P.append(proc.Process(target=crawler, args=(Yr, Mo, Da, Ho, Mn,)))
'''
for i in range(len(P)):
    P[i].start()
    print (q.get())
    P[i].join()
'''
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)
