from src.driver.ScientificCalc import ScientificCalc
import sys
import argparse

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True, nargs='+')
    args=parser.parse_args()
    arguments=args.function
    method_name = arguments[0]
    angle = arguments[1]
    calc = ScientificCalc()
    if method_name=='calculate_sin':
        res = calc.calculate_sin(angle)
        print(res)
    else:
        print("method not found")