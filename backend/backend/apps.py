from django.apps import AppConfig
import os


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        # Запуск только в режиме разработки
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from django.conf import settings
        if settings.DEBUG:
            try:
                from django.core.management import call_command
                print("🚀 Запуск автоматического заполнения данных...")
                call_command('seed_data')
            except Exception as e:
                print(f"⚠️ Ошибка при автозапуске seed_data: {e}")
