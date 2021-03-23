#!/usr/bin/python3
#!/utf/8in/xorpp
#!/ali/elainous

from    getpass import  getpass
from    sys     import  argv
from    os      import  path

def decode(data):
    'Decode the target file.'
    try:
        return data.decode(), 'utf8'
    except UnicodeDecodeError:
        return data.decode('latin'), 'latin'

def XORPP(Bytes, password, length):
    'XOR++ Algorithm, (length of key > 1)'
    coded = ''
    Bytes,typ = decode(Bytes)
    for indx,byte in enumerate(Bytes):
        coded += chr(password[indx % length] ^ ord(byte))
    return coded.encode(typ)

def passwd():
    cin = input
    #cin = getpass
    password0 = cin('password        : ').encode()
    password1 = cin('Confirm password: ').encode()
    if  password0 != password1:
        exit('Error: Password does not match.')
    return password0, len(password1)

def main():
    filename = argv[1] if  len(argv) == 2 else input('filename: ')
    if  not path.exists(filename):
        quit('Error: The file "{}" does not exist.'.format(filename))
    with open(filename, 'rb') as File:
        password, length = passwd()
        data_coded  = XORPP(File.read(), password, length)
    with open(filename,'wb') as File:
        File.write(data_coded)

if  __name__ == '__main__':
    main()
