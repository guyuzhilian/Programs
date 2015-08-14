# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-14 17:39
sd={0:0,1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
dd1={10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
dd2={2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
td= {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}
cd={0:0,1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9:    4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:9,19:8}


def cw(n) :
    if n/10 == 0 :               # If the number is less than 10 execute this section
        length = sd[n%10]
    elif n/100 == 0 :           # If the number is less than 100 execute this section
        if n<20 :
            length = (dd1[n])         # Directly map to dd1
        else :
            length = (dd2[n/10]+sd[n%10])  # If the number is > 20 do a construction
    elif n/1000==0 :
        if n%100==0:
            length = sd[n/100] + 7        # If the number is multiples of 100 give assuming single digit and 7 for hundred
        elif n%100 < 20 :
            length = td[n/100] + cd[n%100]  # If 3 digit numbers not more than *20 , then direct mapping
        else :
            length = td[n/100] + dd2[(n%100)/10] + sd[n%10]

    print(n, length)
    return length

count = 0
for i in range(1,506) :
 count = count + cw(i)
print count