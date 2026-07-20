import secrets, string, re
from rich import print
while True:
    print("""[bold green]1.Generate Password...
2.Password Strength Analyzer...[/bold green][bold red]\n3.Quit...[/bold red]""")
    try:
        user_choice = int(input("Enter the number of respective task do you wanna perform: "))
    except ValueError as e:
        print(f"Please enter a valid value\nError: {e}")
        continue
    if user_choice == 1:
        try:
            pass_lenght = int(input("How much lenght of password do you want?[suggested is 12 ]: "))
            pass_letters = int(input("How many letter do you want in you password?[suggested is 4]: "))
            pass_numbers = int(input("How many digit do you want in your password?[suggested is atleast 3]: "))
            pass_symbols = int(input("How many specialo character do you want in you password?[suggested is alteast 2]: "))
            if pass_letters + pass_numbers + pass_symbols > pass_lenght:
                print("Requirements exceed the password length.")
                exit()
        except ValueError as e:
            print(f"Please enter a valid value\nError: {e}")
            continue
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = "".join(secrets.choice(alphabet) for _ in range(pass_lenght))
            if(
            any(s.islower() for s in password) and
            any(s.isupper() for s in password) and
            sum(s.isdigit() for s in password) >= pass_numbers and
            sum(s in string.punctuation for s in password) >= pass_symbols and
            sum(s in string.ascii_letters for s in password) >= pass_letters
                ):
                    print(password)
                    break
    elif user_choice == 2:
        user_pass = input("Enter you password to analyze: ")
        has_lower = re.search(r"[a-z]",user_pass)
        has_upper = re.search(r"[A-Z]",user_pass)
        has_digit = re.search(r"[0-9]",user_pass)
        has_sym = re.search(r"[^A-Za-z0-9]",user_pass)
        long_enough = len(user_pass) >= 12
        length = len(user_pass)
        score = 0
        if has_lower:
            score += 8
        if has_upper:
            score += 8
        if has_digit:
            score += 15
        if has_sym:
            score += 22
        if length >= 12:
            score += 47
        else:
            score -= 5
        print("✓ lowercase" if has_lower else "✗ no lowercase")
        print("✓ uppercase" if has_upper else "✗ no uppercase")
        print("✓ digits" if has_digit else "✗ no digits")
        print("✓ special characters" if has_sym else "✗ no special characters")
        print("✓ Good! long enough" if long_enough else "✗ not long enough")
        print(score)
        if score >= 75:
            print("[bold green]Strong[/bold green]")
        elif score >= 45:
            print("[bold yellow]Medium[/bold yellow]")
        else:
            print("[bold red]Weak[/bold red]")
    
    elif user_choice == 3:
         break

