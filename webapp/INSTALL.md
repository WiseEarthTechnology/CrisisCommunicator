#Development Environment

(If you want to use this code in a production environment, see below)

It's super-easy to set up our development environment.

To begin development, we recommend that you use vagrant.  That makes setting up the development environment super-easy, and also doesn't make any changes to your system.

## Collect Pre-Requisites

1. VirtualBox from www.virtualbox.org, or your OS's repositories.
2. Vagrant from www.vagrantup.com.  Find the packages on the website.
3. Git version control from www.git-scm.com or your OS's repositories.

## Get the Files

1. Create a folder for this project.
```bash
host:~$ mkdir ~/CrisisCommunicator
host:~$ cd CrisisCommunicator
```

2. Clone the Code
```bash
host:~/CrisisCommunicator$ git clone https://github.com/WiseEarthTechnology/CrisisCommunicator-Challenge.git
```

3. Start Vagrant
```bash
host:~/CrisisCommunicator$ vagrant up
```

4. It will download and install the precise64 virtual image, and then boot the system.  After booting, it will update the package lists, and then install `curl`.
5. After it's booted, log into the vagrant box by:
```bash
host:~/CrisisCommunicator$ vagrant ssh
```

6. Run the Adorno script.  It will set up the vagrant box, install requirements, and create a virtual environment.
```bash
vagrant:~$ curl -s https://raw.github.com/swiftarrow/Adorno/master/adorno.sh | bash
```

7. You may now begin development.  Since you're in a vagrant box, you do all the development on your host machine (including git versioning), and run the code on the vagrant machine.  See the readme for Adorno at https://github.com/swiftarrow/Adorno#tango-steps for a quick command reference.

8. Run the following commands to create the database.
```bash
vagrant:~/vagrant/webapp$ python manage.py syncdb
```

9. Run the followinng command so that necessary static files are copied to the STATIC\_ROOT configured in ```communicator/settings.py```.
```bash
vagrant:~/vagrant/webapp$ python manage.py collectstatic
```

10. If no errors are reported, the development server is ready.
```bash
vagrant:~/vagrant/webapp$ python manage.py runserver 0.0.0.0:8888
```
The development server will be now accessible from http://127.0.0.1:8888

Welcome Aboard!




#Production Environment

For a production environment, it is recommended that you follow these steps here: http://grokcode.com/784/how-to-setup-a-linux-nginx-uwsgi-python-django-server/


#Installed Apps
1. [django-bootstrap-toolkit](https://github.com/dyve/django-bootstrap-toolkit)
2. [django-haystack](https://github.com/toastdriven/django-haystack)
3. [Whoosh](https://github.com/JoeGermuska/django-whoosh)
