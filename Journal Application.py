import os
import datetime

class JournalEntry:
    def __init__(self, title, content, timestamp):
        self.title = title
        self.content = content
        self.timestamp = timestamp

class JournalApplication:
    def __init__(self):
        self.entries = []

    def add_entry(self, title, content):
        timestamp = datetime.datetime.now()
        entry = JournalEntry(title, content, timestamp)
        self.entries.append(entry)
        print("\nEntry added successfully.")

    def view_entries(self):
        if not self.entries:
            print("\nNo entries available.")
        else:
            print("\nJournal Entries:")
            for idx, entry in enumerate(self.entries, start=1):
                print(f"{idx}. {entry.title} - {entry.timestamp}")

    def search_entries(self, keyword):
        matching_entries = [entry for entry in self.entries if keyword.lower() in entry.title.lower() or keyword.lower() in entry.content.lower()]
        if not matching_entries:
            print("\nNo matching entries found.")
        else:
            print(f"\nMatching Entries for '{keyword}':")
            for idx, entry in enumerate(matching_entries, start=1):
                print(f"{idx}. {entry.title} - {entry.timestamp}")

    def delete_entry(self, entry_index):
        try:
            deleted_entry = self.entries.pop(entry_index - 1)
            print(f"\nEntry '{deleted_entry.title}' deleted successfully.")
        except IndexError:
            print("\nInvalid entry index. Please enter a valid index.")

def main():
    journal_app = JournalApplication()

    while True:
        print("\nJournal Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entries")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter entry title: ")
            content = input("Enter entry content: ")
            journal_app.add_entry(title, content)

        elif choice == '2':
            journal_app.view_entries()

        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            journal_app.search_entries(keyword)

        elif choice == '4':
            index_to_delete = int(input("Enter the index of the entry to delete: "))
            journal_app.delete_entry(index_to_delete)

        elif choice == '5':
            print("Exiting the Journal Application.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
