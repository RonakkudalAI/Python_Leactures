class UnderAgeException(Exception):
    pass

class InvalidPercentageException(Exception):
    pass

class CourseNameBlankException(Exception):
    pass

try:
    Name = input("Enter the Student Name:")
    
    try:
        Age = int(input("Enter age"))
    except ValueError as ve:
        print("Invalid Values Enter!!",ve)   

    try:
        Percentage = float(input("Enter Percentage"))
    except ValueError as ve:
        print("Invalid Percentage Input!!")

    Course = input("Enter Course Name")


    if Age <16:
        raise UnderAgeException("You are small kids")

    if Percentage < 0 or Percentage > 100:
        raise InvalidPercentageException("Please Inser Correct Percentage")

    if Course.strip()=="":
        raise CourseNameBlankException("Course Name Can not be Blank:")
    
    print("Student Admission Confirmed")
    print(f"Name:{Name}")
    print(f"Age:{Age}")

except UnderAgeException as e:
    print("❌ UnderAge Error:", e)

except InvalidPercentageException as e:
    print("❌ Percentage Error:", e)

except CourseNameBlankException as e:
    print("❌ Course Error:", e)

except Exception as e:
    print("❌ General Error:", e)

finally:
    print("\n--- Admission Process Completed ---")
