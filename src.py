from pyspeedtest import SpeedTest
from datetime import datetime, timedelta
from time import sleep
from csv import writer

# config: (device, notes)
# device, ap, ping, ul, dl, notes

class Internet:

    BITS_TO_MEGA_BITS = 1000000

    def __init__(self, ap, device, duration, interval, notes=None):
        self.ap = ap
        self.device = device
        self.notes = notes
        self.test(duration, interval)

    def test(self, duration, interval):
        """
        Run the speed test for a duration given some interval.
        """
        count = 1
        st = SpeedTest()
        start_time = datetime.now()
        time_delta = timedelta(minutes=duration)

        while start_time + time_delta > datetime.now():
            print "Running speed test: " + str(count)
            self.write(
                st.ping(),
                st.download() / Internet.BITS_TO_MEGA_BITS,
                st.upload() / Internet.BITS_TO_MEGA_BITS
            )
            count += 1
            sleep(interval * 60)

        print "Completed %d speed tests" % count

    def write(self, ping, dl, ul):
        """
        Write the test results to csv.
        """
        with open('output.csv', 'a') as output:
            csv_writer = writer(output)
            csv_writer.writerow(
                [self.device, self.ap, ping, dl, ul, self.notes]
            )


Internet(
    ap="RT-AC1200",
    device="MBP",
    duration=60,
    interval=1,
    notes="Test was conducted in close proximity to the router"
)
