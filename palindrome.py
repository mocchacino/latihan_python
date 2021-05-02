"""
input string 
output palindrome or not
"""
def isPalindrome(kata):
    jumlah_kata = len(kata)
    dibalik = ""
    for n in range(jumlah_kata,0,-1):
        dibalik += kata[n-1]
    if (kata == dibalik):
        print("kata {} adalah palindrome".format(kata))
    else:
        print("kata {} adalah bukan palindrome".format(kata))

isPalindrome("buku")