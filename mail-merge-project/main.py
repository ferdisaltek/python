
from dataclasses import replace
from logging import PlaceHolder


PlaceHolder="[name]"

with  open("C:/python_learn/python/mail-merge-project/Input/Names/invited_names.txt","r") as name_files:
    names=name_files.readlines()
    #print(names)


with open("C:/python_learn/python/mail-merge-project/Input\Letters/starting_letter.txt") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        strip_name=name.strip()
        new_letter=letter_content.replace(PlaceHolder,strip_name)
        with open(f"C:/python_learn/python/mail-merge-project/Output/ReadyToSend/letter_for_{strip_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
