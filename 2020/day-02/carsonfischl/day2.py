file = open("./day2.txt", "r")
passwords = file.readlines()
all_passwords = 0

"""for password in passwords:
    counter = 0
    these_words = password.split()
    this_letter = list(these_words[1])
    this_letter = this_letter[0]
    guidelines = these_words[0].split("-")
    min_letters = guidelines[0]
    max_letters = guidelines[1]
    password_letters = these_words[2]
    print(password_letters)
    
    for letter in password_letters:
        if letter == this_letter:
            counter = counter + 1
    
    if(counter >= int(min_letters) and counter <= int(max_letters)):
        all_password_count = all_password_count + 1
                
print(all_password_count)"""

# part two
for password in passwords:
    these_words = password.split()
    this_letter = list(these_words[1])
    this_letter = this_letter[0]
    guidelines = these_words[0].split("-")
    first_index = int(guidelines[0]) - 1
    second_index = int(guidelines[1]) - 1
    password_letters = these_words[2]
    password_letters = list(password_letters)
    print(password_letters)
    
    if(first_index > len(password_letters)):
        pass
    if(second_index > len(password_letters)):
        if(password_letters[first_index] == this_letter):
            all_passwords = all_passwords + 1
            pass
    if(password_letters[first_index] == this_letter or password_letters[second_index] == this_letter):
        all_passwords = all_passwords + 1
    if(password_letters[first_index] == this_letter and password_letters[second_index] == this_letter):
        all_passwords = all_passwords - 1

                
print(all_passwords)