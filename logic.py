import pandas as pd
import numpy as np

memorryData = pd.read_csv("memory.csv") 
memorryData = memorryData.replace(np.nan, '', regex=True)

def LOAD2ACC(address):
    global memorryData
    address = int(''.join(address))
    nAdd = memorryData['Data'][int(address)%200]
    if(nAdd==""):
        return 0
    else:
        return int(memorryData['Data'][int(address)%200])
    return 0

def STORE2MEM(address, data):
    global memorryData
    memorryData['Data'][int(address)%200] = data
    memorryData.to_csv("memory.csv",index=False)
    return 0

def mainF(l):
    a = 0
    e = 0
    instruction = []
    for i in range(len(l)):
        if(l[i][0]=="2"):
            print(int(l[i][1:]))
            if(int(l[i][1:]) not in [200,201,202,203,204]):
                a = 0
                e += 1
            else:
                a = LOAD2ACC(l[i][1:])
                e += 0
                instruction.append("Load memory word from Address {} to AC -> {}\n".format(l[i][1:],a))
        if(l[i][0]=="1"):
            if(int(l[i][1:]) not in [200,201,202,203,204]):
                a = 0
                e += 1
            else:
                a = a + LOAD2ACC(l[i][1:])
                e += 0
                instruction.append("Add memory word from Address {} to AC -> {}\n".format(l[i][1:],a))
        if(l[i][0]=="0"):
            if(int(l[i][1:]) not in [200,201,202,203,204]):
                a = 0
                e += 1
            else:
                a = a & LOAD2ACC(l[i][1:])
                e += 0
                instruction.append("And memory word from Address {} to AC -> {}\n".format(l[i][1:],a))
        if(l[i][0]=="3"):
            if(int(l[i][1:]) not in [200,201,202,203,204]):
                a = 0
                e += 1
            else:
                STORE2MEM(l[i][1:],a)
                e += 0
                instruction.append("Store AC {} to memory word to Address{} \n".format(a,l[i][1:]))
        if(l[i]=="7020"):
            a = a + 1
            e += 0
            instruction.append("Increment AC -> {}\n".format(a))
        if(l[i]=="7200"):
            a = ~a
            e += 0
            instruction.append("Complement AC -> {}\n".format(a))
        if(l[i]=="7800"): 
            a = ""
            instruction.append("Clear AC\n")
        if(l[i]=="7080"):
            a = a >> 1
            instruction.append("Circulate AC right -> {}\n".format(a))
        if(l[i]=="7040"):
            a = a << 1
            instruction.append("Circulate AC left -> {}\n".format(a))
        if(l[i]=="7001"):
            instruction.append("Halt\n")
            break
    return [a,e,instruction]