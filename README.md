# life_tracker

Currently the project is set up to store google form responses in a google sheets spreadsheet as they come in. A more robust option in the future is to use a google apps script trigger to send form responses directly to the database when they're submitted, but this will require keeping the database instance running which will cost money. For the time being, a script to grab everything new from the spreadsheet and store it in the database is going to the solution.

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

Then run

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
