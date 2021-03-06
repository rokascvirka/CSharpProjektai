
def personal_code_lenght_checker(person_code_param):
    person_code_param = str(person_code_param)
    return len(person_code_param) == 11

def is_entered_personal_code_is_number(person_code_param):
    person_code_param = str(person_code_param)
    for x in range(len(person_code_param)):
        if(ord(person_code_param[x]) < 48 or ord(person_code_param[x]) > 57): 
            return False
            
    return True

def get_birth_date_from_personal_code(person_code_param):
    return person_code_param[0:7] 

def is_last_number_is_exeption_for_no_birth_date(person_code_param):
    birth_date = get_birth_date_from_personal_code(person_code_param)
    if birth_date[1:3] == "00" or birth_date[3:5] == "00":
        return True
    return False

def is_personal_code_exeptional(person_code_param):
    return person_code_param[0] == '9'

def is_entered_personal_code_first_number_valid(person_code_param):
    first_number_list = ["1", "2", "3", "4", "5", "6", "9"]
    first_number = person_code_param[0]
    if first_number in first_number_list:
        return True
    return False

def what_year_is_it(person_code_param):
    year = 5
    birth_date = get_birth_date_from_personal_code(person_code_param)
    input_first_number = birth_date[0]
    if input_first_number == '1' or input_first_number == '2':
        year = "18" + str(birth_date[1:3])
    if input_first_number == '3' or input_first_number == '4':
        year = "19" + str(birth_date[1:3])
    if input_first_number == '5' or input_first_number == '6':
        year = "20" + str(birth_date[1:3])
    return int(year)

def is_entered_personal_code_is_leaf_year(person_code_param):
    year = what_year_is_it(person_code_param)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def is_entered_personal_code_month_is_in_range(person_code_param):
    birth_date = get_birth_date_from_personal_code(person_code_param)
    month = birth_date[3:5]
    month = int(month)
    if 0 < month < 13:
        return True 
    if is_personal_code_exeptional(person_code_param) == True:
        return True
    if is_last_number_is_exeption_for_no_birth_date(person_code_param) == True:
        return True 
    return False

def is_entered_personal_code_day_is_in_range(person_code_param):
    birth_date = get_birth_date_from_personal_code(person_code_param)
    days_in_month_list_leaf = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = birth_date[5:7]
    days = int(days)
    month = birth_date[3:5] 
    month = int(month)
    if is_entered_personal_code_is_leaf_year(person_code_param) == True:
        if days <= days_in_month_list_leaf[month - 1]:
            return True
    if days <= days_in_month_list[month - 1]:
        return True 
    if is_personal_code_exeptional(person_code_param) == True:
        return True
    return False

def is_last_number_of_personal_code_is_legit(person_code_param):
    input_last_number = person_code_param
    last_number = ((int(input_last_number[0]) * 1 + int(input_last_number[1]) * 2 + int(input_last_number[2]) * 3 + int(input_last_number[3]) * 4 + int(input_last_number[4]) * 5 +
                  int(input_last_number[5]) * 6 + int(input_last_number[6]) * 7 + int(input_last_number[7]) * 8 + int(input_last_number[8]) * 9 + int(input_last_number[9]) * 1)  % 11)
    if last_number == 10:
        last_number = ((int(input_last_number[0]) * 3 + int(input_last_number[1]) * 4 + int(input_last_number[2]) * 5 + int(input_last_number[3]) * 6 + int(input_last_number[4]) * 7 
                       + int(input_last_number[5]) * 8 + int(input_last_number[6]) * 9 + int(input_last_number[7]) * 1 + int(input_last_number[8]) * 2 + int(input_last_number[9]) * 3) % 11)
        if last_number == 10:
            last_number = 0 
    if int(input_last_number[10]) == last_number:
        return True 
    if is_personal_code_exeptional(person_code_param) == True:
        return True
    return False 
    
def is_person_isnt_too_old(person_code_param):
    year = what_year_is_it(person_code_param)
    if year > 1890:
        return True 
    return False

def is_person_isnt_too_young(person_code_param):
    year = what_year_is_it(person_code_param)
    if year < 2023:
        return True
    return False

def verify_personal_code(personal_code):
    if personal_code == None:
        return "Input can not be empty"
    if personal_code == "":
        return "Input can not be empty"

    personal_code = str(personal_code)
    input = "".join(personal_code.split())
    if personal_code != input:
        return "Personal code should be written without spaces"

    if personal_code_lenght_checker(input) == False:
        return "Personal code is too short or too long."
    if is_entered_personal_code_is_number(input) == False:
        return "Personal code has unexpected symbols. It must be a number."
    if is_entered_personal_code_first_number_valid(input) == False:
        return "Personal code first number is incorrect."
    if is_entered_personal_code_month_is_in_range(input) == False:
        return "Personal code month is not in range."
    if is_entered_personal_code_day_is_in_range(input) == False:
        return "Personal code day is not in range."
    if is_last_number_of_personal_code_is_legit(input) == False:
        return "Personal code is invalid. Last number is not comfirmed."
    if is_person_isnt_too_old(input) == False:
        return "There is no human alive that old..."
    if is_person_isnt_too_young(input) == False:
        return "Come back after your birthday..."

    return "valid"

#tests

if  verify_personal_code(None) == "valid":
    print("Personal code input can not be None.")
if  verify_personal_code("") == "valid":
    print("Personal code input can not be empty.")
if  verify_personal_code("3 9 6 0124 00 40") == "valid": #Logika is not found. Ar reiktu tikrint FALSE?
    print("Method join does not work.")
if  verify_personal_code("396012400400") == "valid":
    print("Personal code lenght checker is not working.")
if  verify_personal_code("3960124004") == "valid":
    print("Personal code lenght checker is not working.")
if  verify_personal_code("LT396012400") == "valid":
    print("Personal code symbol checker does not work.")
if  verify_personal_code("79601240040") == "valid":
    print("Personal code first symbol checker does not work.")
if  verify_personal_code("39615240040") == "valid":
    print("Personal code month checker does not work.")
if  verify_personal_code("39600240046") == False:
    print("Personal code month checker does not work. If someone doesn't know birth month case.")
if  verify_personal_code("99600240040") == False:
    print("Personal code month checker does not work. If code starts with 9 case.")
if  verify_personal_code("39601000044") == False:
    print("Personal code day checker does not work. If someone does't know birth day case.")
if  verify_personal_code("39601400040") == "valid":
    print("Personal code day checker does not work. Leaf year case.")
if  verify_personal_code("39602290047") == False:
    print("Personal code day checker does not work. Leaf year case.")
if  verify_personal_code("99601400040") == False:
    print("Personal code day checker does not work. If code starts with 9 case.")
if  verify_personal_code("39601240043") == "valid":
    print(f"Personal code last number checker does't work. ")
if  verify_personal_code("17901240040") == "valid":
    print("Person is too old")
if  verify_personal_code("27901240040") == "valid":
    print("Person is too old")
if  verify_personal_code("59601240040") == "valid":
    print("Person is too young")
if  verify_personal_code("69601240040") == "valid":
    print("Person is too young")

print("All tests passed")



