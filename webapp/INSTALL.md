#Installation

The recommended way to develop Python projects is to use virtual
environments for each project.

Setting up a virtual environment
--------------------------------
PyPi:
```bash
$ sudo apt-get install python-pip
```
Virtualenvwrapper:
```bash
$ pip install virtualenvwrapper
```

Add following to the shell's startup file(.zshrc, .bashrc, .profile, etc)

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/directory-you-do-development-in
source /usr/local/bin/virtualenvwrapper.sh
```

Create a new virtual environment with any name.

```bash
$ mkvirtualenv crisis
```

This command will create and switch to the virtual environment(the name of the environment will be prepended to the shell). If not, run the following command to switch.

```bash
$ workon crisis
```

Installation of the app requirements
------------------------------------

Application packages:
```bash
$ pip install -r requirements.txt
```

Setting up the Database
-----------------------
We have Sqlite3 database in Crisis Communicator:
```bash
$ sudo apt-get install sqlite3
```

After specifying the settings, run the following commands to create the database.
```bash
$ python manage.py syncdb
```

Collecting static files
-----------------------

Run the followinng command so that necessary static files are copied to STATIC\_ROOT.

```bash
$ python manage.py collectstatic
```

Running the development environment
-----------------------------------
If no errors are reported, the development server is ready.
```bash
$ python manage.py runserver
```

The development server will be now accessible from <http://127.0.0.1:8080/>


##Installed Apps
1. [django-bootstrap-toolkit](https://github.com/dyve/django-bootstrap-toolkit)
2. [django-haystack](https://github.com/toastdriven/django-haystack)
3. [Whoosh](https://github.com/JoeGermuska/django-whoosh)
