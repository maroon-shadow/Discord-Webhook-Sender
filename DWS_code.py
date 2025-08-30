import requests
import os
import time
import keyboard

ver = ("0.1.0")

if ver <= "1.0.0":
    if ver < "0.1.0":
        os.system("title Dc Webhook Sender: Alpha")
    else:
        os.system("title Dc Webhook Sender: Beta")
else:
    os.system("title Discord Webhook Sender")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def webhook():
    data = {}

    print("Webhook Info: \n")
    webhook_url = input("Enter webhook URL: ")

    # Validate webhook URL
    while not webhook_url.startswith("https://discord.com/api/webhooks/"):
        clear()
        print("Invalid URL \n")
        print("Webhook Info: \n")
        webhook_url = input("Enter a valid webhook URL: ")

    # Basic fields
    username = input("Enter bot username (opt): ")
    pfp = input("Enter bot pfp URL (opt): ")
    content = input("Enter a message: ")

    # Embed setup
    print("\nEmbed (opt): \n")
    title = input("Enter a title (opt): ")
    description = input("Enter a description (opt): ")
    colorhex = input("Enter a color in hex (opt, e.g., FF0000): ")

    # Parse hex color if valid
    if colorhex is not None:
        colorhex.strip()
        try:
            color = int(colorhex, 16)
        except ValueError:
            print("Invalid hex color, skipping...")

    # Build payload
    if content.strip():
        data["content"] = content
    if username.strip():
        data["username"] = username
    if pfp.strip():
        data["avatar_url"] = pfp

    embed = {}
    if title.strip():
        embed["title"] = title
    if description.strip():
        embed["description"] = description
    if color is not None:
        embed["color"] = color

    if embed:
        data["embeds"] = [embed]  # embeds must be a list

    # Send
    if data:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("✅ Sent!")
        else:
            print("❌ Failed:", response.status_code, response.text)
    else:
        print("⚠️ No data to send.")

webhook()

print("\nPress 'space' to send another or press 'esc' to exit...")

while True:
    if keyboard.is_pressed("space"):
        clear()
        webhook()
        time.sleep(0.3)
    elif keyboard.is_pressed("esc"):
        clear()
        print("Now exiting...")
        time.sleep(2)
        break