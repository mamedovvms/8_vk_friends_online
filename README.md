# Watcher of Friends Online

Displays a list of friends of the social network [VK.COM](https://vk.com) who are online. 
Login and password required


# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

#Example

```bash
$ python vk_friends_online.py

Please enter your login: mamedovvms@mail.ru
Please enter your password: # when you enter the password will not be displayed

Online friends
Petrov Ivan
Sokolov Vladimir

#If there is no one online, then a message will be displayed.
#No online friends
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
