# AirBnB clone - The console

### This is our first step towards building a we application!

---
## Description:

Same as our previous _Shell Project_, the __console__ is a command interpreter for our AirBnB clone strictly limited to methonds we create in this case the __console__ will help us manage, retrieve, update and delete objects from a file, database, etc.

### Instructions:
Once the repo has been pulled...

To start your console execute the __console.py__ file and press enter as shown:
```bash
$ ./console.py
(hbnb)
```
As described before once inside the __console__ the user will be able to: 

* create
* destroy (delete)
* show
* update

Objects from a file, database, etc.

As well in the __console__ you can see all the commands available using the __help__ command as shown:
```bash
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 

```
By typing the command __help <topic>__ a detailed help description is displayed:

```bash
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit

        Exits the program using quit command

        Usage: quit
        
(hbnb) 

```

## Command descriptions:

* __create__ - creates a new instance, if successful prints the ID of the new instance.
```bash.
(hbnb) help create

        Creates a new class instance, if sucessful it prints the ID of
        the new instance.

        Usage: create <class_name>"
        
(hbnb)
```
* __destroy__ - Destroys/deletes an instance based on the given Class and the ID.
```bash
(hbnb) help destroy

        Destroys/deletes an instance based on the given Class and the ID

        Usage: destroy <class_name>"
        
(hbnb) 
```
* __show__ - Shows the string representation of an instance based on the given Class and ID.
```bash
(hbnb) help show

        Shows the string representation of an instance based on the
        given Class and ID

        Usage: show <class_name>
        
(hbnb) 
```
* __update__ - Updates an instance based on the Class name and Id by adding or updating an attribute.
```bash
(hbnb) help update

        Updates an instance based on the Class name and ID by adding
        or updating an attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        
(hbnb) 
```
* __all__ - Prints all objects of a specific type, or all objects if no Class is specified
```bash
(hbnb) help all

        Prints all objects of a certain type, or all objects if no Class
        was specified.

        Usage: all <class name>
        
(hbnb) 
```

## Unittest:
All test codes present in the __*test*__/ directotr. 

Tested with python unit test, for how to stars, use and stability using command as shown:
```bash
$ python3 -m unittest discover test
```

## Contributors:
* Gustavo Hornedo
* Jared Beguelin
* Angel Gonzalez
#### console v.0.1
