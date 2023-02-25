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

    #\\\ Empty list that will have the location of each category. This is only solving the first problem
    datez = []
    countyz = []
    statez = []
    flipz = []
    casesz = []
    deathz = []
    #\\\ A while loop to find and seperate all the data in VA. This is only solving the first problem
    n = 0
    while n <= len(data)/6:
        datez.append((data[n]).date)
        countyz.append((data[n]).county)
        statez.append((data[n]).state)
        flipz.append((data[n]).fips)
        casesz.append((data[n]).cases)
        deathz.append((data[n]).death)
        n = n + 1
    hburg_county = []
    rockingham_county = []

    for HBURG in range(len(data)):
        if (data[HBURG]).county == "Harrisonburg City":
            hburg_county.append((data[HBURG]).cases)
    print(hburg_county)
    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County? When was the first in Harrisonburg?

    #\\\ Uses the previous definition function to find the first Rockingham County one
    first_RC=countyz.index('Rockingham')
    print('The first case in Rockingham County')
    printerz(first_RC)

    # \\\ Uses the previous definition function to find the first Harrisonburg one
    first_Hbrug=countyz.index('Harrisonburg city') #\\\ Man I was typing in Harrisonburg like a fool not Harrisonburg City
    print('The first case in Harrisonburg City')
    printerz(first_Hbrug)
    #\\\ Gangster first one done

    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?


    # write code to address the following question:
    # What was the worst seven day period in either the city and county for new COVID cases? This is the 7-day period where the number of new cases was maximal.


