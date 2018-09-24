# Django LinkedIn Middleware

Connect to the LinkedIn API.

Detailed documentation is in the "docs" directory.


## Installation
```
$ pip install django-linkedin-middleware
```



## Quick start

1. Add "LinkedinMiddleware" to your MIDDLEWARE setting like this::

    MIDDLEWARE = [
        ...
        'LinkedinMiddleware',
    ]

2. Select the wanted page to be accessible through this middleware