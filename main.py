from aiogram import executor
from handlers import dp


def main():
    executor.start_polling(dp, skip_updates=False)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        main()
