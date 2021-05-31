# https://replit.com/@heysujal/day-30-2-exercise#main.py
# https://replit.com/@heysujal/day-30-1-exercise

try:
    file = open("a_file.txt", mode='r')
    # file = open("a_file.txt",mode='w')
    # file.wrote('jdiawhdiha')

    # a_dictionary = {'key':'value'}
    # print(a_dictionary['sss'])
except AttributeError:
    print('attribute error')
except FileNotFoundError:
    print('file error hai ji')
except KeyError as message:
    print(f'{message} key not found')
else:
    print("sab changa si")
finally:
    print('mai to chalunga hi')
    # raise KeyError
    # raise TypeError("This is the error which I made")
