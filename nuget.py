# This is a script that will scan a directory for Fornite and delete it.
try:
    import os
    import string
    import sys
except ImportError:
    sys.exit("Code: 4440")
cancer = "Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe"

# Check if the directory exists from A to Z
for drive_letter in string.ascii_uppercase:
    potential_path = f"{drive_letter}:\\{cancer}"
    if os.path.exists(potential_path):
        print(f"Found Fortnite at {potential_path}")
        print("Deleting...")
        os.remove(potential_pat)
        print("Deleted Fortnite.")
        print("Code: 4441")
        break
else:
    print("Fortnite not found.")
    print("Code: 4442")
