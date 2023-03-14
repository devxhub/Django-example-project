

'''
Choices for the Job model 
Job type default choices
gender default choices 

'''

JOB_TYPE = (
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
    ('Remote', 'Remote'),
    ('Paid Internship', 'Paid Internship'),
)

GENDER = (
    ('Only males are allowed to apply', 'Only males are allowed to apply'),
    ('Only females are allowed to apply', 'Only females are allowed to apply'),
    (' Both males and females are allowed to apply',
     ' Both males and females are allowed to apply'),
)


APPLICATION_STATUS = (
    ('Pending', 'Pending'),
    ('Shortlisted', 'Shortlisted'),
    ('Interview', 'Interview'),
    ('Interviewed', 'Interviewed'),
    ('Hired', 'Hired'),
    ('Rejected', 'Rejected'),
)
