try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["asd"])

except FileNotFoundError:
    file = open("a_file.txt",mode='w')
    file.write("Something")

except KeyError as error_msg:
    print(f"The Key {error_msg} does not exist")

finally:
    raise TypeError("This is error i made up")
