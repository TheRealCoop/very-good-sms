# Very Good SMS
This application's name is derived from [Very Good Building Company](https://www.youtube.com/watch?v=G4GcRiMj0JE). Please use this application to send your SMS text messages to folks or do not. I am not a begger.

## Setup
1. Apply the environment variables defined in .envrc.example to your environment. I've done this with the use of [direnv](https://github.com/direnv/direnv), but this can be done however you'd like. Note - if you do choose to use .envrc, then you'll need to copy the .envrc.example file and create a new one called .envrc
2. `pip install -r requirements.txt`
3. Run the tests to ensure everything installed properly with `pytest`
3. `flask run`
4. Go to http://localhost:5000 and view the Very Good SMS application

## Run in Production Mode
Follow the steps in the Setup section to run this application in development mode. Note, *development mode will not actually send the SMS text*. You must run it in production to achieve that functionality. To run this app in production mode:
1. Install Heroku's CLI
2. Change the `FLASK_ENV` environment variable to be `production`
3. Run `heroku local`
