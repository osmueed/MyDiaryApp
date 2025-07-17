# main.py

from diary import save_entry, show_entries

def main():
    print("=== Welcome to Your Diary App ===")
    while True:
        print("\nChoose an option:")
        print("1. Add new entry")
        print("2. Show all entries")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            text = input("Write your diary entry: ")
            save_entry(text)
            print("Entry saved!")
        elif choice == '2':
            show_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
