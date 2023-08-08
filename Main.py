import re

from jira import JIRA

from BasicAuth import BasiAuth

if __name__ == "__main__" : 
    basicAuth = BasiAuth()
    basicAuth.process()