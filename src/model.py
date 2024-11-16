from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import logging
from tqdm import tqdm
import time
import re


class QIYANAModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.tokenizer = None
        self.model = None
        self.load_model()

    def load_model(self):
        print("\n" + "=" * 50)
        print("🚀 Инициализация QIYANAChat")
        print("=" * 50)

        steps = ['Подготовка токенизатора', 'Загрузка модели', 'Настройка параметров']
        for step in tqdm(steps, desc="💫 Прогресс загрузки"):
            if 'токенизатора' in step:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
            elif 'модели' in step:
                self.model = AutoModelForCausalLM.from_pretrained(self.model_path, trust_remote_code=True)
            time.sleep(1)

    def generate_response(self, prompt):
        if not prompt.strip():
            return "Пожалуйста, введите ваш вопрос или сообщение."

        logging.info(f"Processing: {prompt[:50]}...")

        try:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_length=200)
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return "Произошла ошибка. Попробуйте переформулировать запрос."