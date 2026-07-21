from pathlib import Path
import shutil
from rich import print
while True:
    print("1. For seeing the files and their extenctions\n2. Organize the files\n3. Quit")
    try:
        user_choice = int(input("Enter the number of the respective task you wanna perfomr: "))
    except ValueError as e:
        print(f"Enter a valid value\nError:{e}")
        continue
    if user_choice == 3:
        break
    user_main_folder = input("Creat the sub folder in your main folder and enter the name of that folder here: ")
    main_folder = Path.cwd()
    targeted_folder = main_folder/user_main_folder
    if user_choice == 1:
        for items in targeted_folder.iterdir():
            if items.is_file():
                print(f"The file name is {items.name} and the extention is {items.suffix}")
    elif user_choice == 2:
        print("[bold red]IMPORTANT DESCRIPTION: This programme only supports three extentions yet [.pdf,.jpg,.mp3,.py] other extentions will be added later......")
        user_extention = input("Enter the extention of files you want to oraganize into a folder[example for pdf files enter pdf]: ")
        if user_extention == "pdf":
            # for pdf files
            pdf_folder = targeted_folder/"Documents"
            pdf_extention = targeted_folder.glob("*.pdf")
            pdf_folder.mkdir(parents=True,exist_ok=True)
            for file_path in pdf_extention:
                if file_path.name == Path(__file__).name:
                    continue
                destination = pdf_folder/file_path.name
                if destination.exists():
                    print(f"Skipped (already exists): {file_path.name}")
                    continue
                shutil.move(file_path,destination)
                print(f"Moved:{file_path.name}")
        elif user_extention == "jpg":
            # for jpg files
            jpg_folder = targeted_folder/"Images"
            jpg_extention = targeted_folder.glob("*.jpg")
            jpg_folder.mkdir(parents=True,exist_ok=True)
            for file_path in jpg_extention:
                if file_path.name == Path(__file__).name:
                    continue
                destination = jpg_folder/file_path.name
                if destination.exists():
                    print(f"Skipped (already exists): {file_path.name}")
                    continue
                shutil.move(file_path,destination)
                print(f"Moved:{file_path.name}")
        elif user_extention == "mp3":
            # for mp3 files
            mp3_folder = targeted_folder/"Audio"
            mp3_extention = targeted_folder.glob("*.mp3")
            mp3_folder.mkdir(parents=True,exist_ok=True)
            for file_path in mp3_extention:
                if file_path.name == Path(__file__).name:
                    continue
                destination = mp3_folder/file_path.name
                if destination.exists():
                    print(f"Skipped (already exists): {file_path.name}")
                    continue
                shutil.move(file_path,destination)
                print(f"Moved:{file_path.name}")
        elif user_extention == "py":
            # for python files
            py_folder = targeted_folder/"Python Programmes"
            py_extention = targeted_folder.glob("*.py")
            py_folder.mkdir(parents=True,exist_ok=True)
            for file_path in py_extention:
                if file_path.name == Path(__file__).name:
                    continue
                destination = py_folder/file_path.name
                if destination.exists():
                    print(f"Skipped (already exists): {file_path.name}")
                    continue
                shutil.move(file_path,destination)
                print(f"Moved:{file_path.name}")
        else:
            print("Please only enter the respective extentions names......")







