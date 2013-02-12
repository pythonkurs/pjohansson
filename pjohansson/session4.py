"""Module for Session 4 Assignment. Tools for collecting commit information
of the pythonkurs repo and creating data frame of it.

'get_commit_dataframe' creates the desired DataFrame.
'most_common_time' parses it and prints the most common weekday and hour."""

import os
import requests
from collections import Counter, namedtuple
from pandas import DataFrame, Series
from dateutil import parser

class github_repository(object):
    """A Github repository."""

    def __init__(self, name, url):
        self.url = url
        self.name = name

    def get_commits(self, username, password):
        """Get commit messages and times of repository and returns
        as a Series."""

        # Download and extract commit history
        commit_url = self.url + '/commits'
        raw_data = requests.get(commit_url, auth = (username, password))

        # Check if download correct
        if raw_data.status_code != 200:
            print "Could not download data from '%s'." % commit_url
            return

        full_commit_data = raw_data.json()

        # Initiate lists for dates and messages
        dates = []; messages = [];

        # Read and parse date and message
        for commit in full_commit_data:
            date_raw = commit['commit']['committer']['date']
            dates.append(parser.parse(date_raw))
            messages.append(commit['commit']['message'])

        return Series(messages, index = dates)

class github_organisation(object):
    """A class for a Github organisation."""

    def __init__(self, organisation = 'pythonkurs'):
        self.url = 'https://api.github.com/orgs/' + organisation.strip('/')

    def get_repositories(self, username, password):
        """Get repository names and url's of organisation. Supply username
        and password to authenticate."""

        authentication = (username, password)
        repos_url = self.url + '/repos'
        raw_data = requests.get(repos_url, auth = (username, password))

        # Control download status
        if raw_data.status_code != 200:
            print "Could not download data from server."
            return

        # Initiate repository dictionary
        repositories = {}

        full_repository_data = raw_data.json()

        for repository in full_repository_data:
            name = repository['name']
            url = repository['url']

            repositories[name] = github_repository(name, url)

        return repositories

    def get_commit_dataframe(self, username, password):
        """Collect commit data from repositories in organisation into a
        DataFrame. Supply username and password to authenticate."""

        # Get all repositories
        repositories = self.get_repositories(username, password)

        # Initiate empty dictionary for DataFrame
        commit_data = {}

        # For all repositories, get commit messages and dates as series,
        # add to dictionary
        for repo in repositories:
            commit_data[repo] = repositories[repo].get_commits(username,
                    password)

        return DataFrame(commit_data)

def get_commit_dataframe(username, password):
    """Create and return a DataFrame of commits for Assignment 4. Github
    username and password required for authentication - the latter can
    be supplied in different ways, 1) By giving the path to a file containing
    the password in plaintext, or 2) As a regular function argument."""

    # Get password if file entered
    if os.path.exists(password):
        with open(password) as secret_file:
            password = secret_file.read().strip()

    pythonkurs = github_organisation()

    return pythonkurs.get_commit_dataframe(username, password)

def most_common_time(dataframe):
    """Prints the most common day and time of commits in a DataFrame."""

    commit_times = dataframe.index

    weekday = get_most_common_weekday(commit_times)
    hour = get_most_common_hour(commit_times)

    print "The most common day to commit has so far been %s." % weekday
    print "The most common time has been between %d:00-%d:00." % (hour, hour+1)

    return

def get_most_common_weekday(of_list):
    """Returns the most common week day of a list of dates."""

    weekdays_list = of_list.weekday
    weekday_num = get_most_common_element(weekdays_list)

    return get_weekday(weekday_num)

def get_most_common_hour(of_list):
    """Returns the most common hour of a list of dates."""

    hours_list = of_list.hour

    return get_most_common_element(hours_list)

def get_most_common_element(of_list):
    """Returns the most common elements of a list."""

    return Counter(of_list).most_common(1)[0][0]

def get_weekday(day):
    """Returns the weekday name of a given number."""

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']

    return week[day % 7]
