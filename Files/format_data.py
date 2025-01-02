

def run():
    f = open('test.txt', 'r')
    r = open('formated.txt', 'a')

    counter = 0
    for l in f.readlines():
        r.writelines([str(l[20:29]), '\n'])
        counter += 1
if __name__ == "__main__":
    run()

# def run():
#     f = open('test.txt', 'r')
#     r = open('formated.txt', 'a')

#     counter = 0
#     for l in f.readlines():
#         r.writelines([str(l[23:29])])
#         counter += 1
# if __name__ == "__main__":
#     run()