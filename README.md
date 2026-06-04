## Im not responsible for any damage to infrastructure or reputation. This is not an exploit, and it should not cause any damage. Use at your own risk.

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

### How to rate each course alone ?
On the website, navigate to the course you want, then run the script for one course with the stars you want, complete the captcha and so on. You can not choose the stars for each question alone (then why use this).