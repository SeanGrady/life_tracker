# life_tracker
See also additional documentation in [the wiki](https://github.com/SeanGrady/life_tracker/wiki)

# Google Form Responses Intake

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

installin selenium?
