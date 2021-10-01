# formatted output log
def prif(val, flag='info'):
    print(f' [{flag}] {val}')


# formatted input log
def inpf(val, flag='info'):
    return input(f' [{flag}] {val}')


# formatted exit info
def exif(val):
    prif(val, 'error')
    inpf('insert any key to exit', 'warn')
    exit()
