from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import nest_asyncio
from crypto import get_crypto_price
import asyncio


nest_asyncio.apply()

with open('token.txt', 'r') as f:
    token = f.read()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! This is crypto bot!")


async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        crypto_ticker = context.args[0].upper()
        price_info = get_crypto_price(crypto_ticker)
        await update.message.reply_text(price_info)
    else:
        await update.message.reply_text("Please provide a cryptocurrency ticker, e.g., /crypto BTC")
        

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
        Available commands for me:
        /start           -> Welcome message
        /help            -> Commands menu
        /crypto <Ticker> -> Crypto price
    """)


async def main():
    app = ApplicationBuilder().token("7946983291:AAExp2OvgCy5MBtzXta9IgKN7qWp3M8ir7o").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("crypto", crypto))
    
    await app.run_polling()


if __name__ == '__main__':    
    asyncio.get_event_loop().run_until_complete(main())
