# HTTP log monitoring console program

A simple program that monitors HTTP traffic on your machine

<h2>Features:</h2>
<ul>
  <li>Consume an actively written-to w3c-formatted HTTP access log (https://en.wikipedia.org/wiki/Common_Log_Format)</li>
  <li>Every 10s, display in the console the sections of the web site with the most hits (a section is defined as being what's before the second '/' in a URL. i.e. the section for "http://my.site.com/pages/create' is "http://my.site.com/pages"), as well as interesting summary statistics on the traffic as a whole.</li>
  <li>Make sure a user can keep the console app running and monitor traffic on their machine</li>
  <li>Whenever total traffic for the past 2 minutes exceeds a certain number on average, add a message saying that “High traffic generated an alert - hits = {value}, triggered at {time}”</li>
  <li>Whenever the total traffic drops again below that value on average for the past 2 minutes, add another message detailing when the alert recovered</li>
  <li>Make sure all messages showing when alerting thresholds are crossed remain visible on the page for historical reasons.</li>
  <li>Write a test for the alerting logic</li>
  <li>Explain how you’d improve on this application design</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python</li>
  <li>pytest</li>
  <li>coverage</li>
</ul>

<h2>Running the project</h2>
```
python main.py /Users/flavio/Desktop/monitor/log/file.log
```

<h2>Running the tests</h2>

<h3>Install Requirements</h3>
```
sudo pip install -r requirements.txt
```

<h3>Run Tests</h3>
```
coverage run --source='.' -m py.test tests -v
```

<h2>Genereating Logs</h2>
On the foler /log type to start generating the log files:
```
python loggenerator.py /Users/flavio/Desktop/monitor/log/file.log
```

<h2>Architecture</h2>
![System](diagram.png)

<h2>Improvements</h2>
<ul>
  <li>Add database to store stats data instead of variables</li>
  <li>Allow more than one log file to be monitored</li>
  <li>On the Collector avoid sending individual data to the DB, create and aggregator to make batches of 10seconds. This is to decrease the number of access to the DB</li>
  <li>Divide agent, server-backend and server-frontend in three different projects</li>
  <li>Use a modern framework on the frontend (AngularJS, React, ...)</li>
  <li>Use a modern framework on the backend (Django, Flask, ...)</li>
  <li>Change interface components to bring warnings from defined period (eg. last 12 hours)</li>
  <li>User pagination on the interface modules and allow more registers</li>
  <li>Use a modern real-time bidirectional event-based communication to alert the frontend that the backend has changed (e.g. when a warning is created on the server to update the screen)
  <li>Create much more tests</li>
</ul>
