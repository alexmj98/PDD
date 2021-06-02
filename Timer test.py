from threading import Timer

second = 0

def seconds():
    global second
    second += 1
    print(f"{second}")
    Timer(1,seconds).start()
seconds()







