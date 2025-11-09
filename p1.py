import random
from collections import Counter

num, chances = random.randint(100, 999), 10

for _ in range(chances):
    print("generated num is:", num)
    try:
        g = int(input("3 digit likh 😭: "))
        if not 100 <= g <= 999: print("3 digit likh ❌."); continue
    except: print("chal chal chal."); continue

    if g == num: print("🎉 Jeet gaye!"); break
    elif Counter(str(g)) == Counter(str(num)): print("digits sahi hain, bas jumbled!")
    elif any(d in str(num) for d in str(g)): print("ek digit sahi hai.")
    else: print("sab galat 😭.")

    print("too low." if g < num else "too high.")
    chances -= 1
    print(f"chances bache: {chances}\n")
else:
    print(f"😢 Haar gaye. Number tha {num}.")



# import random

# num = random.randint(100, 999)
# chances = 10

# def guess_num():
#     while True:
#         try:
#             g = int(input("3 digit likh 😭: "))
#             if 100 <= g <= 999:
#                 return g
#             print("3 digit likh ❌.")
#         except:
#             print("chal chal chal.")

# for _ in range(chances):
#     print("generated num is:", num)
#     g = guess_num()

#     if g == num:
#         print("🎉 Jeet gaye!")
#         break
#     elif sorted(str(g)) == sorted(str(num)):
#         print("digits sahi hain, bas jumbled!")
#     elif any(d in str(num) for d in str(g)):
#         print("ek digit sahi hai.")
#     else:
#         print("sab galat 😭.")

#     print("too low." if g < num else "too high.")
#     chances -= 1
#     print(f"chances bache: {chances}\n")
# else:
#     print(f"😢 Haar gaye. Number tha {num}.")


