import os
import random
def secure_delete(file_path, passes=3):
    if os.path.exists(file_path):
        try:
            with open(file_path,'ba+', buffering=0)as delfile:
                length = delfile.tell()
                for _ in range(passes):
                    delfile.seek(0)
                    delfile.write(random.randbytes(length))
            os.remove(file_path)
            print(f"{file_path} has been securly deleted.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("File does not exist.")
if __name__ == "__main__":
    file_to_delete = input("Enter the full path of the file to securely delete: ")
    secure_delete(file_to_delete)