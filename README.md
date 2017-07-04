# inet-speed

### Problem

I was having really atrocious internet speeds in my bedroom. My download speed was roughly `5 mbps` while my upload speed was sometimes as bad as `0.5 mbps`. I was manually testing this using a tool I found online but it was taking me a few minutes just to collect a single row of data. It was less than ideal and I was wasting a plethora of my time. I knew I needed to collect a lot of data to empirically prove that the new router I purchased was actually worse than my current despite the specifications stating that it would preform better.

### Solution
To automate this task I knew I would need an API to test my internet speed. I quickly did some research and found [speedtest-cli](https://github.com/sivel/speedtest-cli) and [pyspeedtest](https://github.com/fopina/pyspeedtest). Both seemed like reasonable options but I ultimately chose pyspeedtest because of its simple API and zero configuration required.

After I had chosen the API it was time to start implementing. Initially, I wrote the output to a csv file and copied it over to a Google doc. That got old fast so I looked for a Python API client for Google docs. Once the Google docs API client was set up I began writing my data directly to Google docs removing all manually aspects of this task aside from running it.

While the scripts ran on various devices I would go run errands or do some chores. I did make a __substantial__ error, if any one of the `SpeedTest#ping()`, `SpeedTest#download()` or `SpeedTest#upload()` were to fail to connect to the test server the whole script would crash. That was a problem because if the script crashes it won't write any of its data to Google docs.

This error became quite frustrating while testing poor connections because I would essentially lose all data collect up until that point. Since I only write the data once, after I have collected it all from the different tests the only solution was to `try-catch` the individual test. Now, the script would not crash on an individual test failure and it would continue trying to collect data.


### Analysis
I collected 313 rows of data. Manually collecting data took me approximately 3 minutes per row. To collect 313 rows of data it would have taken me roughly 16 hours. I spent 4 hours writing the script (2 of which was wrestling with and learning the Google Docs API), I spent 2 hours doing analysis of the data and I probably spent another hour or so administering the scripts on various devices while doing other things. Meaning, in total, I spent 7 hours on this task and saved myself 9 hours of time if I were to collect as much data.

The data collected result in me empirically proving that my newly purchased router was actually slower than my current router. I quickly went to the store and bought a higher quality router. I am happy to inform you that my internet speeds are roughly `80 mbps` and `20 mbps` for download and upload respectively. Not too bad for being behind 4 walls and as far away from the router as you possibly can be in my house.
