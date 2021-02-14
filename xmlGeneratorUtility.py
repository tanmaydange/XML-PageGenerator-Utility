#!/usr/bin/python


import xml.etree.ElementTree as ET

inputList =[
{
    "DESCRIPTION" : "Let Us C",
    "IMAGE_URL" : "https://springframework.guru/wp-content/uploads/2015/04/spring_framework_guru_shirt-rf412049699c14ba5b68bb1c09182bfa2_8nax2_512.jpg",
    "PRICE" : "495",
    "EMAIL" : "Yashwant@Kanitkar.com",
    "ID" : "10",
    "NAME" : "Yashwant Kanitkar"
},
{
    "DESCRIPTION" : "Angels and Daemons",
    "IMAGE_URL" : "https://springframework.guru/wp-content/uploads/2015/04/spring_framework_guru_shirt-rf412049699c14ba5b68bb1c09182bfa2_8nax2_512.jpg",
    "PRICE" : "900",
    "EMAIL" : "Dan@Brown.com",
    "ID" : "11",
    "NAME" : "Dan Brown"
}
]

def replaceFields(filedName, fieldValue):
    for elem in root.getiterator():
        try:
            elem.text  = elem.text.replace(filedName, fieldValue)
        except AttributeError:
            pass

def getKeys(dict):
    return dict.keys()


i=0;
for input in inputList:
    with open('template/template.xml') as f:
        tree = ET.parse(f)
        root =  tree.getroot()
        root.attrib['id'] = input.get('ID')
        print(tree.getroot().attrib['id'])
        for key in getKeys(input):
            replaceFields(key, input.get(key))
    print('Saving File..'+"output-"+str(i)+".xml")
    tree.write("output/output-"+str(i)+".xml")
    i=i+1
    print("")
