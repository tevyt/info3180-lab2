from time import strftime

def current_date():
    return strftime('%a %W %b %Y')


if __name__ == '__main__':
    print current_date()
