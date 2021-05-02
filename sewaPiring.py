"""
Vikrie menyewakan 6 gros piring. 
Sebanyak 4 lusin dipinjam tio dan sebanyak 2 gros dipinjam david.
berapa piring yang tersisa di vikrie?? (1 gross = 144 , 1 lusin = 12)
"""
def sisaPiring():
    total = 6 * 144
    tio = 4 * 12
    david = 2 * 144

    return (total - tio - david)

print(sisaPiring())