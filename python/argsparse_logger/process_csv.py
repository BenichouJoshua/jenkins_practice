import argparse
import pandas as pd
from logger import Logger

parser = argparse.ArgumentParser()
parser.add_argument("filePath", help="path to file to process required", type=str)

args = parser.parse_args()
error_logger = Logger("error_logs.txt")
results = Logger("results.csv")
results.WriteToFile("number1,number2,addition_result")

df = pd.read_csv(args.filePath, encoding='latin1')

for row in df.iterrows():
    results.WriteToFile(f"{row[1][0]},{row[1][1]},{int(row[1][0]) + int(row[1][1])}")

print("added something")       
print("added something else!")       