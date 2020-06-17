# life_tracker

# Google Cloud SQL Proxy
to connect:
./cloud_sql_proxy -instances=life-tracker-personal:us-west1:lifetracker-personal-psqldb=tcp:5432

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
