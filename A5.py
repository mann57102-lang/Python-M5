# Create Class
class Student:

    # Initializing
    def __init__(self):
        print('Student object created')

    # Calling destructor
    def __del__(self):
        print("Destructor executed")


def make_object():
    print('Creating Object...')
    
    student_obj = Student()
    
    print('Function completed...')
    
    return student_obj


print('Calling make_object() function...')

result = make_object()

print('Program Finished...')
