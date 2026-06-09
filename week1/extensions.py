import sys

file = input("File name: ").lower().replace(" ", "")
if "." not in file:
    print("application/octet-stream")
    sys.exit()
file_type = file.rsplit('.', 1)[1]

if file_type == "gif" or file_type == "jpeg" or file_type == "png":
    print(f"image/{file_type}")
elif file_type == "jpg":
    print("image/jpeg")
elif file_type == "pdf" or file_type == "zip":
    print(f"application/{file_type}")
elif file_type == "txt":
    print(f"text/plain")
else:
    print("application/octet-stream")