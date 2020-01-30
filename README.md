# For starting:


**Step #1:**

*  `git clone git@github.com:stepanenko-ys/blank_django.git` - SSH
*  `git clone https://github.com/stepanenko-ys/blank_django.git` - HTTP

*  **  **

**Step #2:**

**Now you need to go to the "develop" branch**

*  `git checkout develop`

*  **  **

**Step #3:**

**Now you need to install all the libraries and dependencies**

*  `pip install -r requirements.txt`

*  **  **

**Step #4:**

**Enter this command:**
*  `python manage.py makemigrations`
*  `python manage.py migrate`
*  `python manage.py loaddata fixtures/*.json`
*  `python manage.py runserver`

**Note: Fixture "users.json" create custom superuser with the name "admin" and the password "admin"**
*  **  **
