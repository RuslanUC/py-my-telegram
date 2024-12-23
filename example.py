from asyncio import get_event_loop

from my_telegram import MyTelegram


async def main() -> None:
    phone_number = input("Phone number (in international format): ").strip()

    mytg = MyTelegram(phone_number)
    await mytg.send_code()

    password = input("Password: ").strip()
    await mytg.login(password)

    app = await mytg.get_app()

    print("App info:")
    print(f"  Api id: {app.api_id}")
    print(f"  Api hash: {app.api_hash}")
    print(f"  Title: {app.title}")
    print(f"  Short name: {app.short_name}")


if __name__ == "__main__":
    get_event_loop().run_until_complete(main())
