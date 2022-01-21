import csv
import random

filename = "test.csv"


# write a random number in 500 rows, 12 columns
def write_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(500):
            writer.writerow([random.randint(0, 500) for i in range(12)])


write_csv(filename)
