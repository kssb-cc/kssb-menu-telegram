from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import load_dotenv
import admin, kssbmenu, os, sys, time

load_dotenv()

updater = Updater(os.getenv("TELEGRAM"), use_context=True)
m = kssbmenu.kssb_menu()


# Start commands.
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Welcome to the bot to get the KSSB menu!\n\nYou can type "/menu" to get the menu for the week.\n\nIf you have any complaints, questions etc, I am on Twitter @BrailleScreen.'
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'The only command available at the moment is "/menu". If typed, it will send back KSSB\'s lunch menu for the week.'
    )


def menu(update: Update, context: CallbackContext):
    menu = ""
    update.message.reply_text(
        "Obtaining the menu. This should only take a few seconds."
    )
    result = m.download()
    for k, v in result.items():
        menu += f"Menu for {k}:\n{v}\n"
    update.message.reply_text(menu)


def user_info(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(f"Username: {user['username']}\n\nID: {user['id']}")


def exit_bot(update: Update, context: CallbackContext):
    user = update.message.from_user
    if admin.is_administrator(user["id"]) == False:
        update.message.reply_text("Error: You are not a bot administrator.")
        return
    update.message.reply_text("Initiating exit process.")
    log(f"User {user['first_name']} {user['last_name']} is exiting the bot.")
    update.message.reply_text("Logged; exiting now.")
    sys.exit("Sys? ")
    os.system("kill " + os.getpid())


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Sorry; I don\'t know this command. Please type "/help" for a listing of available ones.'
    )


# End commands.


def log(what):
    # Used to log stuff to a file quickly. Also prints it out.
    f = open("logs/events.log", "a")
    f.write(f"{what}\n")
    f.close()
    print(what)


def main():
    log("Setting up stderr log.")
    errorlog = open("logs/error.log", "a")
    sys.stderr = errorlog
    log("Adding command handlers.")
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("menu", menu))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("user_info", user_info))
    updater.dispatcher.add_handler(CommandHandler("exit", exit_bot))
    # Handle unknown commands.
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    log("KSSB Menu Telegram Bot is running and pulling.")


if __name__ == "__main__":
    main()
