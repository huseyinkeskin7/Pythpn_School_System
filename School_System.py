# Written by Hüseyin Berk Keskin
import random
import time

print("Written by Hüseyin Berk Keskin")


def all_students_list():
    with open("students.txt","r",encoding="utf-8") as file:
        i=0
        print("\n")
        for satir in file:
            i+=1
            if i>0 and i<=3:
                print('(CLASS A)',satir)
            elif i>3 and i<=6:
                print('(CLASS B)',satir)
            elif i>6 and i<=9:
                print('(CLASS C)',satir)
            elif i>9 and i<=12:
                print('(CLASS D)',satir)
            elif i>12 and i<=15:
                print('(CLASS E)',satir)
            elif i>15 and i<=18:
                print('(CLASS F)',satir)
            elif i>18 and i<=21:
                print('(CLASS G)',satir)
            elif i>21 and i<=24:
                print('(CLASS H)',satir)
            elif i>24 and i<=27:
                print('(CLASS I)',satir)
            elif i>27 and i<=30:
                print('(CLASS J)',satir)
        print("\n")
#all_students_list()

def shuffle_class():
    with open("students.txt","r",encoding="utf-8") as file:
        i=-1
        liste=[]
        for satir in file:    
            liste.append(satir)
        random.shuffle(liste)
        file.close()
        l = len(liste)

    with open("students.txt", "w",encoding="utf8") as file:
        while True:
            if i<l-1:
                i+=1
                file.write(liste[i])
            else:
                break
        file.close()
    with open("students.txt","r",encoding="utf-8") as file:
        u=0
        print("\n")
        for satir in file:
            u+=1
            if u>0 and u<=3:
                print('(CLASS A)',satir)
            elif u>3 and u<=6:
                print('(CLASS B)',satir)
            elif u>6 and u<=9:
                print('(CLASS C)',satir)
            elif u>9 and u<=12:
                print('(CLASS D)',satir)
            elif u>12 and u<=15:
                print('(CLASS E)',satir)
            elif u>15 and u<=18:
                print('(CLASS F)',satir)
            elif u>18 and u<=21:
                print('(CLASS G)',satir)
            elif u>21 and u<=24:
                print('(CLASS H)',satir)
            elif u>24 and u<=27:
                print('(CLASS I)',satir)
            elif u>27 and u<=30:
                print('(CLASS J)',satir)



    
#shuffle_class()

def find_stu_w_number():
    number = input("Enter student's number: ")
    with open("students.txt", "r",encoding="utf8") as file:
        for line in file:
            if number in line:
                print(line)
                break
        else:
            print("Student not found.")

#find_stu_w_number()

def remove_student():
        number = input("Enter student's number: ")
        with open("students.txt", "r",encoding="utf8") as file:
            read = file.readlines()
            file.close()
        with open("students.txt", "w",encoding="utf8") as file:
            for line in read:
                if not number in line:
                    
                    file.write(line)
                  

#remove_student()


def add_student():
    name = input("Enter student's name : ")
    surname = input("Enter student's surname : ")
    number = int(input("Enter student's number : "))
    with open("students.txt","a",encoding="utf-8") as file:
        file.write(name+' '+surname+': '+str(number)+'\n')
    print('New student has been added!')


#add_student()

while True:

    print("<<<School System>>>")
    print("1. View all student list")
    print("2. Shuffle Classes")
    print("3. Find Student with Number")
    print("4. Add Student")
    print("5. Remove Student")
    print("6. Exit the system")
    choice = input("Enter choice: ")
    
    if choice == "2":
        shuffle_class()
        time.sleep(3)

    elif choice == "1":
        all_students_list()
        time.sleep(3)
        
    elif choice == "3":
        find_stu_w_number()
        time.sleep(3)

    elif choice == "4":
        add_student()
        time.sleep(3)

    elif choice == "5":
        remove_student()
        print("Student has been deleted!")
        time.sleep(3)

    elif choice == "6":
        break
    else:
        print("Invalid choice")


