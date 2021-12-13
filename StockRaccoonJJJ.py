import datetime
import time
import requests
ProjectStart = time.perf_counter()
error = False
i=0

INTRODUCTION = '''
                           \U0001FA99 Stock Raccoon\U0001FA99
\U0001F4C8--------------------------------------------------------------------\U0001F4C8
  Welcome to Stock Raccoon. We'll give you roughly 5-6 months of 
  daily data and up to 20 years of weekly stock data about the opens, 
  closes, highs, lows, and the volume. We'll ask what stock you need 
  the data on and then give it to you.
\U0001F4C8--------------------------------------------------------------------\U0001F4C8
'''


def DailyData(x):
    start = time.perf_counter()

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function":"TIME_SERIES_DAILY","symbol":x.upper(),
    "outputsize":"compact","datatype":"json"}

    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': "7fff5a67damsh4ee374da51f9e15p1f5982jsn5d5b45736b7f"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.text.__contains__('Error'):
        print('This is not a valid ticker symbol, try again!')
        global error
        error = True
    else:
        print(response.text)
    
    
    end = time.perf_counter()

    tim = end - start

    t = datetime.datetime.now()
    print('\nCurrent date and time: ' + time.strftime('%c'))
    print('Results Obtained in ' + str(tim) + ' seconds')

def WeeklyData(x):
    start = time.perf_counter()

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function":"TIME_SERIES_WEEKLY","symbol":x.upper(),"datatype":"json"}

    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': "7fff5a67damsh4ee374da51f9e15p1f5982jsn5d5b45736b7f"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.text.__contains__('Error'):
        print('This is not a valid ticker symbol, try again!')
        global error
        error = True
    else:
        print(response.text)


    end = time.perf_counter()

    tim = end - start

    t = datetime.datetime.now()
    print('\nCurrent date and time: ' + time.strftime('%c'))
    print('Results Obtained in ' + str(tim) + ' seconds')


def ValidString(Response):
    if not Response.isalpha():
        return False
    else:
        return True

print(INTRODUCTION)


while i < 1:
    i+=1
    Stock = input('\nWhat stock do you want data on?(Only enter to stock ticker symbol)\n')
    
    if ValidString(Stock):
        pass
    else:
        print('This input has or is a number, enter a valid ticker symbol!')
        error = True

    if not error:
        data = input('''\nWould you like weekly data or daily data?
(Enter either \"weekly\" or \"daily\")\n''')

        if ValidString(data):
            pass
        else:
            print('This input eith has or is a number, enter either \"daily\" or \"weekly\"')
            error = True
    else:
        pass
    

    weekly = True

    if not error:
        if data.lower() == 'daily':
            weekly = False
        elif data.lower() == 'weekly':
            weekly = True
        else:
            print('This is not a valid input, try again!')
            error = True

    if weekly and not error:
        WeeklyData(Stock)
        ProjectEnd = time.perf_counter()
        x = ProjectEnd - ProjectStart
        print('Time spent in application: ' + str(x) + ' seconds')
    elif not weekly and not error:
        DailyData(Stock)
        ProjectEnd = time.perf_counter()
        x = ProjectEnd - ProjectStart
        print('Time spent in application: ' + str(x) + ' seconds')

    if error:
        i-=1
        error = False
    else:
        j=0
        while j < 1:
            j+=1
            yayOrNay = input('''\nWould you like more data on other stocks?
(Answer with a simple \"yes\" or \"no\")\n''')

            if yayOrNay.lower() == 'yes':
                i-=1
            elif yayOrNay.lower() == 'no':
                pass
            else:
                print('That is not a yes or no answer, try again!')
                j-=1