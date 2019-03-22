import com.jieyi.util.StringUtil as StringUtil

import sys

print(sys.path)

if __name__ == '__main__':
    # StringUtil测试
    print(StringUtil.hex_str2bytes("313233"))
    print(StringUtil.bytes2hex_str(StringUtil.hex_str2bytes("313233")))
    print(StringUtil.add_left0("111", 10))
    print(StringUtil.add_right0("111", 10))
    print(StringUtil.add_right_space("111", 10))
    print(StringUtil.add_str_as_some_multiple("111", 0, 10, 'F'))
    print(StringUtil.add_str_as_some_multiple("111", 1, 20, 'F'))
    print(StringUtil.get_random_str_according_datetime(32, 0))
    print(StringUtil.get_random_str_according_datetime(32, 1))
    print(StringUtil.add_right_space_for_bytes('', 'GBK', 10))
    print(StringUtil.add_right_space_for_bytes('牛', 'GBK', 10))
    print(StringUtil.reverse_str('112233445566'))
    print(StringUtil.reverse_str('11223344556'))
    print(StringUtil.str_xor_str('112233445566', '665544332211'))
