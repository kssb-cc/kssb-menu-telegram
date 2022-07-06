# KSSB-Menu-Telegram

[Kansas State School for the Blind's Food menu](https://kssb.net/parents/menus) was sometimes annoying to navigate to; especially if you are lazy like myself.

This bot aims to run on a server somewhere, and request the week's menu for you. Takes a few seconds, rather than like 30.

## Usage
As the user, all one must do is type '/menu' into it and it will obtain it for you.

As one who wishes to run the code, it's as simple as:
* Obtain a Telegram bot token; outside of the scope of this readme. Create a file called `.env`. See `example_env` for an example.
* Clone this repo.
* `pip install -r requirements.txt`
* `python3 bot.py` or `run.bat` (Windows).

## Final notes
For more information (including initial work on obtaining the menu) see the [KSSB-Menu repo itself](https://github.com/kssb-cc/kssb-menu).

