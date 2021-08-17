#!/usr/bin/python

from Author import Author
from Book import Book
import csv


def readCsvFile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        inputList = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                book = Book(row[0], row[1],
                            row[2], row[3], row[4], row[5])
                bookDictionary = book.__dict__
                print(bookDictionary)
                inputList.append(bookDictionary)
                line_count += 1

        return inputList
