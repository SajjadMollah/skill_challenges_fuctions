
import datetime
def AgeAllowed(birthday):
    try:
        birthYear = int(birthday[0:4])
        birthMonth = int(birthday[5:7])
        birthDay = int(birthday[8:10])
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day
        if birthYear > year:
            return "Invalid Date"
        if birthYear == year:
            if birthMonth > month:
                return "Invalid Date"
            elif birthMonth == month:
                if birthDay > day:
                    return "Invalid Date"
        if month < birthMonth:
            year = year - 1
        elif month == birthMonth:
            if day < birthDay:
                year = year - 1
        age = year - birthYear
        allowed = False
        if age >= 16:
            return "Access Granted"
        else:
            output = "Access Denied. You need to be 16 and you are " + str(age) + "."
            return output
    except:
        return "Invalid Date"