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
    if 10 <= num < 20:
        return create_teens(num)
    if 20 <= num < 30:
        tmp = create_ones(num - 20)
        return "twenty-" + tmp
    if 30 <= num < 40:
        tmp = create_tens(num - 30)
        return "thirty-" + tmp
    if 40 <= num < 50:
        tmp = create_tens(num - 40)
        return "forty-" + tmp
    if 50 <= num < 60:
        tmp = create_tens(num - 50)
        return "fifty-" + tmp
    if 60 <= num < 70:
        tmp = create_tens(num - 60)
        return "sixty-" + tmp
    if 70 <= num < 80:
        tmp = create_tens(num - 70)
        return "seventy-" + tmp
    if 80 <= num < 90:
        tmp = create_tens(num - 80)
        return "eighty-" + tmp
    if 90 <= num < 100:
        return "ninety-" + tmp
    
