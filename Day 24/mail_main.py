PLACEHOLDER = "[name]"

with open('./Day 24/Input/Names/invited_names.txt') as name_files:
    names = name_files.readlines()
    # print(names)

with open('./Day 24/Input/Letters/starting_letter.docx') as letter_file:
    letter = letter_file.read()
    # print(letter)

    for name in names:
        stripped_name=  name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        # writing to the new files that will be automatically created
        with open(f'./Day 24/Output/ReadyToSend/letter_for{stripped_name}.docx', mode='w') as completed_letter:
            completed_letter.write(new_letter)
        # print(new_letter)