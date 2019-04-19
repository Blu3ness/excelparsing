import string
import time
import openpyxl


wb = openpyxl.load_workbook('i:/sheet.xlsx')
sheet = wb.active




with open('i:/uklog.txt', 'r') as f, open('i:/hi.txt', 'w') as w:
    # poop = f.readline().split()
    # print(poop)
    counter = 0
    print(counter)
    for line in f:

        if '`' in line:

            print(line.split())
            print(len(line))
            counter += 1
            w.write(line)
        try:
            hi = line.strip()

        except:
            pass

    print(counter)
