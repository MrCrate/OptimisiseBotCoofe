import logging  
from telegram import Update  
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
                    level=logging.INFO)  

logger = logging.getLogger(__name__)  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  
    welcome_message = (  "👋 Привет! Мы — команда разработчиков, создающих ботов для автоматизации и улучшения работы. Наши решения помогают упростить взаимодействие с клиентами, повысить эффективность и обеспечить высокий уровень обслуживания. Если у вас есть вопросы, мы всегда готовы помочь!"
    )  
    await update.message.reply_text(welcome_message)  

def main():  
    TOKEN = '8143763376:AAFT8Jk_oYPsHDzbBROlT5xx5R_VYcNEbno'  
    application = ApplicationBuilder().token(TOKEN).build()  
    application.add_handler(CommandHandler("start", start))  
    application.run_polling()  

if __name__ == '__main__':  
    main()
