# Basic Testing Server and Config for Heroku.

## Setup
1. Clone this repo (or place files in a git repo)
2. Create an app in Heroku account, either using CLI or at https://dashboard.heroku.com/apps
3. Create git remote to herkou project. Remote address found in Heroku UI > Project > Settings > Heroku Git Url.
* (git remote add heroku <heroku_remote_address>)
* or use CLI: heroku git:remote -a <project_name>
4. Add all files, commit and push to heroku remote master branch.
* (git add *;git commit -m "initial commit";git push heroku master)
* App should install dependencies and boot
* Herkou CLI > use command 'herkou logs' to watch progress and requests.

## Other
* The server here is not production ready, just for testing.
* Flask API docs relevant to this: http://flask.pocoo.org/docs/0.12/api/