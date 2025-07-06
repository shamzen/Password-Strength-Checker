# SCT_CYBER 03 - Password Strength Checker

import re

def check_password_strength(password):
    # Rule 1: Length >= 8
    length_error = len(password) < 8

    # Rule 2: At least one lowercase letter
    lowercase_error = re.search(r"[a-z]", password) is None

    # Rule 3: At least one uppercase letter
    uppercase_error = re.search(r"[A-Z]", password) is None

    # Rule 4: At least one digit
    digit_error = re.search(r"\d", password) is None

    # Rule 5: At least one special character
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Calculate score: each passing rule adds 1 point
    passed_criteria = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Verdict
    if passed_criteria == 5:
        verdict = "Strong 💪"
    elif passed_criteria >= 3:
        verdict = "Moderate 🔑"
    else:
        verdict = "Weak ⚠️"

    # Print the report
    print("\n=== Password Strength Report ===")
    print(f"Length >= 8: {'✅' if not length_error else '❌'}")
    print(f"Contains lowercase: {'✅' if not lowercase_error else '❌'}")
    print(f"Contains uppercase: {'✅' if not uppercase_error else '❌'}")
    print(f"Contains digit: {'✅' if not digit_error else '❌'}")
    print(f"Contains special char: {'✅' if not special_char_error else '❌'}")
    print(f"Overall Verdict: {verdict}")

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
