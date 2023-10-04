import random;

while True:
    try:
        num_max_range = int(input("range massimo: "))
        num_tentativi = int(input("num tentativi: "))
        break;
    except ValueError:
        print("[!] valore non valido")

num_indovina = random.randint(1,num_max_range)
print(num_indovina)
for i in range(num_tentativi):
    print(f"tentativi rimanenti: {num_tentativi-i}")
    check_num = int(input(">"))
    if check_num == num_indovina:
        print("indovinato!")
        break;
    else:
        if i!=num_tentativi-1:
            print("sbagliato")
        else:
            print("hai perso")










