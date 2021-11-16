# Django-Simple-Todolist-App
============================
-----------
A simple "ToDo List", built in Django and used to help understand how Django works and get more practice.

## Running the Project Locally
==============================
-----------
#### Follow the steps:

1. Relax and smile :)
2. Clone or Download the repository to your local machine:
  - ```git clone https://github.com/JoeDimumbi/Django-Simple-Todolist-App.git```
  
3. Install [pip]
  3.1. Install Python Pip on Ubuntu 20.04
  
  - Using the terminal:
  
    $ sudo apt update
    $ sudo apt install python3-pip
    
    The command above will also install all the dependencies required for building Python modules.
    When the installation is complete; verify the installation by checking the pip version:

    $ pip3 --version
    
   3.2. Install pip in macOS
   
   - Press Command + Space Bar and type in Terminal. Click the app icon to open a new terminal window.
   - Download pip by running the following command:
   
    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   - Install the downloaded package by running:
    
    $ python3 get-pip.py
   
   - Wait for the installation to finish. Now you have successfully installed pip on your Mac.
   
   3.3. Install pip in Windows
   - Download the get-pip.py (https://bootstrap.pypa.io/get-pip.py) file and store it in the same directory as python is installed.
   - Change the current path of the directory in the command line to the path of the directory where the above file exists.
   - Run the command given below:

    $ python get-pip.py
    
    - Voila! pip is now installed on your system.
    
4. Install the project dependencies:

    - ```pip install -r requirements.txt``` in your root project folder.
    
5. Apply the migrations:

    - ```python manage.py migrate```
6. Finally, Run your project:
    - ```python manage.py runserver```
7. See in the localhost; The project will be available at:
    - **127.0.0.1:8000**

8. You can change the *port* what django will run your project: 
    - ```python manage.py runserver 8080``` --> ```127.0.0.1:8080```


The source code is released under the [MIT License](https://github.com/JoeDimumbi/Django-Simple-Todolist-App/blob/master/LICENSE).
