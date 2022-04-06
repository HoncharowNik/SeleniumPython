import string
import random
import logging as logger

def generate_random_email_and_password(domain=None, email_prefix=None):

    if not domain:
        domain = 'random.com'
    if not email_prefix:
        email_prefix = 'test'

    random_email_string_length = 10
    rand_password_length = 16

    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    random_password = ''.join(random.choices(string.ascii_letters, k=rand_password_length))
    email = email_prefix + '_' + random_string + '@' + domain

    logger.info(f'Generated random email: {email}')

    random_info = {'email': email, 'password': random_password}

    return random_info