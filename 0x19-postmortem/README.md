Postmortem


Issue Summary:
Duration: March 1st, 2023, 9:00 AM EST - March 1st, 2023, 12:00 PM EST
Impact: The login service was down, and users were unable to access their accounts. Approximately 30% of users were affected.

Root Cause: A database migration script was improperly tested and caused a table to be locked, preventing access to user login information.

Timeline:

9:00 AM: The issue was detected when users started reporting login errors.
9:05 AM: The monitoring system sent an alert to the engineering team.
9:10 AM: The engineering team investigated the issue and found that the login service was down.
9:20 AM: The team assumed the issue was related to server capacity and began scaling up the login service.
9:30 AM: As the scaling did not improve the situation, the team began to investigate the database.
10:00 AM: The team identified that a database migration script was improperly tested and caused a table lock.
10:30 AM: The team attempted to fix the issue by manually unlocking the table.
11:00 AM: The team found that the manual unlock did not work and decided to revert the migration.
12:00 PM: The team successfully reverted the migration and the login service was restored.
Root Cause and Resolution:
The root cause of the issue was an improperly tested database migration script that caused a table lock, preventing access to user login information. The issue was resolved by reverting the migration and ensuring that all database migration scripts are thoroughly tested before deployment.

Corrective and Preventative Measures:
To prevent similar issues in the future, the following corrective and preventative measures will be taken:
Implement automated testing of all database migration scripts.
Improve monitoring of database locks and implement automatic alerts for any lock lasting more than a certain threshold.
Update incident response procedures to include database issues and ensure that the appropriate team members are notified promptly.
Tasks to address the issue:
Implement automated testing of all database migration scripts before deployment.
Improve monitoring of database locks and implement automatic alerts for any lock lasting more than 5 minutes.
Review and update incident response procedures to ensure they include database issues and involve the appropriate team members.

