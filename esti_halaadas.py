
def esti_naplo(n):
    print("Üdv, ebben a kis programban te csinálod magadnak az alvásnaplót. Ahány nap óta vezeted, annyi számot adj meg, majd írd le külön naponta, miért vagy hálás ma.")
    print("Miért vagy hálás ma?")
    for i in range(1, n+1):
        print(f"{i}. nap: {input()}")

esti_naplo(5)