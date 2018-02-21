import os
import random

def main():
		sum = 0
		for i in range(1,1001):
			d={}
			for i in range(1,101):
					ranNUM = random.sample(range(1, 80), 5)
					d[i] = ranNUM
			found = False
			count = 0
			while found==False:
					count+=1
					ranNUM1 = random.sample(range(1, 80), 5)
					for i in range(1,101):
									if ranNUM1==d[i]:
													found= True
													print(d[i])
													print(count)
													sum = sum + count
		mesosOros = sum / 1000
		print(mesosOros)
main()
