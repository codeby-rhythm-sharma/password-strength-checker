import string

def check_strength(p):
    score = 0
    if any(c.islower() for c in p): score += 1
    if any(c.isupper() for c in p): score += 1
    if any(c.isdigit() for c in p): score += 1
    if any(c in string.punctuation for c in p): score += 1
    if len(p) >= 8: score += 1

    if score <= 2: return "Weak Password 😢"
    if score == 3: return "Moderate Password 🙂"
    return "Strong Password 🔥"

password = input("Enter password: ")
print(check_strength(password))
