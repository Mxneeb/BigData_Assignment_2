#!/usr/bin/env python3
import sys

#Defining myDICT array to save words in it
# temp user id will save the user id number 
MyDICT = {}
TempUserID_ = 0 
# running loop throughout the dataset 
for line in sys.stdin:
    MyDICT[TempUserID_] = line.strip()
    TempUserID_ += 1 

WORD_ARRAY = set()

for Sentence in MyDICT.values():
    WORD_ARRAY.update(Sentence.split())
#converting from set to list
WORD_ARRAY = sorted(list(WORD_ARRAY))

temp = enumerate(WORD_ARRAY)
i_WORD_ARRAY = list(temp)