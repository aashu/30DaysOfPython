import random
import string

def random_user_id(length=6):
    '''
    generate a 6 digit random id. id may contain uppercase,lowercase,punctuations and digits.
    '''
    sample = string.ascii_letters + string.digits + string.punctuation
    user_id = ''
    for count in range(length):
        user_id += random.choice(sample)
    return user_id

def user_generated_uid():
    '''
    takes input from user for id length and number of ids to generate
    '''
    id_length = int(input('enter user id length: '))
    number_of_ids = int(input('number of ids to be generated: '))
    ids = []
    for count in range(number_of_ids):
        ids.append(random_user_id(id_length))
    return ids

def generate_colour(code_type='hex'):
    '''
    generate a valid color value either in hex or rgb
    '''
    if code_type == 'hex':
        valid_hex = list(range(10))
        valid_hex.extend(string.ascii_uppercase[:6])
        hex_code = ''.join(str(e) for e in random.sample(valid_hex,6))
        color = f'{hex_code}'
        return color
    elif code_type == 'rgb':
        color = f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})'
        return color
