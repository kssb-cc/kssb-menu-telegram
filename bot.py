from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5371005183:AAFmbWVMP3_muBdSBvKwDQclf58G-jSL0Yk", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Welcome to the bot to get the KSSB menu!\n\nYou can type \"/menu\" to get the menu.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("The only command available at the moment is \"/menu\".")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry; I don't know this command. Please type \"/help\" for a listing of available commands.")


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands


updater.start_polling()
