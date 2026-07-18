import hashlib

file_path = input("Enter file path: ").strip('"')

try:
    with open(file_path, "rb") as file:
        file_data = file.read()
        hash_object = hashlib.sha256(file_data)
        file_hash = hash_object.hexdigest()

    print("SHA-256 Hash:", file_hash)

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("Error:", e)