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