###############################################
# Name: Trey Brumley
# Class: CMPS 4663 Cryptography
# Date: 04 August 2015
# Program 3 - Elliptical Curve
###############################################

import argparse
import sys
import ec

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
	parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
	parser.add_argument("-x1",dest="x1", help="")
	parser.add_argument("-y1",dest="y1", help="")
	parser.add_argument("-x2",dest="x2", help="")
	parser.add_argument("-y2",dest="y2", help="")
	
	args = parser.parse_args()
	# Example:
	# python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1
	print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
	
	ec.plot(args.a, args.b, args.x1, args.y1, args.x2, args.y2)


if __name__ == '__main__':
    main()