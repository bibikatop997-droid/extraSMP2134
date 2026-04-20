import requests
import json
from datetime import datetime

# ⚠️ ВСТАВЬ СВОЙ URL ВЕБХУКА СЮДА
WEBHOOK_URL = "https://discord.com/api/webhooks/1494634771152764978/gBXicCL7nh2nPaAio4nX7vUDY6j9dtwPEzfHXGE_M-7e_CEkWBxKMP_gv8l2xKsWQ8ew"


def send_discord_notification(nickname, message=""):
    """
    Отправляет уведомление в Discord через вебхук
    """

    # Если сообщение пустое, используем стандартное
    if not message.strip():
        message = "Хочет получить доступ к Проходке"

    # Создаём красивое сообщение для Discord
    data = {
        "embeds": [
            {
                "title": "🎮 НОВЫЙ ЗАПРОС ОТ ИГРОКА!",
                "color": 0x57F287,  # зелёный цвет
                "fields": [
                    {
                        "name": "📛 Никнейм",
                        "value": f"`{nickname}`",
                        "inline": True
                    },
                    {
                        "name": "💬 Сообщение",
                        "value": message,
                        "inline": False
                    },
                    {
                        "name": "🖥️ IP сервера",
                        "value": "`d1.rustix.me:25212`",
                        "inline": True
                    },
                    {
                        "name": "⏰ Время",
                        "value": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "SMP Проходка | Бесплатный вайб"
                },
                "timestamp": datetime.now().isoformat()
            }
        ],
        "username": "SMP Проходка Бот",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2163/2163781.png"
    }

    # Отправляем запрос
    try:
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 204:
            print(f"✅ Уведомление для {nickname} отправлено!")
            return True
        else:
            print(f"❌ Ошибка! Код: {response.status_code}")
            print(f"Ответ: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False


# ============ ОСНОВНАЯ ПРОГРАММА ============

def main():
    print("=" * 50)
    print("🎮 SMP ПРОХОДКА — ОТПРАВКА УВЕДОМЛЕНИЙ")
    print("=" * 50)

    while True:
        print("\nВыбери действие:")
        print("1. Отправить уведомление")
        print("2. Выйти")

        choice = input("Твой выбор (1/2): ")

        if choice == "1":
            nickname = input("Введи никнейм игрока: ").strip()

            if not nickname:
                print("❌ Никнейм не может быть пустым!")
                continue

            message = input("Введи сообщение (Enter чтобы пропустить): ").strip()

            send_discord_notification(nickname, message)

        elif choice == "2":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")


if __name__ == "__main__":
    main()
