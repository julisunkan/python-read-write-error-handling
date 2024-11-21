//File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
//The program will:
//Read the content of an existing file.
//Modify the content (e.g., convert all text to uppercase).
//Write the modified content to a new file.

# File Read & Write Challenge

def modify_file_content(input_file, output_file):
    try:
        # Open the file for reading
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content successfully modified and saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: Unable to read/write to the file. {e}")

# Example usage
modify_file_content("input.txt", "output.txt")


//Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
//This program will:
//Prompt the user for a filename.
//Try to open and read the file.
//Handle errors if the file doesn’t exist or can’t be read.

# Error Handling Lab

def read_user_file():
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: Unable to read the file. {e}")

# Example usage
read_user_file()
