select = (input("select your time: \ny=year\nh=hours\nm=minutes "))


def conve_to_seconds(select):
    if select == "y":
        years = int(input("type years: "))
        print(f"yesars in seconds is {years * 31556952}")
    elif select == "h":
        years = int(input("type hours: "))
        print(f" hours in seconds is {years * 3600}")
    elif select == "m":
        years = int(input("type minutes: "))
        print(f"minutes in seconds is {years * 60}")
    else:
        print("type valide value")


conve_to_seconds(select)
