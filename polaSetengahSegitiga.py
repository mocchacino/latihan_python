"""
Buat pola segitiga siku-siku, dan pola lainnya (biasanya pake * bintang)

*
**
***
****
*****
"""
def setengahSegitiga(num):
    for n in range(0,num+1):
        line = ""
        for x in range(0,n):
            line += "*"
        print(line)

setengahSegitiga(5)