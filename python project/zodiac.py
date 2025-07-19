
'''#Key Parts of the Code
#Global Dictionary (Dictionary1):

#This is used to store user information (name, date of birth, zodiac sign) for each user who enters their details.
#Functions:

#The program is divided into several small functions, each responsible for a specific task.
#takeUserDay():

#This function asks the user to input the day of the month they were born.
#It checks if the input is a valid number (between 1 and 31). If not, it asks the user to input the day again.
#takeUserMonth():

#This function asks the user for the month they were born in. It accepts both full month names (like "January") and short forms (like "Jan" or "1").
#It converts the month to a number (1 for January, 2 for February, etc.).
#takeUserYear():

This function asks for the year of birth.
It checks if the year is valid (greater than zero).
It also tells you if the year is a leap year (a year divisible by 4).
calculateSign(day, month):

This is the core function that determines the user's zodiac sign based on their birth month and day.
For example, if you're born on March 20, your sign is Pisces; if it's March 21, your sign is Aries.
takeDate(year, month, day):

This function combines the user's year, month, and day into a valid date using Python’s datetime module and prints the complete date.
repeatQuestion():

After calculating the zodiac sign, this function asks if the user wants to calculate another person's zodiac sign.
If the user answers "yes," the program repeats the process for the next person.
UserInput(count):

This function gathers the user's name, birth date, and zodiac sign.
It stores this information in the global Dictionary1, where each user's data is associated with a unique number (starting from 1).
SavetoPandas():

Although this function is currently empty, it is meant to handle saving the data to a Pandas DataFrame (a table-like structure) later on.
Main Program (if __name__=='__main__':):

This is the main part of the code that runs when you execute the program.
It repeatedly asks for user input and keeps track of multiple users' zodiac signs.
When the user is done, the program saves the collected data (name, date of birth, zodiac sign) into a CSV file using the Pandas library.
How the Program Works Step by Step:
User Input:

The program asks the user to input their name, day, month, and year of birth.
Calculate Zodiac Sign:

Based on the provided birth date, the program calculates the zodiac sign.
Store Data:

It stores the user’s name, birth date, and zodiac sign in a dictionary.
Repeat:

The program asks if another person's zodiac sign should be calculated.
Save to CSV:

When all users' data has been entered, the program converts the dictionary into a Pandas DataFrame and saves it to a CSV file.'''
import datetime
import csv
import pandas

Dictionary1={} # global dictionary to use store data for each user
def takeUserDay():
    try:
        day =int(input('Enter day: '))

        if day != str:
            if day <= 0 or day > 31:
                print('Enter a valid day!!! ')
                return takeUserDay() # to re enter a day
            
            else:
                return day
    except:
        print('ERROR: Only Numbers are accepted!')
        return takeUserDay()



def takeUserMonth():
    month = input('Enter month: ')
    if month == 'January' or month == '1' or month == 'Jan' or month == 'january' or month == 'jan' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month=='February' or month == '2' or month == 'Feb' or month =='february' or month =='feb' or month =='02' :
        monthNumber = 2
        return monthNumber
    elif month=='March' or month =='3' or month =='Mar' or month =='march' or month =='mar' or month =='03':
        monthNumber = 3
        return monthNumber
    elif month=='April' or month =='4' or month =='Apr' or month =='april' or month =='apr' or month =='04':
        monthNumber = 4
        return monthNumber
    elif month=='May' or month =='5' or month =='may' or month =='05':
        monthNumber = 5
        return monthNumber
    elif month=='June' or month =='6' or month =='june' or month =='06':
        monthNumber = 6
        return monthNumber
    elif month=='July' or month =='7' or month =='july' or month =='07':
        monthNumber = 7
        return monthNumber
    elif month=='August' or month =='8' or month =='Aug' or month =='august' or month =='aug' or month =='08':
        monthNumber = 8
        return monthNumber
    elif month=='September' or month =='9' or month =='Sept' or month =='september' or month =='sept' or month =='09':
        monthNumber = 9
        return monthNumber
    elif month=='October' or month =='10' or month =='Oct' or month =='october' or month =='oct':
        monthNumber = 10
        return monthNumber
    elif month=='November' or month =='11' or month =='Nov' or month =='november' or month =='nov':
        monthNumber = 11
        return monthNumber
    elif month=='December' or month =='12' or month =='Dec' or month =='december' or month =='dec':
        monthNumber = 12
        return monthNumber
    else:
        print('ERROR: Enter a valid month ')
        return takeUserMonth() # re do it again 



def takeUserYear():

    try:

        year = int(input('Enter year: '))
        
        if year != str:
            if year <= 0:
                print('ERROR:  ')
                return takeUserYear()
            elif year%4 == 0:
                print('Leap year!')
                return year
            else:
                return year
    except:
        print('ERROR: Enter Numerical Value Only')
        return takeUserYear() # re do it again 
    



def calculateSign(day,month):
      
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
        
    return astro_sign

def takeDate(year,month,day):
    date1=datetime.date(year,month,day)
    print('DOB: ',date1)
    return date1


def repeatQuestion():
    Finder=input('Do you want to find any other Zodiac sign(yes/no): ')
    if Finder =='yes':
        return True
    else:
        return False


def UserInput(count):
    
    userName= input('Enter the name of the user: ')
    userYear = takeUserYear()
    userMonth = takeUserMonth()
    userDate = takeUserDay()
    fullDate = takeDate(userYear,userMonth,userDate)
    yourSign = calculateSign(userDate, userMonth)
    print(userName, "your Zodiac sign is :",yourSign)
    Dictionary1[count] = { 'FullName' : '', 'DateOfBirth' : '', 'ZodiacSign' : '' }
    Dictionary1[count]['FullName'] = userName
    Dictionary1[count]['DateOfBirth'] = str(fullDate)
    Dictionary1[count]['ZodiacSign'] = yourSign
    
    
    print(Dictionary1[count])
    
def SavetoPandas():
    pass

if __name__=='__main__':
    Repeat = True
    Count = 1
    while Repeat == True:
        UserInput(Count)
        Count +=1
        Repeat = repeatQuestion()
    df = pandas.DataFrame(data=Dictionary1)
    fileName = input('PLease enter file Name:   ')
    savedData = df.to_csv(fileName+'.csv', index = True)
    print(df)
