# File Creation:

def create_file():
    try:
        # Creates a new text file named "my_file.txt" in write mode ('w').

        with open('my_file.txt', 'w') as file:

            # Write at least three lines of text to the file, including a mix 

            file.write("This is the first line.\n")
            file.write("Here's a number: 1234\n")
            file.write("And another line with some text.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Reading and Display:

def read_file():
    try:
        # Read the contents of the my_file.txt
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found: Ensure the file exists before trying to read.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Appending:

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:

            # Append three additional lines of text to the existing content.

            file.write("Appending the first additional line.\n")
            file.write("Appending another line with a number: 67890\n")
            file.write("Appending a final line of text.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("File not found: Ensure the file exists before trying to append.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  

if __name__ == "__main__":
    main()