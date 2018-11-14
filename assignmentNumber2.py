from __future__ import print_function

import urllib2
import csv
import argparse
import logging
import datetime

TEST_URL = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"

LOG_FILENAME = 'errors.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)

logger = logging.getLogger("assignment2")


def downloadData(url):
    """
    Use urllib2 to download the file which is found from website on old student's Github assignment.

    :param url: the URL
    :return:
    """
    file = urllib2.urlopen(url)
    return file


def processData(page):
    """
    1. processData (downloadData, loop line by line, birthday as a datetime object) accepts three parameters.
     2. The birthday may be in the wrong format- log each instance into ANOTHER FILE- a logger named assignment 2.
        - The logger should be sent to the ERROR level.
     3. Store CSV information in dictionary that maps IDs to TUPLES.

    :param page:
    :return:
    """
    person_dict = dict()

    header = True
    line_number = 0
    for line in page:
        if header:
            header = False
            continue

        line_number = line_number + 1 #Look above for how to iterate beyond a header.

        pieces = line.rstrip().split(",") #Pieces are every line [ for line in page- line.rstrip ] split by "," character into a distinct element, indexed into a list.
        userid = int(pieces[0])
        name = pieces[1]
        try:

            birthday = datetime.datetime.strptime(pieces[2], "%d/%m/%Y")
            # print("id = {} | name = {} | birthday = {}".format(userid, name, birthday.strftime("%Y%m%d")))
            person_dict[userid] = (name, birthday)
        except ValueError:
            logging.error("Error processing line #{} for ID #{}".format(line_number, userid))

    return person_dict


def displayPerson(id, personDataDictionary):
    """

    :param id:
    :param personDataDictionary: Look at displayPerson in __name__ function. But I thought bday was pieces[2].
    :return:
    """
    print("id = {}, name = {}, birthday = {}".format(id, personDataDictionary[id][0],
                                                     personDataDictionary[id][1].strftime("%Y-%m-%d")))


if __name__ == '__main__':
    """
    1. Use the argeparse module to take the url parameter.
    2. csvData= downloadData()
    3. Set up logger named assignment2. This can be done here or in a separate function.
    4. Pass csvData into processData(), save result into a variable called personData; which is a dictionary that matches ID to tuples.
    5. User input: ID number
        -If 0, exit. If negative number- exit.
    - Iterate through a csv file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Add URL", action="store", type=str, required=True)
    parser.add_argument("--name")
    args = parser.parse_args()

    print("URL passed = {}".format(args.url))
    page = downloadData(args.url)
    persons = processData(page)


    while True:
        prompt = int(raw_input(" Enter ID of person you would like to search for- or 0 to Terminate program: "))

        if prompt > 100:
            print("Invalid ID- please enter ID between 1-100.")
            continue

        elif prompt >0:
            displayPerson(prompt,persons)

        else:
            break

    print("Thank you for using this program.")

























