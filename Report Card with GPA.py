def report_card():
    my_grades_list = []
    my_classes_list = []
    total = 0
    classes = int(input("How many classes did you take? "))
    for elements in range(classes):
        my_classes = input("Enter the courses name: ")
        grades = int(input("Enter your grades: "))
        my_grades_list.append(grades)
        my_classes_list.append(my_classes)
    print("--- PRINTING REPORT CARD ---")
    for i in range(classes):
            print(my_classes_list[i], '-->', my_grades_list[i])
    for contents in my_grades_list:
        total = total + contents
    print("**************")
    gpa = round(total/classes)
    print("Overall GPA:", gpa)
    print("**************")
    if gpa >= 90:
        print("Your Final Grade is A")
    elif gpa >= 80 < 90:
        print("Your Final Grade is B")
    elif gpa >= 70 < 80:
        print("Your Final Grade is C")
    elif gpa < 70:
        print("Your Final Grade is D")


report_card()
