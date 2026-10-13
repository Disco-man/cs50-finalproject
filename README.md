# PASSWORD AND ENTROPY
## Name: Rassul
## Surname: Mamraikhan
## edX username: r-mamraikhan
## GitHub username: Disco-man
## City: Kyzylorda
## Country: Kazakhstan
### Video Demo:  https://youtu.be/u6koTbO4OX0?si=JGFOZtLLJ6w4tJv8
### Date of Video Recording: 09-27-2026
### Description:
This program calculates the level of password reliability entered by the user and evaluates it based on the entropy of the password. Password entropy is a mathematical measurement of how unpredictable a password is, expressed in bits. In addition, the program helps to generate a strong password for the user.

### Functions:
`cal_entr(password)`: This function calculates the entropy in bits using the formula: length * log2(size of the character pool). The size of the pool depends on the presence of certain characters. For example, the inclusion of a lowercase character in the password adds 26 to the pool, because there are 26 lowercase letters in the English alphabet. If the pool value has not been changed, it returns 0.

`is_common(password)`: Checks whether the password is in the list of popular passwords, which includes such passwords as "password","123456","12345678","qwerty" and others. Then it returns True/False

`get_score(password)`: Returns a score from 0 to 5. The password gets one point for each entropy threshold it reaches (28,36,60,80,100). The threshold is a set of approximate bit values ​​required for a password to be considered good.

`evaluate_strength(score)`: Evaluates the password reliabiliyy based on the number of points. "Weak" if score <= 2; "Mid" if score <= 4; "Strong" if score == 5

`evaluate_crack_time(entr)`: Calculates the average password cracking time using password entropy. It assumes an attacker can make 10 billion guesses per second (1e10). The number of possible passwords is '2 ** entropy', and dividing this by the guessing speed gives you time to try each combination. Dividing by 2 accounts for the fact that, on average, the correct password is found halfway. The result is then converted from seconds to the largest valid unit (years, days, hours, or minutes)

`get_tips(password)`: Returns the list of tips. The tip gives an information about what the password is missing. For example, it will display "Add a lowercase letter" if the password lacks lowercase letters.

`generate()`: Creates a random 16-character password with the 'secrets' module and repeats until the password has no tips. Characters taken from the full set of ASCII letters, digits, and special symbols

### Libraries:
`re` - used to find patterns in the password - whether there is a lowercase letter, capital letter, number or special character (re.search (r "[a-z]," password)).

`math` - to use mathematical functions like 'math.log2()'

`secrets` - to generate cryptographically strong random values. Used in generate () to select random characters for a new password. Unlike random, secrets takes randomness from the source of the operating system

`string` - used to create ready-made constants with character sets: string.ascii_letters (letters), string.digits (numbers), string.punctation (special characters). Used in generate () to avoid manual writing

`sys` - accessing command line arguments through sys.argv. Used in main() to check if the program is runned with 'generate' argument. 'sys.exit()' is used to stop the program

`pytest` - used to run test suite

### Files:
`project.py` - main program code

`test_project.py` - a set of tests to check the functionality of the program

`requirements.txt` - libraries used in the program. Can be downloaded using `pip install -r requirements.txt`

