pinger
======

This program is meant to aid in automating verification testing.  Today, this supports onePK by using CPAL, but it idea could easily be ported to use any API or even SSH.  Next steps would be to loop through any number of source routers to test connectivity to all of the destinations and store contents in a file.  Then parse the file to see which destinations are failing.

Sample output when running this:


cisco@onepk:~/apps/pinger$ python pinger.py
.-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.110
Success rate is 100 percent (5/5)
.-----------------------------------------------------
.-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.120
Success rate is 100 percent (5/5)
.-----------------------------------------------------
.-----------------------------------------------------
SOURCE: 10.1.1.110 DESTINATION: 10.1.1.130
Success rate is 100 percent (5/5)
.-----------------------------------------------------

Note:  using '.' in front of dashed lines to prevent auto-formatting in file.
