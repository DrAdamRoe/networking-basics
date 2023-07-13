# Networking Introduction for Programmers

This repository is meant to accompany lectures given at C<>DE University. This repository contains many versions of low-level servers and clients, intended to demonstrate various principles of how web servers work, including sockets, HTTP requests, file servers, etc. 

## Before We Begin...

Students joining this workshop are expected to have:
- An interest in learning how the internet works
- Basic familiarity with the terminal and command line on your own computer (e.g. navigating directories, executing scripts)
- Node.js installed on your computer (ideally v18, but v16 or v20 is OK)
- Optional: Python3 installed on your computer (v3.8 or higher)
- Optional: git installed on your own computer, and the ability to clone a repository (nothing advanced required).
- A code editor / integrated development environment installed locally on your computer (e.g. Visual Studio Code).

To start, clone this repository into a working directory on your computer and open it in your code editor. You can do this by opening a New Window in Visual Studio Code selecting "Clone Git Repository", entering the URL of this repository (copied from your browser), and then selecting a local directory to save it to. You can also download this repository as a .zip file instead and open it from the downloads folder. 

##### Lesson 1: Client, Server, Sockets, Ports

Start the server (`$ python server.py `) and in another terminal, start the client (`$ python3 client.py `). This is running on the _localhost_.

Start the server again, and in another terminal, check that it is running using netstat: `netstat -an | grep 65432`.

Change the port of the server, and run the client. What happens? Now fix it so they can communicate again.
