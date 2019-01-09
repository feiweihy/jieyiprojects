import binascii,datetime,random


# Convert bytes to string
def bytes2hex_str(self):
    return binascii.b2a_hex(self).decode()


# Convert string to bytes
def hex_str2bytes(self):
    return binascii.a2b_hex(self)


# Function for string left zeros
def add_left0(self, length):
    return self.zfill(length)


# Function for string right zeros
def add_right0(self, length):
    self_len = len(self)
    return_str = self+''
    for i in range(length-self_len):
        return_str += '0'
    return return_str


# Function for string right spaces
def add_right_space(self, length):
    self_len = len(self)
    return_str = self+''
    for i in range(length-self_len):
        return_str += ' '
    return return_str


# Function for string left or right spaces
# left_or_right-0，左边补；1-右边补
def add_str_as_some_multiple(self, left_or_right, length, add_str):
    self_len = len(self)
    return_str = self+''
    remainder = self_len % length
    for i in range(length-remainder):
        if left_or_right == 0:
            return_str = add_str+return_str
        else:
            return_str = return_str+add_str
    return return_str


# get a random str,the length must be larger than 17
def get_random_str_according_datetime(length, number_flag):
    today = datetime.datetime.now()
    today_str = datetime.datetime.strftime(today, "%Y%m%d%H%M%S")
    char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(length-len(today_str)):
        if number_flag == 0:
            today_str += str(random.randint(0, 9))
        else:
            today_str += random.choice(char)
    return today_str


# right space for bytes length
def add_right_space_for_bytes(self, charset, length):
    return_str = self + ''
    return_str_bytes = return_str.encode(charset)
    for i in range(length-len(return_str_bytes)):
        return_str += ' '
    return return_str


# right space for bytes length
def reverse_str(self):
    return_str = '';
    self = self + '' if len(self)%2 == 0 else '0' + self
    self_bytes_len = len(self)
    for i in range(self_bytes_len//2):
        return_str += self[self_bytes_len-2-i*2:self_bytes_len-i*2]
    return return_str


# right space for bytes length
def str_xor_str(str1, str2):
    if len(str1) != len(str2):
        return 'ERR1'
    if len(str1) % 2 != 0:
        return 'ERR2'
    bytes_new = b''
    for i in range(len(str1)//2):
        xor_result = (binascii.a2b_hex(str1[i * 2:(i + 1) * 2])[0]^binascii.a2b_hex(str2[i * 2:(i + 1) * 2])[0])
        bytes_new += bytes([xor_result])
    return_str = bytes2hex_str(bytes_new)
    return return_str


if __name__ == '__main__':
    print(hex_str2bytes("313233"))
    print(bytes2hex_str(hex_str2bytes("313233")))
    print(add_left0("111", 10))
    print(add_right0("111", 10))
    print(add_right_space("111", 10))
    print(add_str_as_some_multiple("111", 0, 10, 'F'))
    print(add_str_as_some_multiple("111", 1, 20, 'F'))
    print(get_random_str_according_datetime(32, 0))
    print(get_random_str_according_datetime(32, 1))
    print(add_right_space_for_bytes('', 'GBK', 10))
    print(add_right_space_for_bytes('牛', 'GBK', 10))
    print(reverse_str('112233445566'))
    print(reverse_str('11223344556'))
    print(str_xor_str('112233445566','665544332211'))
