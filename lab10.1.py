import random
import os

if os.path.exists('numbers.txt'):
    with open('numbers.txt', 'r') as file:
        car_numbers = file.readlines() 

    if car_numbers: 
        full_numbers = []
        for number in car_numbers:
            number = number.strip()  
            random_digits = random.randint(1000, 9999)
            full_number = f"{number} {random_digits}"
            full_numbers.append(full_number)
        
        print("Дані, що будуть записані у full_numbers.txt:")
        print(full_numbers)
        
        with open('full_numbers.txt', 'w') as file:
            for full_number in full_numbers:
                file.write(full_number + '\n')

        print("Серії номерів з випадковими чотиризначними числами збережені у файл full_numbers.txt.")
    else:
        print("Файл numbers.txt порожній або не містить серій номерів.")
else:
    print("Файл numbers.txt не знайдено.")
