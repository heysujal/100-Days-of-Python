# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
all_letters = []
with open("Input/Names/invited_names.txt") as names:
    response = names.readlines()
    names_list = [x.replace('\n', '') for x in response]

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_body = starting_letter.read()
for member in names_list:
    temp = letter_body
    temp = temp.replace("[name]", f"{member}")
    all_letters.append(temp)

    # print(starting_letter.tell())
    # starting_letter.seek(0)
    # letter_body = starting_letter.read()
    # print(starting_letter.tell())
    # letter_body = letter_body.replace("[name]", f"{member}")
    # print(letter_body)
i = 0
for name in names_list:
    print(name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as final:
        final.write(all_letters[i])
    i += 1
