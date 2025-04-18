def has_min_length(password):
    return len(password) >= 8

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_characters = "!@#$%^&*"
    return any(char in special_characters for char in password)

def check_password_strength(password):
    # Run each check
    check_results = [has_min_length(password), has_lowercase(password), has_uppercase(password), has_digit(password), has_special_char(password)]

# Count passed checks
    passed_checks = sum(check_results)

    # Strength
    if passed_checks == 5:
        strength = "Strong"
    elif 3 <= passed_checks < 5:
        strength = "Medium"
    else:
        strength = "Weak"
        
    # Feedback for what’s missing
    feedback = []

    if not has_min_length(password):
        feedback.append("Password should be at least 8 characters long.")
    if not has_lowercase(password):
        feedback.append("Password should include at least one lowercase.")
    if not has_uppercase(password):
        feedback.append("Password should include at least one uppercase.")
    if not has_digit(password):
        feedback.append("Password should include at least one digit.")
    if not has_special_char(password):
        feedback.append("Password should include at least one special character (!@#$%^&*).")

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)
    if strength != "Strong":
        print("\nSuggestions to improve your password:")
        for i in feedback:
            print(i)


if __name__ == "__main__":
    main()
