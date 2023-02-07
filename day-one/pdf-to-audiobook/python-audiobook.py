import pyttsx3
from pypdf import PdfReader


def menu():
    print("1. Convert pdf to audio book")
    print("0. Quit")
    option = int(input())
    return option


def text_to_speech(text, file_name, number):
    file_name = file_name[0:len(file_name)-4] + '-' + str(number) + ".mp3"

    print(file_name)

    engine = pyttsx3.init()
    engine.save_to_file(text, file_name)
    engine.runAndWait()


def read_pdf(file_name):
    reader = PdfReader(file_name)
    number_of_pages = len(reader.pages)
    for number in range(0, number_of_pages):
        page = reader.pages[number]
        text = page.extract_text()
        text_to_speech(text, file_name, number)


def logic(option):
    if option == 1:
        file_name = input("Enter file name with extension: ")
        read_pdf(file_name)
    else:
        print("Program interrupted...")



if __name__ == "__main__":
    response = menu()
    logic(response)
