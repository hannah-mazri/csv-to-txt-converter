import csv

# before running the code:
# please make sure that the data in the CSV file follows the structure in example_data.csv
# i.e. first column: X, second column: Y, the rest are columns for wavelength/intensity
# no need to rename the csv file


input_file = open('example_data.csv', newline='')    #change <example_data> to filename of interest
reader = csv.reader(input_file)
row1 = next(reader)[2:]

for r, row in enumerate(reader):
    # print(r)
    x = row[0]
    y = row[1]
    row1_copy = [row1.copy()]
    row1_copy.append(row[2:])

    with open(f'SiC_x{float(x)}_y{float(y)}_intensity_{r}.txt', 'w', newline='') as output_file:
        for index, x_row in enumerate(row1_copy[0]):
            colStr = f'{float(row1_copy[0][index])} {float(row1_copy[1][index])}'
            writer = csv.writer(output_file)
            writer.writerow(colStr.split(","))