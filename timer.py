import datetime as timer

def ex_01(date_str):
    return timer.datetime.strptime(date_str, '%b %d %Y %I:%M%p')

def ex_01_01(date):
    return str(date)

def ex_02():
    days = len([m for m in range(1,13) for y in (2015, 2016) if (timer.date(y, m, 1)).weekday() == 0])
    return days

def ex_03():
    lines = []
    with open("input") as file:
        lines = file.read().splitlines()

    lines.sort()

    str = "\n".join(lines)
    lines.sort(reverse=True)
    str2 = "\n".join(lines)
    str += "\n" + str2

    with open('output', 'w') as file:
        file.write(str)
        # file.write(str2)



if __name__ == "__main__":
    x = ex_01('Jun 1 2005  1:33PM')
    print(x),
    print(type(x))

    x = ex_01_01(timer.datetime.now())
    print(x),
    print(type(x))
    print(ex_02())
    ex_03()