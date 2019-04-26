##MagenticAI Test Task

#Installing

Create a virtual env and run
```
$ pip install -r requirements.txt
```

#To run test task by linux command line
```
$ export FLASK_APP=app.py

$ flask run
```

To display all games category and names from _https://play.google.com/store/apps/category/GAME_ :
[see all games](http://127.0.0.1:5000/games)

_http://127.0.0.1:5000/games/<your_substring>_ to filter games name by substring