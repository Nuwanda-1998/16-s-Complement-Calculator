# This is program will calculate the 16s Complement of hexadecimal numbers.

def splitnumber(hex_num):
    """
    Spliting the number to list for calculating
    each individual
    """
    return [num for num in hex_num]

def numletter(hex_number):
    """
    convert numbers to their letters in hex
    """
    hex_num = int(hex_number)
    if hex_num > 9:
        conv_dic = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F',
        }
        return conv_dic[hex_num]
    else:
        return hex_num


def letternum(hex_num):
    """
    convert letter to their number in decimal
    """
    if not hex_num.isnumeric():
        conv_dic = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
        }
        return conv_dic[hex_num]
    else:
        return hex_num

def complementcalculator(num_list):
    """
    Calculating the 16s complement
    """
    final_number = []
    last_number_index = (len(num_list) - 1)
    for index, num in enumerate(num_list):
        if index == last_number_index:
            if num.isnumeric():
                int_num = int(num)
                number = ((15-int_num)+1)
                final_number.append(number)
            else:
                lettonum = letternum(num)
                int_num = lettonum
                number = ((15-int_num)+1)
                final_number.append(number)
        else:
            if num.isnumeric():
                int_num = int(num)
                number = (15-int_num)
                final_number.append(number)
            else:
                lettonum = letternum(num)
                int_num = lettonum
                number = (15-int_num)
                final_number.append(number)
    return final_number


hex_number = input('enter number to calculate 16s comp: ')
num_list = splitnumber(hex_number)

numii= complementcalculator(num_list)
print('this is the final result {} '.format(numii))




# print('this is the equvilant number to the letter {} '.format(lettonum))
        
