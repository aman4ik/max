
import os
import re


class Library:
    __secret_key = os.environ.get("SECRET_LIB_KEY")
    __book_list = ["Идиот", "Подросток", "Робинзон Крузо", "Маленький принц"]

    @classmethod
    def get_books(cls):
        if cls.__secret_key is not None:
            return cls.__book_list
        else:
            raise Exception("Forbidden action")

    @classmethod
    def change_key(cls, new_key):
        cls.__secret_key = new_key

    @classmethod
    def get_secret_key(cls):
        return cls.__secret_key

    @classmethod
    def give_book(cls, book_name):
        if cls.__secret_key is not None and book_name in cls.__book_list:
            cls.__book_list.remove(book_name)
            return cls.__book_list
        else:
            print(f"Can't give this book {book_name} to you")
    @classmethod
    def check_student_key(cls, pub_key):
        try:
            pattern = r"\d{2}\w+-\w\d\w\d-\d{3}\w\d\w"
            found = re.findall(pattern, pub_key)
            if len(found) > 0:
                print("Success")
            else:
                print("Incorrect Pub key")
        except:
            raise Exception("Error")



student_key = os.environ.get('STUDENT_PUB_KEY')
Library.check_student_key(student_key)

print("File loaded")

# Library.change_key("new password")
# print(Library.get_secret_key())
# print(Library.get_books())
# num = random.randint(0, 3)
# book_name = Library.get_books()[num]
#
# Library.give_book(book_name)
# print(Library.get_books())