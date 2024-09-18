def write_to_file():
  try:
    # Open the file for writing
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's a line with a number: 42\n")
      file.write("And a final line for good measure.\n")
    print("Successfully wrote to my_file.txt")
  except PermissionError:
    print("Error: You don't have permission to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    # Ensure the file is closed even if an error occurs
    if file:
      file.close()

def read_and_display():
  try:
    with open("my_file.txt", "r") as file:
      content = file.read()
      print("Contents of my_file.txt:")
      print(content)
  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def append_to_file():
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending a new line.\n")
      file.write("Adding another line with some data: today's date is 2024-09-18.\n")
      file.write("This is the final line appended.\n")
    print("Successfully appended to my_file.txt")
  except PermissionError:
    print("Error: You don't have permission to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


write_to_file()
read_and_display()
append_to_file()
read_and_display()  