import os
import pickle
from struct import *
import time
import random



FILE_NAME = open('1.txt','r').read()
SECOND_FILE_NAME = 'test.bin'

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    #dictionary = dict((chr(i), i) for i in range(dict_size))
    dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    #dictionary = dict((i, chr(i)) for i in range(dict_size))
    dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
 
#----------------------------------------------------------------------------------------------------------
def dir():
    
    dir__name = str(random.randint(100, 999))
    list__dir = os.listdir(os.getcwd())
    count__folder = list__dir.count(dir__name)
    global file__name 
    file__name = 'Archiv {}'.format(dir__name)
    
    if count__folder == 0:
        os.mkdir(file__name)
    else:
        dir__name = str(random.randint(100, 999))
        os.mkdir(file__name)

    os.chdir(file__name)
    
    
#------------------------------------------------------------------------------------------------------------
def compressing(FILE_NAME):
    start_time = time.time()
    print('--------------------------------------------')
    txt1 = os.path.getsize('1.txt')
    print('Было ' + str(txt1)+ ' Байт')
    print('--------------------------------------------')
    compressed = compress(FILE_NAME)

    
    case =[]

    dir()


    with open('test.bin', 'wb') as f:
        for i in compressed:
            if i < 256:
                f.write(pack('B', i))
                case.append(1)
            else:
                f.write(pack('H', i))
                case.append(2)       

    key = int(''.join(map(str, case)))

    with open('key.bin', 'wb') as f:
        f.write(pack('Q', key))
    
    print('Стало ' + str(os.path.getsize('test.bin')) + ' Байт')
    print('--------------------------------------------')
    percent = 100 - 100*os.path.getsize('test.bin')/txt1
    print('Процент сжатия = ' + str('%.1f' % percent) + '%')
    print('--------------------------------------------') 
    print("Время сжатия составляет " +  str('%.2f ' % (time.time() - start_time)) + 'секунд')
    print('--------------------------------------------')


def decompressing(SECOND_FILE_NAME):
    with open('key.bin','rb') as file:
        case = file.read()
    case = list(unpack('Q', case))
    case = list(str(case[0]))
    new__case = []
    for i in case:
        new__case.append(int(i))    
    
    case__for__bytes = []

    with open('test.bin', 'rb') as f:
        data = f.read()
    k = 0
    i = 0
    while i <= len(new__case)-1:
        if new__case[i] == 1:
            case__for__bytes.append(data[i:i+1])
            i+=1
        elif new__case[i] == 2:
            if k<i:
                k = i
                case__for__bytes.append(data[k:k+2])
                i+=1
                k+=2
            elif k>=i:
                case__for__bytes.append(data[k:k+2])
                i+=1
                k+=2
        else:
            pass    

    case__for__decompress = []

    for i,j in zip(new__case, case__for__bytes):
        if i == 1:
            temp_one = (unpack('B', j))
            temp_one = int(temp_one[0])
            case__for__decompress.append(temp_one)
        else:
            temp_two = (unpack('H', j))
            temp_two = int(temp_two[0])
            case__for__decompress.append(temp_two)
    
    output = decompress(case__for__decompress)
    with open('text.txt', 'w') as f:
        f.write(output)
    
    


    

    





compressing(FILE_NAME)
decompressing(SECOND_FILE_NAME)





#decompressed = decompress(compressed)
