import re

from jira import JIRA

class BasiAuth() :

    def __init__(self) : 
        try : 
            # (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
            self._jira = JIRA(server="https://jira.atlassian.com")
            # Get all projects viewable by anonymous users.
            self._projects = self._jira.projects()
            # Sort available project keys, then return the second, third, and fourth keys.
            self._projectKeys = sorted(project.key for project in self._projects)[2:5]
        except Exception as err :
            print('Erreur initializing BasicAuth')
    def process(self) : 
        try :
            # Get an issue.
            issue = self._jira.issue("JRA-1330")
            
            # Find all comments made by Atlassians on this issue.
            atl_comments = [
                comment
                for comment in issue.fields.comment.comments
                if re.search(r"@atlassian.com$", comment.author.key)
            ]

            # Add a comment to the issue.
            self._jira.add_comment(issue, "Comment text")

            # Change the issue's summary and description.
            issue.update(
                summary="I'm different!", description="Changed the summary to be different."
            )

            # Change the issue without sending updates
            issue.update(notify=False, description="Quiet summary update.")

            # You can update the entire labels field like this
            issue.update(fields={"labels": ["AAA", "BBB"]})

            # Or modify the List of existing labels. The new label is unicode with no
            # spaces
            issue.fields.labels.append("new_text")
            issue.update(fields={"labels": issue.fields.labels})

            # Send the issue away for good.
            issue.delete()

            # Linking a remote jira issue (needs applinks to be configured to work)
            issue = self._jira.issue("JRA-1330")
            issue2 = self._jira.issue("XX-23")  # could also be another instance
            self._jira.add_remote_link(issue.id, issue2)
        except Exception as err : 
            print ('Error processing BasicAuth')