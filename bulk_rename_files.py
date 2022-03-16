import os


def main():
    i = 0
    path = r'C:\Users\Public\Test\\'
    for filename in os.listdir(path):
        new_name = 'file_' + str(i) + '.jpg'
        old_name = path + filename
        new_name = path + new_name
        os.rename(old_name, new_name)
        i += 1


if __name__ == '__main__':
    main()
