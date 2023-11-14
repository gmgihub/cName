# TXT -> sys.argv[1]
# FILE_TYPE -> sys.argv[2]

import os
import sys

#=====================================
# GET STRING FROM .TXT & REMOVE \N or GIVE -help
if sys.argv[1] == '-h':
    print('\033[1;34;4m BRIEF \033[0m', '\n \tIt can change specify type file\'s name in path into new name stored in .txt\n')
    print('\033[1;31;43m MAKESURE \033[0m', '\n \t.txt file is UTF-8(without BOM)\n')
    print('\033[1;32;40m USAGE \033[0m', '\n \tcName  .txt  path  *.xxx\n')
else:
    TXT = open(sys.argv[1])
    lines = TXT.readlines()
    NEW = []
    for line in lines:
        NEW.append(line.replace("\n", ""))
    print('TXT:', NEW)


    #=====================================
    # GET FILE FROM DIR
    PATH = sys.argv[2]
    OLD = os.listdir(PATH)
    print('DIR:', OLD)

    #=====================================
    # SPECIFY FILE TYPE
    # file_type = '*.IM'
    file_type = sys.argv[3]
    NAME = os.path.splitext(file_type)[0]
    TYPE = os.path.splitext(file_type)[1]
    print('FILE_TYPE:', TYPE) 

    cnt = 0
    length = len(OLD)
    while cnt < length:
        if os.path.splitext(OLD[cnt])[1] != TYPE: 
            OLD.pop(cnt)
            cnt-=1
            length-=1
        cnt+=1

    #prob1:for can't change OLD_file, it just increases, so may jump out some elements
    #prob2:In this case, it's mismatched between OLD_file and cnt.

    #for OLD_file in (OLD):                            
        #print(cnt, OLD_file, OLD)
        #if os.path.splitext(OLD_file)[1] != TYPE: 
        #    OLD.pop(cnt)
        #    cnt-=1
        #cnt+=1

    print('EXTRACT:', OLD)
    print('TXT_AMOUNT:', len(NEW))
    print('EXTRACT_AMOUNT:', len(OLD))
    #=====================================
    for i in range(len(OLD)):
        os.rename(OLD[i],  os.path.join(f'{NEW[i]}{TYPE}'))
