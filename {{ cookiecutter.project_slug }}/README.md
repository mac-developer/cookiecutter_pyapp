# {{ cookiecutter.project_slug }}

Brief explanation

# Before use Makefile commands

You would need to prepare your own virtualenv environment before executing any makefile commands.

Example with virtualenvwrapper:

```
cd {{ cookiecutter.project_slug }}
mkvirtualenv -a `pwd` -p `which python` {{ cookiecutter.project_slug }}
```

Example with virtualenv:

```
cd {{ cookiecutter.project_slug }}
virtualenv -a `pwd` venv
source venv/bin/activate
```
