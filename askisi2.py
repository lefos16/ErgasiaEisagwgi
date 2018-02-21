import datetime
import os

def main(): 
		day=0
		count=0
		year=0
		cur_date=datetime.datetime.now()
		day=cur_date.day
		for i in range(0,10):
				year=cur_date.year + i 
				for j in range(1,13):
						date1=datetime.datetime(year,j,day)
						if date1.weekday()==cur_date.weekday() and cur_date<date1:
								count=count+1
		print(count)
main()
