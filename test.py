C = input("Choose your charecter to insert. ")
P = int(input("Choose your character's position. "))
S = input("Choose your string. ")

if P > len(S):
    print(S)
else:
    st = S[:P] + C + S[P:]

    print(st)
    print(C, P, S)