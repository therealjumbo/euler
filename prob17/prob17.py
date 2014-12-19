def count_number_len(num_str):
    num_str = num_str.replace(" ", "")
    num_str = num_str.replace("-", "")

    return len(num_str)

def create_ones(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    else:
        raise LookupError()

def create_tens(num):
    if num < 10:
        return create_ones(num)

    if 10 <= num < 20:
        return create_teens(num)

    elif 20 <= num < 30:
        if num == 20:
            return "twenty"
        else:
            tmp = create_ones(num - 20)
            return "twenty-" + tmp

    elif 30 <= num < 40:
        if num == 30:
            return "thirty"
        else:
            tmp = create_ones(num - 30)
            return "thirty-" + tmp
    
    elif 40 <= num < 50:
        if num == 40:
            return "forty"
        else:
            tmp = create_ones(num - 40)
            return "forty-" + tmp
    
    elif 50 <= num < 60:
        if num == 50:
            return "fifty"
        else:
            tmp = create_ones(num - 50)
            return "fifty-" + tmp
    
    elif 60 <= num < 70:
        if num == 60:
            return "sixty"
        else:
            tmp = create_ones(num - 60)
            return "sixty-" + tmp

    elif 70 <= num < 80:
        if num == 70:
            return "seventy"
        else:
            tmp = create_ones(num - 70)
            return "seventy-" + tmp
    
    elif 80 <= num < 90:
        if num == 80:
            return "eighty"
        else:
            tmp = create_ones(num - 80)
            return "eighty-" + tmp
    
    elif 90 <= num < 100:
        if num == 90:
            return "ninety"
        else:
            tmp = create_ones(num - 90)
            return "ninety-" + tmp
    
    else:
        raise LookupError()
    
def create_teens(num):
    if num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "nineteen"
    else:
        raise LookupError()

def create_hundreds(num):
    if num < 100:
        return create_tens(num)

    elif 100 <= num < 200:
        if num == 100:
            return "one hundred"
        else:
            tmp = create_tens(num - 100)
            return "one hundred and " + tmp

    elif 200 <= num < 300:
        if num == 200:
            return "two hundred"
        else:
            tmp = create_tens(num - 200)
            return "two hundred and " + tmp

    elif 300 <= num < 400:
        if num == 300:
            return "three hundred"
        else:
            tmp = create_tens(num - 300)
            return "three hundred and " + tmp

    elif 400 <= num < 500:
        if num == 400:
            return "four hundred"
        else:
            tmp = create_tens(num - 400)
            return "four hundred and " + tmp

    elif 500 <= num < 600:
        if num == 500:
            return "five hundred"
        else:
            tmp = create_tens(num - 500)
            return "five hundred and " + tmp

    elif 600 <= num < 700:
        if num == 600:
            return "six hundred"
        else:
            tmp = create_tens(num - 600)
            return "six hundred and " + tmp

    elif 700 <= num < 800:
        if num == 700:
            return "seven hundred"
        else:
            tmp = create_tens(num - 700)
            return "seven hundred and " + tmp

    elif 800 <= num < 900:
        if num == 800:
            return "eight hundred"
        else:
            tmp = create_tens(num - 800)
            return "eight hundred and " + tmp

    elif 900 <= num < 1000:
        if num == 900:
            return "nine hundred"
        else:
            tmp = create_tens(num - 900)
            return "nine hundred and " + tmp

    else:
        raise LookupError()

total = 0
thous = "one thousand"
total = count_number_len(thous)

for i in range(1, 1000):
    tmp = create_hundreds(i)
    total += count_number_len(tmp)

print(total)
