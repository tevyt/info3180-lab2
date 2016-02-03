from time import strftime

def current_date_time():
    return strftime('%c')


if __name__ == '__main__':
    print current_date_time()
