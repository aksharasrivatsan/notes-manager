def add_note():
    note = input("Enter your note: ")
    with open("notes/notes.txt","a") as f:
        f.write(note+"\n")
    print("Note added successfully!")

if __name__ == "__main__":
    add_note()
    