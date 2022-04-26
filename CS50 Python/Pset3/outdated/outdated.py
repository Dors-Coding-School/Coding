months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            x, y, year = date.split(" ")
            for i in range(len(months)):
                if x == months[i]:
                    month = i + 1
            day = y.replace(",", "")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

if int(month) < 10:
    month = '0' + str(month)
if int(day) < 10:
    day = '0' + str(day)
print(year + "-" + str(month) + "-" + str(day))
