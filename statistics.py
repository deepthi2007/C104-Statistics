import pandas as pd
import csv
from collections import Counter
from numpy import little_endian
from pandas.core.algorithms import mode

with open("SOCR-HeightWeight.csv",newline='') as f :
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
    weights = []
    for i in range(0,len(data)):
        weights.append(float(data[i][2]))
    size = len(weights)
    weights.sort()

    """ Mean """
    sum = 0
    for i in range(0,size) :
        sum = sum+weights[i]
    print("Mean : ",sum/size)

    """ Median """
    if size%2 == 0 :
        median1 = weights[size//2]
        median2 = weights[size//2-1]
        median = (median1+median2)/2
    else : 
        median = weights[size//2]
    print("Median :", median)

    """ Mode """
    count = Counter(weights)
    modeRange = {
        "100-110":0,
        "110-120":0,
        "120-130":0,
        "130-140":0,
        "140-150":0
    }
    for weight,occurence in count.items() :
        if 100 < float(weight) < 110 :
            modeRange["100-110"]+=occurence
        elif 110 < float(weight) < 120 :
            modeRange["110-120"]+=occurence
        elif 120 < float(weight) < 130 :
            modeRange["120-130"]+=occurence
        elif 130 < float(weight) < 140 :
            modeRange["130-140"]+=occurence
        else :
            modeRange["140-150"]+=occurence
    moderange, modeOccurence = 0,0
    for range , occurence in modeRange.items() :
        if occurence > modeOccurence :
            moderange,modeOccurence = range,occurence

    no = moderange.split('-')
    mode = (int(no[0])+int(no[1]))/2
    print("Mode : ",mode)