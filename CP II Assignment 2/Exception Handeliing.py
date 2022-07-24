try:
    f = open('eop.txt')
    s = f.readline()
except (IOError, ValueError,ImportError,FloatingPointError,	MemoryError,NameError):
    print("!!!Error occurred")