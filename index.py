# file_handling_assignment.py

def create_file():
    try:
        # Create a new file in write mode
        with open('my_file.txt', 'w') as file:
            # Write lines to the file
            file.write("Hello, this is my first line.\n")
            file.write("This is line number 2, which includes a number: 42.\n")
            file.write("And here is line 3 with a float: 3.14.\n")
        print("File created and data written successfully.")

    except PermissionError:
        print("Error: You do not have permission to create this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    try:
        # Read the contents of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Contents of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append additional lines to the file
            file.write("This is an appended line 1.\n")
            file.write("Appended line 2: Everything is going well.\n")
            file.write("Final appended line 3: Goodbye!\n")
        print("Data appended successfully.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to append to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
