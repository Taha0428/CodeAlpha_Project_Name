import os
import pandas as pd
import shutil

file_categories = {
    "Documents": [".txt", ".pdf", ".docx"],
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Videos": [".avi", ".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
}

base_path = r"C:\Users\Abdullah\Desktop\Genomac hub internship\Module 7"
temp_path = os.path.join(base_path, "temp")

def file_sort():
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            extension = os.path.splitext(item)[1]
            for folder, ext_list in file_categories.items():
                if extension in ext_list:
                    new_folder_path = os.path.join(base_path, folder)
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)
                    shutil.move(item_path, new_folder_path)
                    print(f"Moved {item} to {folder}")
                    break
    print("File sorting complete.")

def clean_csv(csv_filename):
    csv_path = os.path.join(base_path, csv_filename)
    if os.path.exists(csv_path):
        data = pd.read_csv(csv_path)
        data.fillna({"column_name": "Unknown"}, inplace=True)
        data.drop_duplicates(inplace=True)
        new_csv_path = csv_path.replace(".csv", "_cleaned.csv")
        data.to_csv(new_csv_path, index=False)
        print(f"Cleaned data saved to {new_csv_path}")
    else:
        print(f"{csv_filename} not found in the folder.")

def clear_temp_files():
    if os.path.exists(temp_path):
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file {item}")
                elif os.path.isdir(item_path):
                    os.rmdir(item_path)
                    print(f"Deleted directory {item}")
            except Exception as error:
                print(f"Could not delete {item}: {error}")
        print("Temporary files cleared.")
    else:
        print("Temp folder not found.")

def menu():
    while True:
        print("\nSelect an option:")
        print("1. Sort files in 'Module 7'")
        print("2. Clean CSV file in 'Module 7'")
        print("3. Remove temporary files in 'Module 7/temp'")
        print("4. Exit")

        option = input("Your choice (1/2/3/4): ")

        if option == '1':
            file_sort()
        elif option == '2':
            csv_name = input("Enter the CSV filename (with extension): ")
            clean_csv(csv_name)
        elif option == '3':
            clear_temp_files()
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    menu()