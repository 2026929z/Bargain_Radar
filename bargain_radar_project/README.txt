Bargain_Radar is an e-commerce application for PC's and mobiles.

Setup:

windows:
1- pull application file and clone them to your workspace directory
2- install setup tools 1.1.6 from https://pypi.python.org/pypi/setuptools/1.1.6 and extract the folder
3- on your command line change directory to setuptools-1.1.6
4- run "python ez_setup.py" on your command line
5- run "easy_install pip" on your command line
6- run "pip install -U django==1.7" on your command line to install django
7- run "pip install pillow" on your command line
8- run "pip install -r requirements.txt" on your command line to install all required packages from the requirements file
9- setup your virtual environment by installing virtualenvwrapper from https://pypi.python.org/pypi/virtualenvwrapper-win
10- run "mkvirtualenv <env's name>" to create your virtual environment
11- run "workon <env's name> to work on it

Unix:
1- pull application file and clone them to your workspace directory
2- install setup tools 1.1.6 from https://pypi.python.org/pypi/setuptools/1.1.6 and extract the folder
3- on your command line change directory to setuptools-1.1.6
4- run "sudo python ez_setup.py" on your shell
5- run "sudo easy_install pip" on your shell
6- run "sudo pip install -U django==1.7" on your shell to install django
7- run "pip install pillow" on your shell
8- run "pip install -r requirements.txt" on your shell to install all required packages from the requirements file
9- setup your virtual environment by running "pip install virtualenv" and then "pip install virtualenvwrapper" on your shell
10- run "mkvirtualenv <env's name>" to create your virtual environment
11- run "workon <env's name> to work on it


Using the application:

superuser's account details: username: "trader", password: "digital"

Bargain radar is an e-commerce website that allows its clients to freely post their deals and manage them whenever they want. Customers can add these deals to their
baskets and claim them.

Using as a customer:
register from the register page but don't tick the representative box. This box is special for our clients. Login after registration and click on offers that are
available in category tab or the index page. From the offer's page you can see the details of the offer and add it to your basket.

Using as a client:
register from the register page and tick the representative box. This will allow you to have extra permissions than other users by having extra tabs "add offer" that
allows you to add your own deals and "my offers" to view your current deals and manage them. Normally by ticking the box it shouldn't give you the extra permissions
right away but you must way to be validated as an authenticated seller but for demo reasons we made an exception. The reason behind it is to reduce spamming.