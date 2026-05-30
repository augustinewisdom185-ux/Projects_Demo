"""This code prevents hacker from introding into a database."""

emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email.replace('DROP TABLE USERS', 'wisdom@gmail.com'):
        print('SQL Injection: Hacker alert')
        continue
    print(f'Processing emails: {email}')
