seconds = int(input("type seconds: "))


def seconds_convertions(seconds):
    print(f"days are: {seconds / (24 * 3600)}")
    seconds = seconds % (24 * 3600)
    print(f"hours are: {seconds / 3600}")
    seconds %= 3600
    print(f"min are: {seconds / 60}")


seconds_convertions(seconds)
