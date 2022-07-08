while True:
    try:
        t = int(input())
        while(t):
            x, y = input().split()
            if((int(y)-int(x))%3==0 or (int(y)-int(x))%3==1):
                print("Yes")
            elif ((int(y)-int(x))%3==2):
                print("No")
    except EOFError:
        break
