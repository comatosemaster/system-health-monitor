A local system monitoring tool written in Python that collects key system metrics — CPU usage, RAM, disk space, and top 10 largest folders — and automatically generates a structured HTML dashboard from live data.

Features

Collects real-time CPU, RAM, and disk stats
Scans directories to find top 10 largest folders
Stores system snapshots in timestamped JSON files
Converts JSON data into a dynamic HTML report using Jinja2
Opens report instantly in the browser
(Upcoming) Email automation for weekly or manual delivery


Technologies Used

System stats -	psutil
Size formatting -	humanfriendly
Templating engine -	jinja2
Data storage - json, datetime, os


How It Works

Collect system data from psutil
Save it into a timestamped JSON file
Render the data into template.html with Jinja2
Output a clean, dark-themed HTML dashboard
