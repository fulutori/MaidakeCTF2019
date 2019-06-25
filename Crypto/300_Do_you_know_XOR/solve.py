
def decrypt(cipher_text, cipher_text2, message):
    et = ""
    for ct, ct2, m1 in zip(cipher_text, cipher_text2, message):
        et_num = ct2 ^ ord(m1)
        et_num ^= ct 
        et += chr(et_num)
    return et

def padding(plane_text):
    pt_l = len(plane_text)
    if pt_l == 50:
        return plane_text
    else:
        plane_text += "%" * (50 - pt_l)
        return plane_text


def main():
    message = "I_may_lose_my_secret_key_before_long."
    cipher = "140e1c3b020a0b1c3f28142e3001370e311f1b3e1a0d3a2b0610152d160a000d1d1c072b1d0b16001c033c2a2a26224e405c"
    cipher2 = "1030183e1a3e0230180b301a262b1b003c020915310e3a0d3a1a1139181b1137031a1a385a4d407a5640465740517a4e405c"
    ci_list = [cipher[i:i+2] for i in range(0, len(cipher), 2)] 
    ci_list = [int(ci_list[i], 16) for i in range(len(ci_list))]
    
    ci_list2 = [cipher2[i:i+2] for i in range(0, len(cipher2), 2)] 
    ci_list2 = [int(ci_list2[i], 16) for i in range(len(ci_list2))]
    
    message = padding(message)
    flag = decrypt(ci_list, ci_list2, message)
    print(flag)

if __name__ == "__main__":
    main()