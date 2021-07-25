#!/usr/bin/python

import csv

def readCsvFile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        inputList = [] 
        for row in csv_reader:
            mydict = {}
            if line_count == 0:
                line_count += 1
            else:
                mydict["ID"]  = row[0]
                mydict["NAME"]  = row[1]
                mydict["EMAIL"]  = row[2]
                mydict["PRICE"]  = row[3]
                mydict["DESCRIPTION"]  = row[4]
                mydict["IMAGE_URL"]  = row[5]
                line_count += 1
            
            if (bool(mydict)):
                inputList.append(mydict)
        return inputList
