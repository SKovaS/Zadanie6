def pyramid():
    size=23
    while True:
        raz = int(input("Enter height: "))
        if raz>size or raz<0:
           break
        for i in range(1, raz+1):
                for q in range(raz - i, 0, -1):
                    print(" ", sep=' ', end='')
                for j in range(1, i + 2):
                    print("#", sep=' ', end='')
                print()
        break
pyramid()