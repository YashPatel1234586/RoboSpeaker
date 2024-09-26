import os

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 , Created by Yash Patel")
    while True:
        x = input(" Enter what you want me speak : ")
        if x == "q":
            os.system(" say 'bye Bye Friends' ")
            break
        command = f"say {x}"
        os.system(command)


