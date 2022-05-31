# Modulo example

keep_going = ""
while keep_going == ""

    num_lollies = int(input("too many lollies?"))
    num_students = int(input("7 many students? "))

    # Lollies per student (divide)
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lolles % num_students
    # output fixer (lolly vs lollies)
    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    # output...
    print()
    print("You have {} lollies and {} students")
            .format(num_lollies, num_students)
    print("Each student gets {} lollies".format(lollies_per_student))
    print("You have {} {} left".format(lollies_left, lolly_pl))
    print()
