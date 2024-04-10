enx = input('Enter Encrypted x: ')
eny = input('Enter Encrypted y: ')
# Separates the input number with a dot
enx = enx.split(".")
eny = eny.split(".")
enx[0] = int(enx[0])
eny[0] = int(eny[0])
# Round the first index of the list, which is an integer, and add it to the number 7 and to the power of 1/2
enx[0] = int(round((enx[0] + 7) ** (1/2)))
eny[0] = int(round((eny[0] + 6) ** (1/3)))
# We list the last index which is a float number
# for example: [7994.0.00000004]  [0]--> 7994   [1]--> 0  [2] or [-1]--> 00000004
enx[-1] = list(enx[-1])
eny[-1] = list(eny[-1])
# insert the first index with a dot
# for example: [00000004]  [0]--> 0   [1]--> 0    [1] Convert dot
enx[-1].insert(1, ".")
eny[-1].insert(1, ".")
# Concatenates all words in the list with nothing (all as a string)
enx[-1] = ''.join(enx[-1])
eny[-1] = ''.join(eny[-1])
# Convert string to integer
enx[-1] = int(round(float(enx[-1])))
eny[-1] = int(round(float(eny[-1])))
print("the result x: " + str(enx[0]) + "." + str(enx[-1]))
print("the result y: " + str(eny[0]) + "." + str(eny[-1]))

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
