import random

def guessing_game():
    print("დავიწყოთ თამაში: რიცხვების გამოცნობა!")
    print("ჩავიფიქრე რიცხვი 50-დან 100-მდე.")
    print("რა რიცხვი ჩავიფიქრე?")

    secret_number = random.randint(50, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("ჩაწერე შენი რიცხვი: "))
            attempts += 1

            if guess < secret_number:
                print("ჩემსაზე დაბალია! თავიდან ცადე.")
            elif guess > secret_number:
                print("ჩემსაზე მაღალია! თავიდან ცადე.")
            else:
                print(f"გილოცავ! შენ შეძელი {attempts} ცდაში გამოცნობა.")
                break
        except ValueError:
            print("გთხოვ, ჩაწერო ნატურალური რიცხვი.")

guessing_game()
