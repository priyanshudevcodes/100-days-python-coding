import time
import random
# Typing speed tester
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an incredibly versatile programming language.",
    "Practice makes perfect when it comes to typing speed."
]
while True:
    print("1. Test your typing speed\n2. Quit")
    try:
        user_choice = int(input("Enter the respective number of your choice: "))
    except ValueError as e:
        print("Please enter a valid value")
        continue
    if user_choice == 1:
        target_text = random.choice(sentences)
        print(target_text)
        # calculate time
        time_start = time.perf_counter()
        user_input = input("Type the above sentence here as fast as you can: ")
        time_end = time.perf_counter()
        # calculate speed
        time_taken = time_end - time_start
        words = len(user_input) / 5
        minute = time_taken / 60
        wpm = words / minute if minute > 0 else 0
        #calculate accuracy
        user_words = user_input.split()
        target_words = target_text.split()
        matches = sum(1 for a, b in zip(user_words, target_words) if a == b)
        accuracy = (matches / len(target_words)) * 100 if target_words else 0
        print(f"Results\nTime taken: {time_taken:.2f} seconds\nSpeed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%")
    elif user_choice == 2:
        break