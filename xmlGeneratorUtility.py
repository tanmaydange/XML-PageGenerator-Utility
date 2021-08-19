#!/usr/bin/python

from datetime import datetime
import xml.etree.ElementTree as ET
import dataLoader as dl

inputList =[]

def log(string):
    print(str(datetime.now())+" | INFO | "+string)

def replaceFields(filedName, fieldValue,root):
    for elem in root.getiterator():
        try:
            elem.text  = elem.text.replace(filedName, fieldValue)
        except AttributeError:
            pass

def getKeys(dict):
    return dict.keys()


def generatePages(inputList):
    i=0;
    for input in inputList:
        with open('template/template.xml') as f:
            tree = ET.parse(f)
            root =  tree.getroot()
            root.attrib['id'] = input.get('ID')
            for key in getKeys(input):
                replaceFields(key, input.get(key),root)
	log('Saving File..'+"output-"+str(i)+".xml")
        tree.write("s3bucket/output/output-"+str(i)+".xml")
        i=i+1

if __name__ == "__main__":
    inputList=dl.readCsvFile('s3bucket/input/input.csv')
    generatePages(inputList)
