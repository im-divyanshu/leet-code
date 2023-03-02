def roman_to_int(roman_num):
    int_num=0
    for i in range(0,len(roman_num)):
        if roman_num[i]=="M":
            int_num+=1000
        if roman_num[i]=="D":
            int_num+=500
        if roman_num[i]=="C":
            try:
                if(roman_num[i+1]=="D" or roman_num[i+1]=="M"):
                    int_num-=100
                else:
                    int_num+=100
            except:
                int_num+=100
        if roman_num[i]=="L":
            int_num+=50
        if roman_num[i]=="X":
            try:
                if(roman_num[i+1]=="C" or roman_num[i+1]=="L"):
                    int_num-=10
                else:
                    int_num+=10
            except:
                int_num+=10
        if roman_num[i]=="V":
            int_num+=5
        if roman_num[i]=="I":
            try:
                if(roman_num[i+1]=="X" or roman_num[i+1]=="V"):
                    int_num-=1
                else:
                    int_num+=1
            except:
                int_num+=1

    return int_num

for i in range(1,100):
    roman_num=input("please enter a roman number : ")

    print(roman_to_int(roman_num))