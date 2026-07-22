# Number System Converter
# Note only binary,decimal and hexadecimal are allowed to use in this programme 
from rich import print
while True:
    print("1. Use Converter\n2. Use Operations on Binary Numbers\n3. Quit")
    try:
        user_choice = int(input("Enter the respective number for your task: "))
    except ValueError as e:
        print("[bold red]Please enter a valid value......[/bold red]")
        continue
    if user_choice == 1:
        try:
            type_of_num = input("Enter the name of the number system for decimal enter [d] for binary enter [b] for hexadecimal enter [h]: ")
        except ValueError as e:
            print("[bold red]Please enter a valide value......[/bold red]")
            continue
        if type_of_num == "d":
            try:
                decimal_num = int(input("Enter you decimal number: "))
            except ValueError as e:
                print("[bold red]Please enter a valid value......[/bold red]")
                continue
            print(f"Decimal to Binary: {decimal_num:b}")
            print(f"Decimal to hexadecimal(lower letters): {decimal_num:x}")
        elif type_of_num == "b":
            try:
                binary_num = input("Enter you binary number: ")
                dec = int(binary_num,2)
            except ValueError as e:
                print("[bold red]Please enter a valid value......[/bold red]")
                continue
            print(f"Binary to decimal: {dec}")
            print(f"Binary to hexadecimal: {dec:x}")
        elif type_of_num == "h":
            try:
                hex_num = input("Enter you hexadecimal number: ")
                dec = int(hex_num,16)
            except ValueError as e:
                print("[bold red]Please enter a valid value......[/bold red]")
                continue
            print(f"hexadecimal to decimal: {dec}")
            print(f"hexadecimal to binary: {dec:b}")
        else:
            print("[bold red]Please enter only (d,b,h) according to the desired outcome......")
# Bitwise Playgroud
    elif user_choice == 2:
        try:
            a = int(input("Enter you first number: "))
            b = int(input("Enter you second number: "))
        except ValueError as e:
            print("[bold red]Please enter a valid number.....[/bold red]")
            continue
        print(f"{a:04b} & {b:04b} = {a & b:04b}  ({a & b})")
        print(f"{a:04b} | {b:04b} = {a | b:04b}  ({a | b})")
        print(f"{a:04b} ^ {b:04b} = {a ^ b:04b}  ({a ^ b})")
        print(f"{a:04b} << 1 = {a << 1:b}  ({a << 1})")
        print(f"{a:04b} >> 1 = {a >> 1:b}  ({a >> 1})")
    elif user_choice == 3:
        break
    else:
        print("[bold red]Plese enter the respective task numbers only......[/bold red]")