dictionary = {

}


def main():
    while True:
        word = input("Слово для перевода")
        if word in dictionary:
            print(dictionary[word])
        else:
            print("Хотите добавить слово в словарь?")
        option = int(input("Выберите вариант "))
        if option == 1:
            translation = input(f"Введите перевод слова{word}")
            dictionary[word] = translation
        else:
            pass


main()
