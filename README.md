# [Twitter Sentiment Analysis](https://twittersentinel.herokuapp.com/new/)
Search for tweets and perform basic sentiment analysis.
- - - -
# Overview
This is a web-app made with [django](https://www.djangoproject.com/) using [tweepy](http://www.tweepy.org/) and [nltk](https://pypi.python.org/pypi/nltk/3.2.2) to analyze tweets on searched topic.

# Getting Started
### Prerequisites
To run locally, it is assumed that you have [python](https://www.python.org/) installed on your system.
### Development Guide
1. Create a virtual environment. `virtualenv venv`
2. Activate venv. `venv\scripts\activate.bat`
3. Install the requirements. `pip install -r requirements.txt`
4. Get the `SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, `CONSUMER_KEY`, `CONSUMER_SECRET` from here [here](http://apps.twitter.com/) and set it manually in [twitSent\settings.py](https://github.com/rahulpsd18/twitter-sentiment-analysis/blob/master/twitSent/settings.py) and [website\views.py](https://github.com/rahulpsd18/twitter-sentiment-analysis/blob/master/website/views.py).
5. Run the server. `python manage.py runserver`

### Hosting the application on Heroku
* Read [this](https://devcenter.heroku.com/articles/deploying-python) to learn deployment of django applications on heroku.
* Save the `SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, `CONSUMER_KEY`, `CONSUMER_SECRET` as environment variables.
Follow [this](https://devcenter.heroku.com/articles/config-vars) official documentation for help.

# Task List
- [ ] Provide option to export data in desired format
- [ ] Sharing option for individual tweets
- [ ] Filtering of tweets based on nature of it
- [ ] Make it a Single Page Application
- [ ] Implement Angular with Django
