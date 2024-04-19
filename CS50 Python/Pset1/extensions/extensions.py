# Get user input
filename = input("Name of the file: ")

# Remove spaces and make it all lower
new_filename = filename.lower().strip()

# Check types
if new_filename.endswith(".gif"):
    print("image/gif")
elif new_filename.endswith(".jpg"):
    print("image/jpg")
elif new_filename.endswith(".jpeg"):
    print("image/jpeg")
elif new_filename.endswith(".png"):
    print("image/png")
elif new_filename.endswith(".pdf"):
    print("application/pdf")
elif new_filename.endswith(".zip"):
    print("application/zip")
elif new_filename.endswith(".txt"):
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
