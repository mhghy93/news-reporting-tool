PROJECT DESCRIPTION:

A reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

AIM OF THIS PROJECT:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


INSTRUCTIONS TO RUN THIS PROJECT:

Step 1: Install virtualbox, You can download it from https://www.virtualbox.org/ (ignore if already installed)

Step 2: Install vagrant, You can download it from https://www.vagrantup.com/. (ignore if already installed)

Step 3: Download or Clone fullstack-nanodegree-vm repository. You can find the link to the fullstack-nanodegree-vm here.(https://github.com/udacity/fullstack-nanodegree-vm)

Step 4: Clone or download this project

Step 5: Open the terminal and type vagrant up and then type vagrant ssh

Step 6: Download the data from here https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Step 7: Unzip newsdata.zip and put the newsdata.sql file into the vagrant directory.

Step 8: Load the data by running:

        psql -d news -f newsdata.sql

Step 9: Go to the project directory by typing:
	
	    cd /vagrant/news-reporting-tool

Step 10: Run this project by typing: 

        python news_log.py



VIEWS USED IN THIS PROJECT:

    	CREATE VIEW total_logs AS
    	SELECT to_char(time, 'DD-MON-YYYY') AS date, COUNT(*) AS total
    	FROM log
    	GROUP BY date;

    	CREATE VIEW error_logs AS
    	SELECT to_char(time, 'DD-MON-YYYY') AS date, COUNT(*) AS error
    	FROM log
    	WHERE STATUS LIKE '%404%'
    	GROUP BY date;

