### Networking Introduction for Programmers

This repository is meant to accompany lectures given at C<>DE University.

##### Lesson 0: Python Installation (check)

You will need to have python 3 installed on your computer.

To check that you have a working install of python 3, execute `sanity/check.py`, you should see the following:

```
$ python3 sanity/check.py
You are sane. Whew.
```

If, instead, you see something like this, you are not using Python 3:

```
$ python sanity/check.py

insane!

This requires Python 3.x. You are using version 2.7
```

You may Python 3 installed and need to specify it (e.g. `python3 sanity/check.py`), or you may need to [Install Python 3](https://realpython.com/installing-python/).

##### Lesson 1: Client, Server, Sockets, Ports

Start the server (`$ python server.py `) and in another terminal, start the client (`$ python3 client.py `). This is running on the _localhost_.

Start the server again, and in another terminal, check that it is running using netstat: `netstat -an | grep 65432`.

Change the port of the server, and run the client. What happens? Now fix it so they can communicate again.
