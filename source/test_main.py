import pytest
from main import *



def test_show_passwords(capsys):
    show_passwords([])

    captured = capsys.readouterr()
    assert captured.out == "You have 0 passwords saved\n"

def test_show_passwords_one(capsys):
    passwords2 = [
        {
            "website": "test",
            "username": "test",
            "password": "z*'o(qP=KG#b~(.+"
        }
    ]

    show_passwords(passwords2) 
    captured = capsys.readouterr()
    assert captured.out == "Passwords saved: \n\nWebsite/app: test, Username: test, Password: z*'o(qP=KG#b~(.+\n"

def test_show_passwords_two(capsys):
    passwords3 = [
        {
            "website": "test",
            "username": "test",
            "password": "z*'o(qP=KG#b~(.+"
        },
        {
            "website": "example",
            "username": "example",
            "password": "|bj[-hrtc-:#xgza"
        }
    ]
    show_passwords(passwords3)
    captured = capsys.readouterr()
    assert captured.out == "Passwords saved: \n\nWebsite/app: test, Username: test, Password: z*'o(qP=KG#b~(.+\nWebsite/app: example, Username: example, Password: |bj[-hrtc-:#xgza\n"

def test_remove_password(capsys):
    passwords = [
        {
            "website": "test",
            "username": "test",
            "password": "z*'o(qP=KG#b~(.+"
        },
        {
            "website": "example",
            "username": "example",
            "password": "|bj[-hrtc-:#xgza"
        }
    ]
    website = "website"
    username = "username"

    remove_password(passwords, website, username)
    captured = capsys.readouterr()
    assert captured.out == "\nWebsite and/or username not found, please check the list of passwords\n"

def test_remove_password_two(capsys):
    passwords = [
        {
            "website": "test",
            "username": "test",
            "password": "z*'o(qP=KG#b~(.+"
        },
        {
            "website": "example",
            "username": "example",
            "password": "|bj[-hrtc-:#xgza"
        }
    ]

    website2 = "test"
    username2 = "test"
    remove_password(passwords, website2, username2)
    captured = capsys.readouterr()
    assert captured.out == f"Removed password for website/app '{website2}' and username '{username2}'\n"
    
