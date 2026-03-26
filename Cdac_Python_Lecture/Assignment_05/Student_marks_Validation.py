marks_list = []

for i in range(5):

    try:
        marks = float(input("Enter the marks of student: "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks should be in range of 0 to 100")

    except ValueError as ve:
        print("Invalid Input:", ve)

    except Exception as e:
        print("Please Enter Numeric values!!")

    else:
        marks_list.append(marks)
        print("Marks are added successfully")

    finally:
        print("Attempt Completed\n")

print("Final Valid marks:", marks_list)