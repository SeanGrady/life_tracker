# LifeTracker
## Why a life tracker?

The primary motivation behind this project is that we are not always adept at recognizing cause/effect patterns that influence our lives. Some of these patterns take place over too long of a time period to be easily noticed. For example, daily vitamin D supplementation can take 2-3 months to noticeably affect mood in the best of cases, and up to a year to completely reverse severe deficiency. Other patterns occur over short timescales but still have too much lag between the cause and the effect to be easily noticed, especially if the link between the two doesn't seem obvious--like the mild "hangover" affect some people get the day _after_ eating too much sugar. Still other patterns affect "noisy" aspects of our lives that other factors have a stronger, more immediate (or more confoundingly random) influence on. Those of us with mood disorders are very familiar with this category: I feel a lot better today, it must be the new morning exercise routine! Or... is it the caffeine I had before lunch? Or that I got more sleep than usual last night? Maybe it was the ibuprofen I took yesterday, I've heard that can have an impact on mood...

The best way to begin addressing these kinds of disconnects is with data. It's a lot easier to notice that you always feel awful the day after you eat too much salt if you can graph your salt intake and daily well-being side by side. There are many different existing solutions that try to solve all or part of this issue, but I have found none that provide all of the three things that are, in my opinion, essential to success:

* Centralization: an easy way to get all your data in one place. Food, exercise, sleep, whatever else you happen to be tracking. In order to notice correlations and cause/effect relationships, you need to be able to work with all your data at the same time.

* Personalization: an easy way to track any metric that you want to improve. Weight is one example that's pretty well handled by existing solutions, but what about energy levels? Or productivity? Or chronic symptoms? Again, there are separate solutions for some of these, but nothing that I have found which makes it easy to define your own metrics and then compare them to anything or everything else you might be tracking.

* Pattern Recognition: an easy way to find correlations and cause/effect relationships in the data. It's all very well to put your food into a calorie tracking app every day, but as of the time of this writing only Chronometer has any ability to introspect your data for long term trends and none of the big 3 apps have a convenient way to determine that, for example, you don't sleep very well on days when you eat fewer than 1500 calories, or that your mood is much better when you drink more than four liters of water per day.

A very important secondary motivation for this project is that we are not always good at answering questions about ourselves and our past behavior. It's often hard to know if something you're trying to change is actually improving or worsening without being able to go back and look at past data.  I track my food consumption meticulously, and if you were to ask me to tell you how many calories I ate per day this week without checking I would be very confident, and also likely very wrong, in my answer.

In a perfect world, you would put all your data into this app and it would immediately pop up a helpful assistant with a dialogue box that said something like "It looks like you're trying to get rid of chronic headaches. You've been skipping lunch a lot, have you tried eating more frequently during the day?" While this is a wonderful long-term goal, it's certainly beyond the scope of a personal project done in one's spare time. We humans are a smart bunch, though, and usually we have a pretty good idea of what we might want to change. The hope behind this undertaking is that an easy, customization  and reliable means of tracking actions and target metrics is enough to help people more effectively help themselves.

## What this project aims to do

* Integrate with as many existing data collection and tracking solutions as possible. Examples are food tracking apps (like LoseIt, MyFitnessPal and Chronometer), or exercise tracking devices (like Fitbit or the Apple Watch).
* Provide a flexible interface for defining your own metrics and logging them. Tags that can be applied to any given day (for example, `headache` if you had a headache that day) are one possible method.
* Make it easy to compare any and all of your data to discover trends over time as well as correlations or cause/effect relationships.
* Allow other people (e.g. personal trainers, primary care doctors, family members) access to some or all of your data.

## What this project does not aim to do

* Any kind of machine learning or data analysis. This is something I would like to explore as I continue to flesh out the project, but the reality is that aside from some very basic statistical analysis there will almost certainly not be enough data to learn anything meaningful with these methods.
* Be anywhere near anything HIPAA-related. Currently, the HIPAA regulations say that broadly speaking as long as you don't bill health insurance or work with anyone who does, you are not a covered entity. Therefore, while providing the information in this app to anyone of your choice including your healthcare provider(s) should be easy for a user to do, working with anyone who is a HIPAA-covered entity or business associate is right out.

## What this project may aim to do in the future

* Integrate data that was originally HIPAA-covered PHI, such as lab results obtained with your primary care physician--think tracking cholesterol levels over time. I am not a HIPAA lawyer, but my understanding of the regulations is that if a user independently requests their medical data from their healthcare provider(s) and voluntarily uploads it to an app like this one, it is no longer covered under HIPAA. I will want to consult someone who _is_ a HIPAA lawyer before starting anything like this.
* Implement limited machine learning. Bag-of-words sentiment analysis on uploaded journal entries is one possible example of a method that may yield useful results, since it can use existing models and does not need to be trained directly on user data, of which there will be relatively little.

# Google Form Responses Intake

regarding email addresses: currently the only way to link gforms responses is via manually entered email addresses. The only way around this currently (afaik) is to either use a different form provider or use the apps script ResponseTrigger event, which would have to store the response somewhere (i.e. spin up the database). That's probably the correct way to do things if/when I actually have users but for now I want to keep the database off most of the time so manual email addresses it is.

Currently the project is set up to store google form responses in a google sheets spreadsheet as they come in. A more robust option in the future is to use a google apps script trigger to send form responses directly to the database when they're submitted, but this will require keeping the database instance running which will cost money. For the time being, a script to grab everything new from the spreadsheet and store it in the database is going to the solution.

UPDATE: Cloud SQL instances can be started/stopped programatically as detailed [here](https://cloud.google.com/sql/docs/postgres/start-stop-restart-instance). For the moment I'm still going to use a python script run locally and manually to grab everything from the Google Sheet(s) and do the ETL for two reasons:

* It's simpler, and I don't really _need_ it to be automated. I'll only need the data in the database to be current while I'm looking at it, so until there's a web interface and/or additional users, if I'm in a place where I need to see the data I'm also in a place where I can just run the script real quick to update the database.
* In order to do this with Apps Script, I would need to do ETL (and therefore keep a copy of the models in the database) in javascript in the apps script project. I'd rather have everything in python and in the project repo on github. So far the only exceptions are where I'm using GAS as a job scheduler that lives in the cloud instead of on my machine, and I would like to keep it that way. Also, I think doing the ETL in GAS would require having the models defined in two places at once, which is obviously not a good solution.

If and when the project turns into a real app with a website, I may move everything onto Google App Engine or something similar, at which point automating data intake from start to finish will make more sense.

# Google Cloud SQL Proxy
to launch the proxy:

```
./cloud_sql_proxy -instances=life-tracker-personal:us-west1:lifetracker-personal-psqldb=tcp:5432
```

to connect to the proxy with the psql client:

```
psql "host=127.0.0.1 sslmode=disable dbname=lifetracker-test user=postgres"
```

# Installing for local development

I highly recommend using a virtual environment (for example `virtualenv` optionally with `virtualenvwrapper`) for this.

To install this project in an editable state (for real though, in your virtual environment or uninstalling this can get messy), first install the requirements with

```
pip install -r requirements.txt
```

Then, from the project root directory, run

```
pip install -e .
```

which will install the package in setuptool's development mode.

To uninstall, you should be able to use

```
pip uninstall lifetracker-sgrady
```

But if, for some reason, this does not work, you should be able to manually uninstall the package by deleteing the .egg-link file in your python install's `site-packages/` folder and deleting the entry from `easy-install.pth` in the same folder.

# Useful Commands
`alembic revision --autogenerate -m "<MESSAGE>"`

# To Document:
Whatever the heck is giong on with the flask_login user_loader function. It can't be in the models.py file, because it needs to import the contextual session from crud.py, which imports base from the models.py file, which causes a circular import. So it should be in its own file (or in the flask_app/__init__.py or something, which is _clearly_ wrong), but then it never gets run because before it was only getting run because UserApp was being imported from models.py so the rest of models.py got run as a side effect. This also seems clearly wrong, but splitting into its own file means I have to make sure it gets run somehow, so I import its module in its sub-package's __init__.py.

installing selenium?

Why I'm using a context manager instesad of sqlalchemy's `scoped_session()` function. (https://stackoverflow.com/a/12223711)
