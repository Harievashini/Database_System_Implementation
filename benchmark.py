#importing some packages
import random
import csv

#convert the stringu1 and stringu2 to have first 7 characters between 'A-Z' followed by 45 x's
def char_convert(unique):
    result = []
    u = unique
    tmp = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
    for i in range(52):
        if i < 7:
            result.append('A')
        else:
            result.append('x')
    i = 6
    while u > 0:
        rem = u % 26
        tmp[i] = (chr(ord('A') + rem))
        u = int(u/26)
        i = i - 1
    j = 1
    for j in range(7):
        result[j] = tmp[j]
    n = ''
    for x in result:
        n += x

    return n

#cyclic generation of the string4 tuple to have AAAAxxxx's, HHHHxxx's, OOOOxxxx's, VVVVxxxx's
def generate_string4(tupCount):
    result = list()
    u = tupCount
    n = ''
    for i in range(52):
        result.append('x')
    if u % 4 == 0:
        for j in range(4):
            result[j] = 'A'
    if u % 4 == 1:
        for j in range(4):
            result[j] = 'H'
    if u % 4 == 2:
        for j in range(4):
            result[j] = 'O'
    if u % 4 == 3:
        for j in range(4):
            result[j] = 'V'
    #convert the list to string
    for x in result:
        n += x
    return n

#generating the remaining tuples using the unique1 value
def generate_relation(tupCount, filename):
    #Contains tuples
    data=[] 
    #Attribute fields
    fields=["unique1", "unique2", "two", "four", "ten", "twenty", "onePercent", "tenPercent", "twentyPercent","fiftyPercent", "unique3", "evenOnePercent", "oddOnePercent", "stringu1", "stringu2", "string4"]
    #All Attribute values are generated
    unique2 = list(range(0, tupCount))
    unique1 = random.sample(unique2, tupCount)
    for i in range(tupCount):
        two = random.choice(unique1) % 2
        four = random.choice(unique1) % 4
        ten = random.choice(unique1) % 10
        twenty = random.choice(unique1) % 20
        onePercent = random.choice(unique1) % 100
        tenPercent = random.choice(unique1) % 10
        twentyPercent = random.choice(unique1) % 5
        fiftyPercent = random.choice(unique1) % 2
        unique3 = random.choice(unique1)
        evenOnePercent = onePercent * 2
        oddOnePercent = (onePercent * 2) + 1
        stringu1 = char_convert(unique1[i])
        stringu2 = char_convert(unique2[i])
        string4 = generate_string4(i)
        tuples=[unique1[i], unique2[i], two, four, ten, twenty, onePercent, tenPercent, twentyPercent,fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4]
        # Appending the tuple to the entire set
        data.append(tuples)
    #Open the csv file and write the tuples
    with open(filename, 'w') as csvfile:
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
        # writing the fields  
        csvwriter.writerow(fields)  
        # writing the data rows  
        csvwriter.writerows(data) 
    #CSV file is now created
    print(filename+" created with "+ str(tupCount)+" tuples")

#Input the count of tuples and the filename
tupCount=input("Enter number of tuples\n")
filename=input("Enter file name\n")
tupCount=int(tupCount)
filename=filename+'.csv'
#Function to generate the tuples
generate_relation(tupCount,filename)
