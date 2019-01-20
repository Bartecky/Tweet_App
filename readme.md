**Twitter-like project**

**Start project**


Clone repository, create your own virtualenv and activate it.<br>
In terminal:<br>
`virtualenv -p python3 <your-dir-name>`<br>
next:<br>
`source <your-dir-name>/bin/activate`<br>
install requirements from project:<br>
`pip install requirements.txt`



Running:<br>
You need postgresql and db called 'twitter_db'<br>
_Apply migrations:_<br>
`python manage.py migrate`<br>
and run project:<br>
`python manage.py runserver`

IMPORTANT: 
Login feature to develop:
You have to create super user by:
`python manage.py createsuperuser` and refresh http://127.0.0.1:8000/
<hr>


Screens:
Main view<br>
<img src="src/images/newtweet.png" height=400>

User details<br>
<img src="src/images/details.png" height=400>

Hashtag #<br>
<img src="src/images/hashtag.png" height=400>

