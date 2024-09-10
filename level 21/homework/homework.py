import random

def guess_number():
    # აირჩიე რიცხვი 1-დან 100-მდე
    target_number = random.randint(1, 100)
    
    print("გამოიცანი რიცხვი 1-დან 100-მდე!")
    
    attempts = 0
    
    while True:
        # მოითხოვე მომხმარებლისგან რიცხვის შეყვანა
        try:
            guess = int(input("შეიყვანეთ რიცხვი: "))
        except ValueError:
            print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
            continue
        
        # განისაზღვროს რამდენი მცდელობა დასჭირდა
        attempts += 1
        
        # შეამოწმე გამოთვლილი რიცხვის სისწორე
        if guess < target_number:
            print("ჩვეულებრივ! იმედია ეს რიცხვი უფრო მაღალია.")
        elif guess > target_number:
            print("გთხოვთ, სცადოთ დაბალი რიცხვი.")
        else:
            print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი {target_number}!")
            print(f"თქვენ გააკეთეთ {attempts} მცდელობა.")
            break

# გაწვდოს პროგრამა
if __name__ == "__main__":
    guess_number()

