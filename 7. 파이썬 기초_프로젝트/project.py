def menu():
    #print('%-10s %15s %11s %-9s %-10s %-10s' %('students','name','Midterm','final','Average','Grade'))
    print('   '+'Student'+'             '+'Name'+'    '+'Midterm'+'     '+'Final'+'       '+'Average'+'     '+'Grade')
    print('--------------------------------------------------------------------------')
def grade():
    for key, value in d.items():
        if int(value[3]) >= 90 :
            value[4] = 'A'
        elif int(value[3]) >= 80 :
            value[4] = 'B'
        elif int(value[3]) >= 70 :
            value[4] = 'C'
        elif int(value[3]) >= 60 :
            value[4] = 'D'
        else:
            value[4] = 'F'
    # print(d)
def average():
    for key, value in d.items():
        value[3] = round(((int(value[1]) + int(value[2]))/2),1)
def show_function():
    average()
    grade()
    menu()
    x = sorted(d.items(), key = lambda item: item[1][3], reverse = True)
    for key, value in x:
        cnt = 0
        print(' '*2+str(key), end='\t')
        for i in value:
            a = int(k[cnt])
            b = int(len(str(i)))
            print(' '*(a-b)+str(i), end='')
            cnt += 1
        print()
def search_function():
    command = input('Student ID: ')
    if command not in list(d.keys()) :
        print('NO SUCH PERSON.')
    else:
        menu()
        for key, value in d.items():
            cnt = 0
            if(key == command):
                print(' ' * 2 + str(key), end='\t')
                for i in range(0,(len(value))) :
                    # print('-------'+str(i))
                    a = int(k[cnt])
                    b = int(len(str(value[i])))
                    print(' '* (a-b) + str(value[i]), end='')
                    cnt += 1
        print()
def changescore():
    command = input('Student ID: ')
    if command not in list(d.keys()):
        print('NO SUCH PERSON.')
    else:
        command2 = input('Mid/Final? ')
        if (command2) == 'mid' :
            command3 = input('Input new score: ')
            if 0 <= int(command3) and int(command3) <= 100:
                for key, value in d.items():
                    if(key == command) :
                        menu()
                        for key, value in d.items():
                            cnt = 0
                            if (key == command):
                                average()
                                grade()
                                print(' ' * 2 + str(key), end='\t')
                                for i in value:
                                    a = int(k[cnt])
                                    b = int(len(str(i)))
                                    print(' ' * (a - b) + str(i), end='')
                                    cnt += 1
                                if (command2) == 'mid':
                                    d[key][1] = int(command3)

                        print('')
                        print('Score changed.')
            else :
                return
        else:
            return
        for key, value in d.items():
            cnt = 0
            if(key == command):
                average()
                grade()
                print(' ' * 2 + str(key), end='\t')
                for i in value:
                    a = int(k[cnt])
                    b = int(len(str(i)))
                    print(' ' * (a - b) + str(i), end='')
                    cnt += 1
        print()
def add():
    command = input('Student ID: ')
    if command in list(d.keys()):
        print('ALREADY EXISTS.')
    else:
        command2 = input('Name: ')
        command3 = input('Midterm Score: ')
        command4 = input('Final Score: ')
        d[command] = [command2, command3, command4,1,1]
        print('Student added.')
def searchgrade():
    command = input('Grade to search: ')
    if command.upper() not in ['A','B','C','D','F']:
        return
    else:
        cnt = 0
        for key, value in d.items():
            if (value[4] == command):
                if(cnt == 0):
                    menu()
                cnt += 1
                cnt2 = 0
                print(' ' * 2 + str(key), end='\t')
                for i in value:
                    a = int(k[cnt2])
                    b = int(len(str(i)))
                    print(' ' * (a - b) + str(i), end='')
                    cnt2 += 1
                print()
        if(cnt == 0):
            print('NO RESULTS.')
def remove():
    if len(d) == 0:
        print('List is empty')
        return
    command = input('Student ID: ')
    if command not in list(d.keys()):
        print('NO SUCH PERSON.')
    else:
        del d[command]
        print('Student removed.')
def quit():
    filename = input('Filename : ')
    f1 = open(filename, "w")
    x = sorted(d.items(), key=lambda item: item[1][3], reverse=True)
    for key, value in x:
        s = '%s\t %s\t %s\t %s\t %d\t %s\n' % (key, value[0], value[1], value[2],value[3],value[4])
        f1.write(s)
    f1.close()

stu_list = list()
d = dict()
k = ['15','9','11','14','10']
f = open('students.txt', 'r')
for i in f:
    stu_list = i.split('\t')
    for j in range(0,1):
        d[stu_list[j]]= [stu_list[j + 1], stu_list[j + 2], (stu_list[j + 3])[:-1],' ',' ']
average()
grade()
while True:
    command = input('# ')
    if command == 'show':
        show_function()
    elif command == 'search':
        search_function()
    elif command == 'changescore':
        changescore()
    elif command == 'add':
        add()
    elif command == 'remove':
        remove()
    elif command == 'searchgrade':
        searchgrade()
    elif command == 'quit':
        save = input('Save data?[yes/no] ')
        if save.lower() =='yes':
            quit()
        elif save.lower() =='no':
            break
        else:
            pass
        break
    else:
        print("wrong input!")