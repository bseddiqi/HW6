import time
startTime = time.time()
def fizzbuzz():
    for i in range(101):
        if i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print('buzz')
        elif i%3==0 and i%5==0:
            print('fizzbuzz')
        else:
            print(i)

    executionTime = (time.time() - startTime)
    print("Execution time is : ", executionTime)

fizzbuzz()

import math

def volumeSphere():
    radius = float(input("What is the radius of the circle: "))
    volume = 4/3*(math.pi)*radius
    print("The volume of the sphere is: ", volume)

volumeSphere()


import csv


def csvFile():
    header = ["Country", 'State', 'County', 'City']
    rows = [
    {'Country':'USA','State':'GA','County':'Dekalb','City':'Stone Mtn.'},
    {'Country':'USA','State': 'CA','County':'Los','City': 'Angeles'}
    ]

    
    with open ('bio.csv','w', encoding='UTF=8', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        #writer = csv.writer(f)
        writer.writeheader()
        writer.writerows(rows)

    filename = 'bio.csv'
    print('File name is: ',filename)

csvFile()


def printCSV():
    with open('/home/bseddiqi3/bio.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
printCSV()

import tempfile
import os

def Temporary():
    f = tempfile.NamedTemporaryFile(delete=False)
    try:
        header = ["Country", 'State', 'County', 'City']
        rows = [
    {'Country':'USA','State':'GA','County':'Dekalb','City':'Stone Mtn.'},
    {'Country':'USA','State': 'CA','County':'Los','City': 'Angeles'}
    ]
    
        with open ('tempfile','w', encoding='UTF=8', newline = '') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            #writer = csv.writer(f)
            writer.writeheader()
            writer.writerows(rows)

        with open('tempfile', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        
            
    finally:
        f.close()


Temporary()