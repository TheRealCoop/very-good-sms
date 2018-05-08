# Very Good SMS
This application's name is derived from [Very Good Building Company](https://www.youtube.com/watch?v=G4GcRiMj0JE). Please use this application to send your SMS text messages to folks or do not. I am not a begger. If you choose to, then you can send one text at a time to one person of your choosing.

## Setup
1. Ensure you're using Python 3.6 or above, because f-strings are used.
2. Apply the environment variables defined in .envrc.example to your environment. I've done this with the use of [direnv](https://github.com/direnv/direnv), but this can be done however you'd like. Note - if you do choose to use .envrc, then you'll need to copy the .envrc.example file and create a new one called .envrc
3. `pip install -r requirements.txt`
4. Create a file called `database/dev.db`
5. Migrations - `flask db upgrade`
6. `flask run`
7. Go to http://localhost:5000 and view the Very Good SMS application

## Run in Production Mode
Follow the steps in the Setup section to run this application in development mode. Note, *development mode will not actually send the SMS text*. You must run it in production to achieve that functionality. To run this app in production mode:
1. Change the `FLASK_ENV` environment variable to be `production`
2. Create a file called `database/prod.db`
3. Run `flask db upgrade` to migrate your production database
4. Add `TWILIO_AUTH_TOKEN` and `TWILIO_ACCOUNT_SID` to your environment variables
5. Run `flask run`


## Tests
1. Create a file called `database/test.db`
2. Run `pytest`
