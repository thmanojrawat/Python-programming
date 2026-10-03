# Logical operators with conditions

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")

is_student = True
has_library_card = False

if is_student or has_library_card:
    print("Library access available.")

if not has_library_card:
    print("Student does not have a library card.")
