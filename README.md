# BAU-auto-rating
This is a script for automatically solving the annoying BAU "mandatory survey" that prevents the students from accessing the university's student interface.

The usage is simple:
```
Usage: eval.py [-h] [--url URL] [-c COURSES] [-jid COOKIES] [-s STARS]

options:
  -h, --help            show this help message and exit
  --url URL             Evaluation website root (to the /eval/ part)
  -c COURSES, --courses COURSES
                        Number of courses to rate
  -jid COOKIES, --cookies COOKIES
                        JSESSIONID for auth
  -s STARS, --stars STARS
                        Stars to rate with (from 1 to 5)

Automatic rating script for BAU rating website
```
To install depedencies:
```pip3 install -r requirements.txt```

---

### How to get the JSESSIONID cookie ?
After logging in, open the developer panel (F12) and navigate to storage, copy the value for the JSESSIONID key.
