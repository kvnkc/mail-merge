with open('./input/names/invited_names.txt') as names:
    names = names.readlines()

with open('./input/letters/starting_letter.txt') as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace('[name]', stripped_name)
        with open(f'./output/readytosend/letter_for_{stripped_name}.txt', mode='w') as outgoing:
            outgoing.write(new_letter)
