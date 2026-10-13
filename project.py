import re, math, secrets, string, sys

common = ["password","123456","12345678","qwerty","abc123","admin","aa123456","11111111"]

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "generate":
        print(generate())
        sys.exit()

    password = input("Password: ").strip()
    entropy = cal_entr(password)
    score  = get_score(password)
    if is_common(password):
        crack_time = "instantly"
    else:
        crack_time = evaluate_crack_time(entropy)

    print(f"Assessment: {score}/5 {evaluate_strength(score)}")
    print(f"Entropy: {entropy} bit")
    print(f"Crack time: {crack_time}")
    for tip in get_tips(password):
        print(tip)

def cal_entr(password): # Calculates entropy in bits
    p = 0
    if re.search(r"[a-z]", password): # Checks for the presence of lowercase letters
        p = p + 26
    if re.search(r"[A-Z]", password): # Checks for the presence of uppercase letters
        p = p + 26
    if re.search(r"\d", password): # Checks for the presence of digits
        p = p + 10
    if re.search(r"[^a-zA-Z\d]", password): # Checks for the presence of special symbols
        p = p + 33
    if p == 0:
        return 0 # Returns 0 if there are no matches
    return round(len(password) * math.log2(p), 1) # Formula: length * log2(size of the character pool)

def is_common(password):
    # Checks whether the password is in
    # the list of popular passwords
    return password.lower() in common

def get_score(password):
    if is_common(password):
        return 0
    entr = cal_entr(password)
    # Each threshold is a minimum entropy needed to earn one point
    # sum() counts the number of 'True'
    return sum(entr >= threshold for threshold in (28,36,60,80,100))

def evaluate_strength(score):
    # Evaluates the password reliabiliyy based
    # on the number of points
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Mid"
    return "Strong"

def evaluate_crack_time(entr):
    if entr > 200: # To avoid float overflow due to very long passwords
        return "practically an eternity"

    # '2**entr' is the total number of possible passwords
    # '1e10' - assumed cracker speed
    # dividing by '1e10' gives the time to try all of them
    # dividing by 2 gives the average since the cracker finds the
    # password halfway
    sec = (2**entr) / 1e10 / 2

    if sec < 1:
        return "instantly"

    un = [("years", 31_536_000), ("days", 86_400), ("hours", 3600), ("minutes", 60)]
    for n, s in un:
        if sec >= s:
            return f"~{sec / s:,.0f} {n}"
    return f"~{sec:.0f} seconds"

def get_tips(password):
    # Returns the list of tips
    tips_list = []
    if len(password) < 16:
        tips_list.append("At least 16 characters")
    if not re.search(r"[a-z]", password):
        tips_list.append("Add a lowercase letter")
    if not re.search(r"[A-Z]", password):
        tips_list.append("Add a uppercase letter")
    if not re.search(r"\d", password):
        tips_list.append("Add a digit")
    if not re.search(r"[^a-zA-Z\d]", password):
        tips_list.append("Add a special symbol")
    return tips_list

def generate():
    alpha = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(secrets.choice(alpha) for _ in range(16))
        if not get_tips(password):
            return password

if __name__ == "__main__":
    main()