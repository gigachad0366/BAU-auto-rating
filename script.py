import requests as r
import argparse
from colorama import Fore, Style
from bs4 import BeautifulSoup
import re

parser = argparse.ArgumentParser(epilog='Automatic rating script for BAU rating website')

parser.add_argument('--url',help='Evaluation website root (to the /eval/ part)')
parser.add_argument('-c','--courses',help='Number of courses to rate')
parser.add_argument('-jid','--cookies',help='JSESSIONID for auth')
parser.add_argument('-s','--stars',help='Stars to rate with (from 1 to 5)')

args = parser.parse_args()

session = r.Session()

headers = {"Cookie":f"JSESSIONID={args.cookies}"}

for i in range(1, (int(args.courses) + 1)):
    if (i != 1):
        response = session.get(args.url + f"Evaluation.jsp", headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        captcha_text = soup.find(string=re.compile(r'أدخل الرقم الآمن التالي في المربع:'))
        if captcha_text: 
            numbers = re.findall(r'\d+', captcha_text)
            captcha_value = numbers[0] if numbers else None
            print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" Captcha value: {captcha_value}")
            payload = {
                    "authcode":f"{authcode}",
                    "captcha":f"captcha_value"
                        }
            response = session.post(args.url + f"EvaluationSubmit.jsp", data=payload, headers=headers)
            response = session.get(args.url + f"Finish.jsp", headers=headers)
        else:
            print(Fore.RED + "[*]" + Style.RESET_ALL + f" Failed to submit the captcha code")
            break
    print(Fore.BLUE + "[*]" + Style.RESET_ALL + f" Trying to get course {i} authcode...")
    response = session.get(args.url + f"Evaluation.jsp", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    authcode = soup.find("input", {"name": "authcode"})['value']
    print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" authcode: {authcode}")
    for o in range(0, 15):
        d = "{:02d}".format(o)
        print(Fore.BLUE + "[*]" + Style.RESET_ALL + f" Trying question {o}...")
        response = session.get(args.url + f"EvaluationSetAnswer.jsp?evalqno={d}&authcode={authcode}&evalans={args.stars}", headers=headers)
print(Fore.BLUE + "[+]" + Style.RESET_ALL + f" Finished")
