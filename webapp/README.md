Crisis Communicator
===================
The **CrisisCommunicator** solves some of the problems faced by disaster responders and response coordinators. Normal communication systems often fail or are unreliable in disasters and crises, forcing responders to rely upon voice communication, simple radio messaging protocols, and expensive solutions like satellite communication.

The CrisisCommunicator builds on today's solutions, implementing a Disaster Management Communication Information System (the focus of this challenge), exchanging data messages via APRS, and providing a robust hardware device to access it's features. Every CrisisCommunicator operator will have access to information coming from all around the disaster area, in a distributed system with multiple redundancy.

By leveraging the power of **APRS** (Automatic Packet Reporting System), a technology with 20 years of active development and deployment in disaster situations, we are creating a distributed Disaster Management Communication Information System (DMCIS), aiding responders with automated communication and mapping of:

1. Live updates from all response teams
2. Refugee Center management (including person register, supplies, and algorithms to re-unite families
3. Messaging
4. Mapped Situation awareness through structured updates (road conditions, impending disasters, help needed, etc.
5. SOS signaling (just in case).

Based on open source technology, the CrisisCommunicator is not your average technology product: at Wise Earth Technology, we give back. Our business structure will integrate our core ethics of environmental, social, and economic sustainability (aka the "Triple Bottom Line"), living wages for direct and indirect employees, honesty, integrity, and dependability.

##How to get started

###Installation

(only for alpha version)

1. Clone the repository
> `git clone git@bitbucket.org:bithin/crisis-communicator.git`
2. Install sqlite3
> `sudo apt-get install sqlite3`
3. Install Django (v1.4.3)
    * Ubuntu repository provides Django v1.5, you can use pip to download v1.4.3
    > `sudo apt-get install python-pip && sudo pip install Django==1.4.3`
4. Install requirements
>`sudo pip install -r requirements.txt`
5. Setup Database
> `python manage.py syncdb`
6. Generating the static files
> `python manage.py collectstatic`
7. Run this in a console (run this command in a terminal always)
> `$ python manage.py runserver`

The development server will be now accessible from <http://127.0.0.1:8080/>


###Installed Apps
1. django-bootstrap-toolkit
2. django-haystack
3. Whoosh (its better to install whoosh v2.4 as v2.5 doesn't support spell checking)

