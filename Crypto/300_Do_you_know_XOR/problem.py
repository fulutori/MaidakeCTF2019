#import FLAG from FLAGS
#import SECRET_KEY from SECRET_KEYS

def encrypt(plane_text, secret_key):
    cipher_text = ""
    for pt, key in zip(plane_text, secret_key):
        cipher_num = ord(pt) ^ ord(key)
        cipher_text += format(cipher_num, '02x')
    return cipher_text

def padding(plane_text):
    pt_l = len(plane_text)
    if pt_l == 50:
        return plane_text
    else:
        plane_text += "%" * (50 - pt_l)
        return plane_text

def main():
    secret_key = SECRET_KEY
    plane_text = padding(FLAG)
    cipher_text = encrypt(plane_text, secret_key)
    with open("result.txt", 'a') as f:
        f.write("FLAG result: " + FLAG)

if __name__ == "__main__":
    main()