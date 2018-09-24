import urllib2
import csv
import argparse
import logging
import datetime


#file = urllib2.urlopen("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")

# https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv
file = urllib2.urlopen("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")





def downloadData():
    ''' Use urllib2 to download the file which is found from website on old student's Github assignment. '''
    file = urllib2.urlopen("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")
    page= file.read()
    file.close()
    return page


def processData(page):
    '''
     1. processData (downloadData, loop line by line, birthday as a datetime object) accepts three parameters.
     2. The birthday may be in the wrong format- log each instance into ANOTHER FILE- a logger named assignment 2.
        - The logger should be sent to the ERROR level.
     3. Store CSV information in dictionary that maps IDs to TUPLES.
     '''
    process= csv.reader(page)
    for line in page:
        print (line)



def displayPerson(id, personDataDictionary):
    ''' ... '''

    pass

if __name__== '__main__':
    '''
    1. Use the argeparse module to take the url parameter.
    2. csvData= downloadData()
    3. Set up logger named assignment2. This can be done here or in a separate function.
    4. Pass csvData into processData(), save result into a variable called personData; which is a dictionary that matches ID to tuples.
    5. User input: ID number
        -If 0, exit. If negative number- exit.
    - Iterate through a csv file.
    '''
    #this= downloadData()
    file = urllib2.urlopen("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")
    page= file.read()
    print page

    parser= argparse.ArgumentParser()
    parser.add_argument("--url", help= "Add URL")
    args= parser.parse_args()

