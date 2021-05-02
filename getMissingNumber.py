def getMissingNumber(numbers, totalCount):
    hilang = []
    for angka in range(1, totalCount, 1):
        if angka not in numbers:
            hilang.append(angka)
    print(hilang)

getMissingNumber([1, 2, 3, 5], 5)
