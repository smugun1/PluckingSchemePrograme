# Initializing the data variable as a list
data = []

# Reading the data from the file and appending it to the data variable
with open('table.txt', 'r') as file:
    for line in file:
        row = line.strip().split('\t')
        data.append(row)


# Defining the function to update the table
def updateTable(row, col, val):
    data[row][col] = val


# Calling the function with the desired row, column and value
updateTable(3, 7, "5")

# Writing the data to a new file
with open('updated_table.txt', 'w') as file:
    for row in data:
        file.write('\t'.join(row))
        file.write('\n')