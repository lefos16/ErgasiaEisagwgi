import os
import random

def main(): 
		p=0
		ranNUM = random.sample(range(-30,29),30)
		print(ranNUM)
		for i in range(0,28):
				for j in range(i+1,29):
						for k in range(j+1,30):
								r = ranNUM[i] + ranNUM[j] + ranNUM[k]
								if r == 0:
										p = p + 1
		if p == 0:
				print("no match")
		else:
				print(p)
main()
