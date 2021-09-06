#!/usr/bin/python

from datetime import datetime
import xml.etree.ElementTree as ET
import dataLoader as dl
import json

inputList =[]
json_output_file = 's3bucket/output/output-'

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
	    # log('Saving File..'+"output-"+str(i)+".xml")
        print('Saving File..'+"output-"+str(i)+".xml")
        tree.write("s3bucket/output/output-"+str(i)+".xml")
        i=i+1

def generateJsonPage(inputList):
    index = 0            
    for item in inputList:   
        with open(json_output_file+str(index)+'.json','w') as fh:
            json.dump(item,fh,indent=4)
        print('Saved File..'+"output-"+str(index)+".json")    
        index += 1

if __name__ == "__main__":
    inputList=dl.readCsvFile('s3bucket/input/input.csv')
    generateJsonPage(inputList)
    generatePages(inputList)
