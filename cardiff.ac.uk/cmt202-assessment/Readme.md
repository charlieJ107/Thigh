# Distributed Library Management System for CMT202 Assessment

## Introduction
This is a distributed library management system that providing serveral functions: 
* Add / Delete Users
* Add / Delete Authors
* Add / Delete Book Copies
* Borrow / Return Books
* Check books borrowing status

## Prerequisites
* Python 3.10.4 (Maching the version of the university provided laptop)
* Pyro5 5.14

## Quick Start

0. Install Pyro5
```bash
pip install pyro5
```

1. Run the name server
```bash
python -m pyro5-ns
```

2. Run the server
```bash
python library.py
```

3. Run the test
```bash
python library_test.py
```