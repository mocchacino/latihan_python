def fibonacci(ntimes):
    bil1 = 0
    bil2 = 1
    totbil = 0
    i = 1
    if ntimes <= 0:
        print("masukan nilai lebih besar dari 0")
    for i in range(ntimes):
        if ntimes == 1:
            print(bil1)
        else:
            print(bil1)
            totbil = bil1 + bil2

            bil1 = bil2
            bil2 = totbil

fibonacci(7)
