from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
import sys
import sqlite3
import time

conn = sqlite3.connect('/usr/share/nginx/html/problems/Haiku_contest/sqlite/user.db')
c = conn.cursor()

while True:
    for row in c.execute('SELECT id FROM users WHERE status=1'):
        user = row[0]
        #print(user)
        c.execute('UPDATE users SET status=0, score=100 WHERE id=?', [user])
        conn.commit()
        login_url = "https://maidakectf2019.aokakes.work/problems/Haiku_contest/admin.php"
        url = "https://maidakectf2019.aokakes.work/problems/Haiku_contest/admin.php?id={}".format(user)

        cookie = {"name": "flag", "value": "MaidakeCTF{If_you_do_not_escape_properly_cookies_can_be_easily_stolen}"}

        options = FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)

        driver.get(login_url)

        driver.add_cookie(cookie)
        driver.get(url)
        driver.quit()

    time.sleep(60)

c.close()
