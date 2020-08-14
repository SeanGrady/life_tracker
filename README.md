# life_tracker
See also additional documentation in [the wiki](https://github.com/SeanGrady/life_tracker/wiki)

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
