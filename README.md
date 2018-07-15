# Some Flasky things

This demonstrates a few things with flask

- SQLAlchemy with postgres database
- JQuery POST requests
- Deploy in Docker


## Setup and deploy
- You will probably want to do this on your DO box where Docker is easy to install. Look up how to install docker here [Docker Documentation](https://docs.docker.com/engine/installation/)
- Git clone the existing template repository.
`app/requirements.txt` and `app/conda-requirements.txt`  contain some default settings which will be installed by `pip` and `conda` respectively.
- There is some boilerplate HTML in `app/templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to auto-generate a name.
- Login to container with `heroku container:login`
- Deploy to Heroku: `heroku container:push web`
- Release image: `heroku container:release web`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).
