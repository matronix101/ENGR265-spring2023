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
    #\\\ Definition loop that will print the exact location hehe
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
    while n <= len(data)/6:
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
    printerz(first_RC)

    # \\\ Uses the previous definition function to find the first Harrisonburg one
    first_Hbrug=countyz.index('Harrisonburg city') #\\\ Man I was typing in Harrisonburg like a fool not Harrisonburg City
    printerz(first_Hbrug)
    #\\\ Gangster first one done

    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?

    #\\\ Hmmmmmm man I don't think you'll like this but I will try and make a seperate list of only Harrisonburg "City"
    #\\\ Then use that max to find the date and from the date find the right location

    def max_finder(area_of_max):
        hBurg_city = []
        hBurg_city_max = []
        print('countlen',len(countyz))
        for yes in range(int(len(countyz))):
            if countyz[yes] == area_of_max:
                hBurg_city.append(yes)
        print(hBurg_city)
        print('len of hburg', len(hBurg_city))


        for hburg_max in range(len(hBurg_city)):
            hBurg_city_max.append(casesz[hBurg_city[hburg_max]])
        print(hBurg_city_max)
        print('len og hbmax', len(hBurg_city_max))
        max_of_hburg = max(hBurg_city_max)
        print(max_of_hburg)
        print(hBurg_city_max.index(max_of_hburg))
        max_of_this = max_of_hburg


        return max_of_this
        #///////ADD SHIT TO FIND THE LOCATION OF THE DATE FROM THE MAX AND DISPLAY THAT LATER
    max_finder("Harrisonburg city")
    # write code to address the following question:
    # What was the worst seven day period in either the city and county for new COVID cases? This is the 7-day period where the number of new cases was maximal.


