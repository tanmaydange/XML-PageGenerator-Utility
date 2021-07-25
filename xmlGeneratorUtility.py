#!/usr/bin/python


import xml.etree.ElementTree as ET
import dataLoader as dl

inputList =[]

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
        print('Saving File..'+"output-"+str(i)+".xml")
        tree.write("output/output-"+str(i)+".xml")
        i=i+1
        print("")

if __name__ == "__main__":
    inputList=dl.readCsvFile('input.csv')
    generatePages(inputList)
