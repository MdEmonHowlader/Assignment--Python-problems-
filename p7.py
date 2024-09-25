import time
def count_time():
    try:
        start=int(input("Enter the countdown starting number: "))
        
        while start>=1:
            print(start)
            time.sleep(1)
            start-=1
        print("Time up!")
        
    except ValueError:
        print("please enter a valid integer.")
count_time()