import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Default directory paths
watch_directory = "/Users/mastersteve/Downloads"
destination_directory = "/Users/mastersteve/Downloads/Music"

# Prefix to trigger the move
trigger_string = "y2mate.com - "


# Function to check if the file has finished downloading (i.e., if the file size is stable)
def is_file_fully_downloaded(file_path, stability_duration=30, check_interval=1):
    """Checks if the file size has remained stable for a given duration."""
    initial_size = os.path.getsize(file_path)
    stable_count = 0

    while stable_count < stability_duration:
        time.sleep(check_interval)  # Check every `check_interval` seconds
        current_size = os.path.getsize(file_path)

        if current_size == initial_size:
            stable_count += 1  # Size has not changed, increment stable count
        else:
            stable_count = 0  # Reset if the file size is changing

        initial_size = current_size  # Update initial size for next comparison

    return True  # File size has been stable for the specified duration


# Handler class to watch for new files
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        file_name = os.path.basename(file_path)

        # Check if the file name contains the trigger string
        if trigger_string in file_name:
            print(f"New file detected: {file_name}")

            # Wait until the file has finished downloading (size is stable)
            if is_file_fully_downloaded(file_path):
                # Remove the trigger string from the filename
                new_name = file_name.replace(trigger_string, "")

                # Get the full new path
                new_location = os.path.join(destination_directory, new_name)

                # Move the file to the destination folder with the new name
                shutil.move(file_path, new_location)
                print(f"Moved: {file_name} to {new_location}")
            else:
                print(f"File {file_name} is still downloading, skipping.")


# Set up the observer to watch the folder
event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, watch_directory, recursive=False)

# Start the observer
observer.start()
print(f"Watching for new files in: {watch_directory}...")

try:
    while True:
        time.sleep(1)  # Sleep for 1 second before checking again
except KeyboardInterrupt:
    observer.stop()
    print("\nStopped watching.")
observer.join()
