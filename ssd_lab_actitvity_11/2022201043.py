import csv


with open("input.csv", "r") as source:
    reader = csv.reader(source, delimiter=',',skipinitialspace=True)
    col = len(next(reader))
    source.seek(0)
    lines = 0
    with open("avg_output.txt", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            if (lines == 0):
                writer.writerow((r[0:col-6]))
            else:
                ls = list()    
                ls.append(r[col-7])
                lis = list()
                for i in range(len(ls)):
                    lis.append(float(ls[i]))
                filtered = list(filter(lambda x:x>=-3, lis))
                # print(filtered)
                if(len(filtered)>0):
                    writer.writerow((r[0:col-6]))
            lines+=1

avg_open, avg_high, avg_low = [],[],[]
with open("avg_output.txt", "r") as source:
    reader = csv.reader(source, delimiter=',', skipinitialspace=True)

    col = len(next(reader))
    lines = 0
    for r in reader:
        avg_open.append(r[1])
        avg_high.append(r[2])
        avg_low.append(r[3])
        lines+=1

data = []
openf=list(map(lambda x: float(x.replace(',', '')), avg_open))
data.append([sum(openf)/len(openf)])
high=list(map(lambda x: float(x.replace(',', '')), avg_high))
data.append([sum(high)/len(high)])
low = list(map(lambda x: float(x.replace(',', '')), avg_low))
data.append([sum(low)/len(low)])

with open('avg_output.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

char = input("Enter single starting character: ")
with open("input.csv", "r") as source:
    reader = csv.reader(source, delimiter=',',skipinitialspace=True)
    col = len(next(reader))
    with open("stock_output.txt", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            if r[0][0]==char:
                ls = list()
                ls.append(r[col-7])
                lis = list()
                for i in range(len(ls)):
                    lis.append(float(ls[i]))
                filtered = list(filter(lambda x: x >= -3, lis))
                if (len(filtered) > 0):
                    writer.writerow((r[0:col-6]))
