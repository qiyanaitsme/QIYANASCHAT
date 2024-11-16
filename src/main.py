from model import QIYANAModel
from interface import Interface
from utils import ChatUtils
from config import MODEL_CONFIG
from tqdm import tqdm
import time


class ChatApplication:
    def __init__(self):
        self.utils = ChatUtils()
        self.utils.setup_directories()
        self.utils.setup_logging()

        self.interface = Interface()
        self.interface.display_welcome_menu()

        self.model = QIYANAModel(MODEL_CONFIG["path"])
        self.chat_history = []

    def run(self):
        while True:
            user_input = input("\n👤 Вы: ").strip()

            if not user_input:
                print("\n⚠️ Введите текст сообщения!")
                continue

            if user_input.lower() == 'exit':
                print("\n👋 До свидания!\n")
                break

            if user_input.lower() == 'save':
                filename = self.utils.save_chat_history(self.chat_history)
                print(f"\n📝 Диалог сохранен в: {filename}")
                continue

            self.chat_history.append(f"Вы: {user_input}")

            print("\n⚡ Генерация ответа: ")
            for i in tqdm(range(10), desc="🤔 Обработка", ncols=100):
                time.sleep(0.1)

            response = self.model.generate_response(user_input)
            formatted_response = self.utils.format_code_blocks(response)
            print(f"\n🤖 Модель:\n{formatted_response}\n")
            self.chat_history.append(f"Модель: {formatted_response}")

            print("-" * 50)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
