import os
import logging
from datetime import datetime


class ChatUtils:
    @staticmethod
    def setup_directories():
        os.makedirs('logs', exist_ok=True)
        os.makedirs('chats', exist_ok=True)

    @staticmethod
    def setup_logging():
        logging.basicConfig(
            filename='logs/model_usage.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    @staticmethod
    def format_code_blocks(text):
        import re
        code_pattern = r"```[\w]*\n?(.*?)```"
        parts = re.split(code_pattern, text, flags=re.DOTALL)

        formatted_text = ""
        for i, part in enumerate(parts):
            if i % 2 == 0:
                formatted_text += part.strip() + "\n"
            else:
                formatted_text += "\n" + "=" * 40 + "\n"
                formatted_text += part.strip() + "\n"
                formatted_text += "=" * 40 + "\n"

        return formatted_text

    @staticmethod
    def save_chat_history(chat_history):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chats/chat_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=== QIYANAChat Диалог ===\n\n")
            for entry in chat_history:
                f.write(f"{entry}\n")

        return filename