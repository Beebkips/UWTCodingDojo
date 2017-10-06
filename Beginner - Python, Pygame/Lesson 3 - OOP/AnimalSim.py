from Bug import Bug
from Terrarium import Terrarium
import time

def main():
    terrarium = Terrarium()
    aBug = Bug()
    terrarium.add(aBug)
    while True:
        terrarium.move()
        terrarium.toString()
        time.sleep(1)


if __name__ == '__main__':
    main()