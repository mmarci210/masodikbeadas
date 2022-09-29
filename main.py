def beadas(a,b,c):
    if a+b < c or a+c < b or b+c < a:
        print("A", a,",", b, "és", c,"háromszög NEM szerkezthető.")
    else:
        print("A", a, ",", b, "és", c, "háromszög szerkezthető.")


if __name__ == '__main__':
    print("Adja meg a háromszög három oldalát cm-ben:")
    a = int(input("a oldal (cm):"))
    b = int(input("b oldal (cm):"))
    c = int(input("c oldal (cm):"))
    beadas(a, b, c)