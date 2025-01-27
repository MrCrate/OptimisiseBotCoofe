import logging  
from telegram import Update  
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
                    level=logging.INFO)  

logger = logging.getLogger(__name__)  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  
    welcome_message = (  
        "👋 Привет! Мы — команда, разрабатывающая ботов для оптимизации работы кофеен. "  
        "Наши решения помогут вам упростить взаимодействие с клиентами, повысить эффективность "  
        "и обеспечить лучшее обслуживание. Если у вас есть вопросы, не стесняйтесь обращаться!"  
    )  
    await update.message.reply_text(welcome_message)  

def main():  
    TOKEN = '8143763376:AAFT8Jk_oYPsHDzbBROlT5xx5R_VYcNEbno'  
    application = ApplicationBuilder().token(TOKEN).build()  
    application.add_handler(CommandHandler("start", start))  
    application.run_polling()  

if __name__ == '__main__':  
    main()