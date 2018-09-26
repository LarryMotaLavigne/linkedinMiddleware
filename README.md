# Django LinkedIn Middleware

[![PyPI](https://img.shields.io/badge/pypi-v0.1.1-blue.svg)](https://pypi.org/project/django-linkedin-middleware/)
[![Build Status](https://travis-ci.com/Squalex/LinkedinMiddleware.svg?branch=master)](https://travis-ci.com/Squalex/LinkedinMiddleware)

Connect to the LinkedIn API.

## Installation

```bash
$ pip install django-linkedin-middleware
```

Just add `django-linkedin-middleware.middleware.LinkedinMiddleware` to your `MIDDLEWARE`.

## Settings


### Linkedin Configuration

You need to create an application on the linkedin developer pages to 
[https://www.linkedin.com/developer/apps](https://www.linkedin.com/developer/apps) to receive your credentials 

`LINKEDIN_APPLICATION_KEY` : the Client ID

`LINKEDIN_APPLICATION_SECRET` : the Client Secret
 
`LINKEDIN_APPLICATION_RETURN_CALLBACK` : the callback url (you should add the same url in the linkedin developer page)

`LINKEDIN_APPLICATION_PROFILE` : a table of different application permissions. Here's a list of the permissions : 
`['r_basicprofile', 'r_emailaddress', 'rw_company_admin', 'w_share']`. You could also add the permission 

### Application Configuration

`PAGES_WITH_LINKEDIN_AUTH_REQUIRED` : the list of all pages on which you should force an authentication. By default, it will be all the pages (example : `['*']`)

`PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED` : the list of all pages on which the authentication is disable.

## Thanks

I only made a middleware for simply connect to linkedin and display information in the session.
I based my work on the [python-linkedin](https://github.com/ozgur/python-linkedin) project. 