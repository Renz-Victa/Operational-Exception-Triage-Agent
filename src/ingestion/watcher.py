import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

error_count = 4

class NewFileHandler(FileSystemEventHandler):
  def on_created(self, event):
    if not event.is_directory:
      print(f"New file detected: {event.src_path}")

folder = "/data/inbound"
observer = Observer()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()

observer.join()

def watch_files():
  WATCH_FOLDER = "incoming"
  global error_count
  seen = set()
  while True:
    files = os.listdir(WATCH_FOLDER)
    for file in files:
      if file not in seen:
        seen.add(file)
        print(f"New file detected: {file}")
        folder(file)
    time.sleep(2)

def notify_admin():
  print("Admin has been notified.")

def errors():
  if error_count > 3:
    notify_admin()

def main():
  watch_files()
  notify_admin()
  errors()
  event_handler = NewFileHandler()
  observer.schedule(
    event_handler, 
    folder, 
    recursive=False
  )
  observer.start()
  observer.join()

if __name__ == "__main__":
  main()