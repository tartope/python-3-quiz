from ValidationException import ValidationException

def validate_file(file_path):
    with open(file_path, "r") as file:
        next(file)
        for lines in file:
            line = lines.split(',')
            # print(line)
            f_name = line[0]
            # print(f_name)
            try:
                f_name.isalpha()
            except:
                raise ValidationException(f"Invalid first name: '{f_name}'")
    # pass #TODO: Only add code inside this function.


def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
