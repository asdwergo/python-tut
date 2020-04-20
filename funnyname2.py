import sys
import random

def main():	
	print("random name\n")
	first=( 'ka', 'kar', 'karr', 'kay', 'kayy', 'ki', 'ke', 'kee', 'ko', 'koe')
	middle=('aa' ,'ar', 'arr', 'aye', 'ei', 'ae', 'aee', 'ao', 'aoe')
	last=('la', 'lar', 'larr', 'lay', 'layy','li', 'le', 'lee', 'lo', 'loe')
	while True:
		firstN=random.choice(first)
		middleN=random.choice(middle)
		lastN=random.choice(last)
		print("\n\n")
		print("{}{}{}".format(firstN,middleN,lastN),file=sys.stderr)
		print("\n\n")
		try_again=input("\n\nTry again? (Press Enter else n to quit)\n ")
		if try_again.lower()=="n":
			break
			input("\nPress Enter to exit.")
if __name__=="__main__":
	main()
