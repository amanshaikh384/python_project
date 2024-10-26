# Desktop Notifier App
from plyer import notification
import time

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # You can provide a path to the icon file if needed
        timeout=10,  # The notification will stay on screen for 10 seconds
    )

if __name__ == "__main__":
    print("Desktop Notifier App")
    while True:
        try:
            title = input("Enter the notification title: ")
            message = input("Enter the notification message: ")
            interval = int(input("Enter the time interval (in seconds): "))
            
            if interval <= 0:
                print("Please enter a positive interval.")
                continue

            while True:
                desktop_notifier(title, message)
                time.sleep(interval)
        except ValueError:
            print("Invalid input. Please enter a valid number for the time interval.")
        except KeyboardInterrupt:
            print("Desktop Notifier App closed.")
            break
