#!/usr/bin/env python
from Summoner import *

def main():
    names = ["你根本在發廢文"]
    for name in names:
        result = Summoner(name).get_recent_games()
        print(result)

if __name__ == "__main__":
    main()
