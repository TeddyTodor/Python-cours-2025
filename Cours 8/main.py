def bitwiseOp (up_value, down_value, shift_value) :
    print(bin(up_value))
    print(bin(down_value))
    print(bin(up_value & down_value))
    print(bin(up_value | down_value))
    
    print(bin(up_value >> shift_value))
    print(bin(up_value << shift_value))