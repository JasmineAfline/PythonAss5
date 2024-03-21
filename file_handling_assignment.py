try:
    # File Creation: Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Writing at least three lines of text to the file
        file.write("First line of text\n")
        file.write("Second line of text\n")
        file.write("12345\n")  # Writing a mix of strings and numbers

    # File Reading and Display: Reading the contents of "my_file.txt" and displaying them on the console
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending: Opening "my_file.txt" in append mode ('a') and appending three additional lines of text
    with open("my_file.txt", 'a') as file:
        file.write("Third line of text\n")
        file.write("Fourth line of text\n")
        file.write("54321\n")  # Appending a mix of strings and numbers

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    try:
        # Reading the contents of "my_file.txt" and displaying them on the console
        with open("my_file.txt", 'r') as file:
            print("\nUpdated contents of my_file.txt:")
            print(file.read())
    except Exception as e:
        print("An error occurred while reading the file:", e)

