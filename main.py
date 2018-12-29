import random
defaultSpecials = "@%+/\\'!#$^?:.(){}[]~"


def GetRandCharacter(specials):
    """
    Get a random character that is either alphanumeric or one of the provided special characters

    :param specials: potentially empty string of special characters
    :return:
    """
    #Numbers: 0=48, 9=57    10
    #Upper: A=65, Z=90      26
    #Lower: a=97, z=122     26
    val = random.randint(0,61 + len(specials))
    if val < 10:
        # Then its a number
        return chr(val + 48)
    elif val < 36:
        # Then its an uppercase letter
        return chr(val + 65 - 10)
    elif val < 62:
        # Then its a lowercase letter
        return chr(val + 97 - 36)
    else:
        # Then its one of the special characters
        return specials[val - 62]


def GetStringLength():
    """
    Get length of string from user
    :return: integer
    """
    lengthInvalid = True
    stringLength = 0
    while lengthInvalid:
        try:
            stringLength = int(input("Enter the length of the randomly generated string: "))
            if stringLength < 1:
                print("You must enter a length greater than or equal to 1.")
                continue
            lengthInvalid = False
        except ValueError:
            print("You must enter an integer.")
        except:
            print("Something went wrong. Try again.")
    return stringLength


def GetSpecialCharacters():
    # Special characters
    inputCharacters = input("Enter any special characters (non alphanumeric) that may be included: ")
    inputCharacters.replace(' ', '')  # remove whitespace
    specialCharacters = ""
    duplicateCharacters = ""
    removedCharacters = ""
    for c in inputCharacters:
        if c.isalnum():
            removedCharacters = removedCharacters + c
        elif c in specialCharacters:
            duplicateCharacters = duplicateCharacters + c
        else:
            specialCharacters = specialCharacters + c

    if len(removedCharacters) > 0:
        print('Removed non-special characters: "%s"' % removedCharacters)
    if len(duplicateCharacters) > 0:
        print('Removed duplicate characters: "%s"' % duplicateCharacters)
    return specialCharacters


def NoSpecialCharacter(string, specialCharacters):
    for c in specialCharacters:
        if c in string:
            return False
    return True


def GetSpecialRequirement():
    while True:
        scRequired = input("Would you like to require the string to have one of these characters? (y/n): ")
        if scRequired.lower() == 'y' or scRequired.lower() == "yes":
            return True
        elif scRequired.lower() == 'n' or scRequired.lower() == "no":
            return False
        else:
            print("You must enter yes or no.")


stringLength = GetStringLength()

specials = input("Would you like to include special characters? (y/n): ") # if not y or yes defaults to no
specialCharacters = ''
specialCharRequired = False
if (specials.lower() == 'y') or  (specials.lower() == 'yes'):

    defaults = input("Would you like to use these default special characters: %s? (y/n): " % defaultSpecials)
    if (defaults.lower() == 'y') or (defaults.lower() == 'yes'):
        specialCharacters = defaultSpecials
    else:
        specialCharacters = GetSpecialCharacters()

    specialCharRequired = GetSpecialRequirement()

# Build String
randomString = ""
for i in range(stringLength):
    randomString = randomString + GetRandCharacter(specialCharacters)

if specialCharRequired and NoSpecialCharacter(randomString, specialCharacters):
    # Inject 1 special character in there
    sc = specialCharacters[random.randint(0,len(specialCharacters) - 1)]
    loc = random.randint(0, stringLength - 1)
    randomString = list(randomString)
    randomString[loc] = sc
    randomString = ''.join(randomString)

print(randomString)