#[9:29 AM] Satyam Singh (Unverified)

def dayOfWeek(dd = 24, mm=5, yyyy=2024):
    if mm < 3:
        mm += 12
        yyyy -= 1 
    q = dd
    m = mm
    K = yyyy % 100
    J = yyyy // 100
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    #print(f"The day of the week for {dd}/{mm}/{yyyy} is {days[h]}.")
    return h

def getMaxDays(mm,yyyy):
    max31 = [1,3,5,7,8,10,12]
    max30 = [4,6,9,11]
    feb = [28,29]
    if mm == 2:
        return feb[isLeap(yyyy)]
    if mm in max30:
        return 30
    if mm in max31:
        return 31

    return -1

def isLeap(year):
    #[10:15 AM] Satyam Singh (Unverified)
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def printCalendar(mm, yyyy):
   #VaishnaviY(vaishnaviyetekar10@gmail.com) (Unverified)
   month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
   
   w = dayOfWeek(1, mm, yyyy)
   print(f'Day {w}')
   
   max = getMaxDays(mm,yyyy)
   if max != -1:
        print(f"{month[mm-1]} {yyyy}\nSu Mo Tu We Th Fr Sa")
        for d in range(w):#for spacing 
            print(f'{" ":3}',end='')
        for d in range(1, max+1): #for printing 
            print(f'{d:<3}', end='' if (d+w) % 7 != 0 else '\n')
                
        print()
        
 

if __name__ == '__main__':
    dayOfWeek()
    dayOfWeek(1,5,2024)
    printCalendar(12,2024)
