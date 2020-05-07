# peloton

written for python3. 
requires requests, json, datetime, pytz, sqlalchemy

the lists script will print some basic output to the cli, but depends on prettytable

it collects a bunch of peloton data from the api and dumps it into an sqlite database for your querying pleasure.

To collect, it'll need environment variables USER and PELOTONPASS defined, be sure to set those (e.g. with a shell script wrapper that starts the collect script after defining these variables, or put the whole thing inside a docker container.)
