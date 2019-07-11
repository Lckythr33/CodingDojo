#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Numpad1::
Send, created_at = models.DateTimeField(auto_now_add = True)
return

Numpad2::
Send, updated_at = models.DateTimeField(auto_now = True)
return

Numpad3::
Send, DATETIME
return

Numpad4::
Send, models.CharField(max_length = 60)
return

Numpad7::
Send, python manage.py makemigrations
return

Numpad8::
Send, python manage.py migrate
return

Numpad9::
Send, python manage.py shell
return

Numpad0::
Send, from apps.app_name.models import *
return

Numpad5::
Send, User.objects.create(first_name="", last_name= "", email="", password ="")
return

Numpad6::
Send, Product.objects.create(name="", img= "", cost="", min_contrib="")