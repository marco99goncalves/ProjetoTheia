# main.py
import argparse
import MergeScript
import SlidingWindow
import SubsetCreator

parser = argparse.ArgumentParser(description="A simple pipeline to create random tests for the Theia Project")

parser.add_argument('-p', '--preprocess', action='store_true', help="Run the Pre-Processing Scripts", required=False,
                    default=False)
parser.add_argument('-a', '--attack', type=float, help="Percentage that of each attack subset to use", required=False,
                    default=0.1666667)
parser.add_argument('-v', '--validation', type=float, help="Percentage of validation rows to use", required=False,
                    default=0.25)
parser.add_argument('-t', '--training', type=float, help="Percentage of training rows to use", required=False,
                    default=0.25)
parser.add_argument('-w', '--window', type=int, help="Window size to use, ignored if no Pre-Processing to be done", required=True)

args = parser.parse_args()

if args.preprocess:  # Run the merge and sliding window scripts
    print("Running merge script")
    MergeScript.run()
    print("Running sliding window script")
    SlidingWindow.run(args.window)

print("Running subset creator script")
SubsetCreator.run(args.attack, args.validation, args.training)
