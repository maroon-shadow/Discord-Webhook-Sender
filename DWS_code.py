import requests
import os
import time
import keyboard

ver = "0.7.4"

if ver <= "1.0.0":
    if ver < "0.1.0":
        os.system(f"title Dc Webhook: Alpha - {ver}")
    else:
        os.system(f"title Dc Webhook: Beta - {ver}")
else:
    os.system(f"title Discord Webhook - {ver}")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def webhook():
    data = {}
    color = None

    print("Webhook Info: \n")
    webhook_url = input("Enter webhook URL: ")

    while not "https://discord.com/api/webhooks/" in webhook_url:
        clear()
        print("Invalid URL \n")
        webhook_url = input("Enter a valid webhook URL: ")

    username = input("Enter bot username (optional): ")
    pfp = input("Enter bot avatar URL (optional): ")
    content = input("Enter a message: ")

    # Embed info
    print("\nEmbed (optional): \n")
    title = input("Enter a title (optional): ")
    description = input("Enter a description (optional): ")
    colorhex = input("Enter a color in hex (optional, e.g., FF0000): ").strip()
    if colorhex:
        try:
            color = int(colorhex, 16)
        except ValueError:
            print("Invalid hex color, skipping...")

    # Optional advanced embed fields
    author_name = input("Author name (optional): ")
    author_url = input("Author URL (optional): ")
    author_icon = input("Author icon URL (optional): ")
    footer_text = input("Footer text (optional): ")
    footer_icon = input("Footer icon URL (optional): ")
    image_url = input("Image URL (optional): ")
    thumbnail_url = input("Thumbnail URL (optional): ")

    # Allowed mentions
    allowed_mentions = {"parse": ["everyone", "users", "roles"]}

    # Build payload
    if content.strip():
        data["content"] = content
    if username.strip():
        data["username"] = username
    if pfp.strip():
        data["avatar_url"] = pfp
    if allowed_mentions["parse"]:
        data["allowed_mentions"] = allowed_mentions

    embed = {}
    if title.strip():
        embed["title"] = title
    if description.strip():
        embed["description"] = description
    if color is not None:
        embed["color"] = color
    if author_name.strip():
        embed["author"] = {}
        embed["author"]["name"] = author_name
        if author_url.strip():
            embed["author"]["url"] = author_url
        if author_icon.strip():
            embed["author"]["icon_url"] = author_icon
    if footer_text.strip():
        embed["footer"] = {"text": footer_text}
        if footer_icon.strip():
            embed["footer"]["icon_url"] = footer_icon
    if image_url.strip():
        embed["image"] = {"url": image_url}
    if thumbnail_url.strip():
        embed["thumbnail"] = {"url": thumbnail_url}

    if embed:
        data["embeds"] = [embed]

    if data:
        try:
            response = requests.post(webhook_url.strip(), json=data)
            if response.status_code == 204:
                print("✅ Sent!")
            else:
                print("❌ Failed:", response.status_code, response.text)
        except Exception as e:
            print("❌ Error sending webhook:", e)
    else:
        print("⚠️ No data to send.")


webhook()
print("\nPress 'space' to send another or 'esc' to exit...")

while True:
    time.sleep(0.1)
    if keyboard.is_pressed("space"):
        clear()
        webhook()
        time.sleep(0.3)
    elif keyboard.is_pressed("esc"):
        clear()
        print("Now exiting...")
        time.sleep(1)
        break