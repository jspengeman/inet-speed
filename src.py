import os
import httplib2
from settings import *
from pyspeedtest import SpeedTest
from datetime import datetime, timedelta
from apiclient import discovery
from time import sleep
from csv import writer
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def get_credentials():
    """
    Gets valid user credentials from storage.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
       'internet-speed-test-data.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def run_speed_test(ap, device, number_of_tests, interval, stressed, room, notes=""):
    """
    Run the speed test for a duration given some interval.
    """
    count = 0
    st = SpeedTest()
    test_data = []

    while number_of_tests > count:
        count += 1
        print "Running speed test: " + str(count)
        try:
            test_data.append([
                ap,
                device,
                round(st.ping(), 2),
                round(st.download() / BITS_TO_MEGA_BITS, 2),
                round(st.upload() / BITS_TO_MEGA_BITS, 2),
                stressed,
                room,
                notes
            ])
            sleep(interval * 60)
        except:
            print "There was an exception while testing."

    if len(test_data) > 0:
        append_to_drive(test_data)
    print "Completed %d speed tests" % count


def append_to_drive(values):
    """
    Append the data products to the google spreadsheet.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build(
        'sheets',
        'v4',
        http=http,
        discoveryServiceUrl=GOOGLE_DRIVE_URL
    )
    service.spreadsheets().values().append(
        spreadsheetId=SPEADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption=VALUE_INPUT_OPTION,
        body={'values': values}
    ).execute()

run_speed_test(
    ap=ACCESS_POINT,
    device=DEVICE,
    number_of_tests=NUMBER_OF_TESTS,
    interval=INTERNVAL,
    stressed=STRESSED_NETWORK,
    room=ROOM,
    notes=NOTES
)
