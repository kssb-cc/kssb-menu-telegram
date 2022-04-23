from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import kssbmenu

updater = Updater("5371005183:AAFmbWVMP3_muBdSBvKwDQclf58G-jSL0Yk", use_context=True)
m = kssbmenu.kssb_menu()


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Welcome to the bot to get the KSSB menu!\n\nYou can type \"/menu\" to get the menu for the week.\n\nIf you have any complaints, questions etc, I am on Twitter @BrailleScreen.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("The only command available at the moment is \"/menu\". If typed, it will send back KSSB's lunch menu for the week.")

def menu(update: Update, context: CallbackContext):
	menu = ""
	update.message.reply_text("Obtaining the menu. This should take about 5 seconds.")
	result = m.download()
	for k, v in result.items():
		menu += f"Menu for {k}:\n{v}\n"
	update.message.reply_text(menu)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry; I don't know this command. Please type \"/help\" for a listing of available ones.")


updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("menu", menu))

#Handle unknown commands.
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))


updater.start_polling()
