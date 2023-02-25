####READ NOTES AT THE BOTTOM IF THIS IS WRONG

class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)


    return covid_data


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)


    return covid_data



if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')

    # each element in list data is a CovidRecord object. Each of which contains
    # date, county, state, fips, cases, and deaths

    # for example, we can print out the data for the first point in the US counties file
    #point = data[6]

    #\\\ Thank you for the hint Dr. Forsyth imma just borrow and adjust it for a
    #\\\ Definition loop that will print the exact location here
    def printerz(location):
        point = data[location]
        ok =print("Data: ", point.date, " County: ", point.county, " State: ", point.state,
            " FIPS: ", point.fips, " Cases: ", point.cases, " Deaths: ", point.death)
        return ok

    #\\\ Empty list that will have the location of each category
    datez = []
    countyz = []
    statez = []
    flipz = []
    casesz = []
    deathz = []
    #\\\ A while loop to find and seperate all the data in VA
    n = 0
    while n <= len(data)-1:
        datez.append((data[n]).date)
        countyz.append((data[n]).county)
        statez.append((data[n]).state)
        flipz.append((data[n]).fips)
        casesz.append((data[n]).cases)
        deathz.append((data[n]).death)
        n = n + 1

    #print (datez)
    #print (countyz)
    #print (statez)
    #print (flipz)
    #print (casesz)
    #print (deathz)

    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County? When was the first in Harrisonburg?

    #\\\ Uses the previous definition function to find the first Rockingham County one
    first_RC=countyz.index('Rockingham')
    print('First case in Rockingham')
    printerz(first_RC)
    print()

    # \\\ Uses the previous definition function to find the first Harrisonburg one
    first_Hbrug=countyz.index('Harrisonburg city') #\\\ Man I was typing in Harrisonburg like a fool not Harrisonburg City
    print('First case in Harrisonburg city')
    printerz(first_Hbrug)
    print()
    #\\\ Gangster first one done

    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?

    #\\\ Definition function that will locate the location of the greatest amount of new daily cases
    #\\\ and you can put in a differient city if you want
    #\\\ delete the #\ cases if you want to see the progress
    def max_finder(area_of_max):

        #\\\Generates empty lists
        hBurg_city = []
        hBurg_city_max = []
        max_finder = []

        #\\\ City finder
        for yes in range(int(len(countyz))):
            if countyz[yes] == area_of_max:
                hBurg_city.append(yes)
        #\\\Change in cases finder
        for hburg_max in range(len(hBurg_city)):
            hBurg_city_max.append(casesz[hBurg_city[hburg_max]])
        for delta_cases in range(len(hBurg_city_max)):
            max_finder.append(hBurg_city_max[delta_cases]-hBurg_city_max[delta_cases-1])
        max_finder.pop(0)
        #\print('Deltaz',max_finder)

        #\\\Most amount of new cases in a week
        mega_max_finder=[]
        counter = 6
        #\print('this is the real list', hBurg_city_max)
        for counter in range(len(max_finder)):
            mega_max_finder.append(max_finder[counter]+max_finder[counter-1]+max_finder[counter-2]+max_finder[counter-3]+max_finder[counter-4]+max_finder[counter-5]+max_finder[counter-6])
        mega_max_finder = mega_max_finder[6:]
        #\print('dis da mega max list',mega_max_finder)
        #\print(('fr dis da max',max(mega_max_finder)))
        week_max=max(mega_max_finder)
        weeks_location=mega_max_finder.index(week_max)+1
        #\print('weeklcoation',weeks_location)
        weekly_max=hBurg_city_max[weeks_location]
        #\print(weekly_max)
        #\print(hBurg_city_max)
        #\print('max_finder')
        #\print(max_finder)

        #\\\Finds the location of the max value
        #\print(hBurg_city_max)
        max_of_hburg = max(max_finder)
        #\print('Delta max of hbrug',max_of_hburg)
        #\print('dis a len of teh maxlist',len(max_finder))
        dis_damax=max_finder.index(max_of_hburg)
        #\print('loc of da amx', dis_damax)
        max_valuez = hBurg_city_max[dis_damax+1]

        #\print('maxcases',hBurg_city_max[dis_damax+1])
        #\\\ Prints the max value
        for yes in range(int(len(countyz))):
            if (countyz[yes] == area_of_max) and (casesz[yes+0] == max_valuez):
                print(f'The most amount of cases in {area_of_max}')
                printerz(yes)
                print(max_of_hburg,'Cases')
                print()

        #\\\Prints weekly max value
        for yes_2 in range(int(len(countyz))):
            if (countyz[yes_2] == area_of_max) and (casesz[yes_2] == weekly_max):
                print(f'The most amount of cases in a week in {area_of_max} starts on ')
                print(f'from {(data[yes_2]).date}')
                printerz(yes_2)
                print()

    max_finder("Harrisonburg city")
    max_finder("Rockingham")

    ####IF THIS IS WRONG GO TO LINE 224 and change +0 to either +1 or -1
    # write code to address the following question:
    # What was the worst seven day period in either the city and county for new COVID cases? This is the 7-day period where the number of new cases was maximal.
    ####IF THIS IS WRONG GO TO LINE 204 and change +1 to either +0 or +2
    print('If this does not work or slightly incorrect refer to the comments near the bottom of the code for each question, hopefully I am right the first time')
    print('Also I should have asked earlier in the week, but from the data that was given, I read the cases data as the total amount of cases, not the amount of cases on that day')
    print('Also I did judge that the new amount of cases in a day based on comparing the current day - previous day')

