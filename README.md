# CodeHelper

An app to help Coders interact with Helpers.

Was built as a part of my Web Technologies mini project

## Features

-Helper/Coder can register on the site.

-The Helper can set his rate and his skills.

-Coders can search for helper with the relevant skills.

-They can contact each other.

-SMS Notifications

-End to end Internal Messaging system built from scratch. 

-WhatYouSeeIsWhatYou get profile editor.


## To run it locally
```sh
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```