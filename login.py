#!/usr/bin/env python3
import cgi
import cgitb
import secret
import os
import sys
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie

cgitb.enable()

storage = cgi.FieldStorage()

username = storage.getfirst("username")
password = storage.getfirst("password")

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None

if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_check = cookie_username == secret.username and cookie_password == secret.password

if cookie_check:
    username = cookie_username
    password = cookie_password

form_check = username == secret.username and password == secret.password


print("Content-Type: text/html")
if form_check:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

if not username and not password:
    print(login_page())
elif not form_check:
    print(after_login_incorrect())
else:
    print(secret_page(username, password))
