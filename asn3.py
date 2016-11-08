def readFile(filename):
    from itertools import islice
    data = []
    with open(filename, 'r') as infile:
        while True:
            next_n_lines = list(islice(infile, 3))
            if not next_n_lines:
                break
            raw = []
            for line in next_n_lines:
                line = line.strip("\n")
                line = line.strip('[').strip(']').strip('{').strip('}').split("\n")
                if line[0] == "":
                    continue
                raw.append(line)
            data.append(raw)
    returnData = []
    for line in data:
        returnRaw = []
        for tupple in line:
            returnRaw+=tupple[0].split(";")
        returnData.append(returnRaw)
    return returnData



def writeCsv(data):
    import csv
    with open("leafs.csv","w") as csvFile:
        fieldNames = data[0]
        del data[0]
        writer  = csv.DictWriter(csvFile,fieldNames)
        writer.writeheader()
        for row in data:
            #Some problem with data being written in csv`#
            writable = dict(zip(fieldNames,row))
            writer.writerow(writable)

def correctDate(row):
    import datetime
    #Need to correct the date by comparing the date column from row and todays date#
    #check http://stackoverflow.com/questions/2217488/age-from-birthdate-in-python#
    return row

data = [["#","NAME","POSITION","AGE","HEIGHT","WEIGHT","BIRTHDAY"]]
data+=readFile("leafs.dmbfmt")
writeCsv(data)








