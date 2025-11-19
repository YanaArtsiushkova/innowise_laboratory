print("Welcom to the mini-profile generator")


def generate_profile(age):
    if 0 <= age <= 12:
        life_stage = "Child"
    elif 13 <= age <=19:
        life_stage = "Teenager"
    elif age >= 20:
        life_stage = "Adult"
    return life_stage


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
life_stage = generate_profile(current_age)
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)


user_profile = {"Name": user_name, "Age": current_age,
                "Life stage": life_stage,
                "Favorite Hobbies": hobbies}

print('---')
print(f'''Profile Summary:
Name: {user_profile["Name"]}
Age: {user_profile["Age"]}
Life Stage: {user_profile["Life stage"]}''')
if not hobbies:
    print("You didn't mention any hobbies")
else:
    print(f'Favorite Hobbies ({len(hobbies)}):')
    for hobby in hobbies:
        print(f'- {hobby}')
print("---")