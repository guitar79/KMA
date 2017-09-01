"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
view-source:http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?201008262022&0&MINDB_01M&0&a
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import time
from datetime import date
import re

output = ''

for year in range(2016,2017):
	for Mo in range(1,2):
		for Da in range(1,32):
			for Ho in range(0,24):
				for Mn in range(0,61): 
					url = "http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?%d%02d%02d%02d%02d&0&MINDB_01M&0&a" % (year, Mo, Da, Ho, Mn)
					soup = BeautifulSoup(urlopen(url), "html.parser")
					mytable = soup.find_all('table')
					#only mytable[1] contains weather data
					for trs in mytable[1].find_all('tr'):
						for tds in trs.find_all('td'):
							#print data
							output += "%d%02d%02d%02d%02d" % (year, Mo, Da, Ho, Mn)
							output += tds.text
							#csv delimeter
							output += ','
						#csv delimeter
						output += '\n'



#open output file
with open('output.csv', 'a', encoding='utf8') as f:
	#write
	f.write(output)