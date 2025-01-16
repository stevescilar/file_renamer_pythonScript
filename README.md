# Watchdog

## Description
The Watchdog script monitors a specified directory for new `.mp3` files that contain a specific trigger string in their names. Once a new file is detected, it checks if the file has finished downloading and then renames the file by removing the trigger string before moving it to a designated destination directory.

## Requirements
- Python 3.x
- `watchdog` library (install via `pip install watchdog`)

## Usage
1. Set the `watch_directory` variable to the directory you want to monitor (default is `"/Users/mastersteve/Downloads"`).
2. Set the `destination_directory` variable to the directory where you want to move the renamed files (default is `"/Users/mastersteve/Downloads/Music"`).
3. Set the `trigger_string` variable to the prefix that triggers the move (default is `"y2mate.com - "`).
4. Run the script:
   ```bash
   python Watchdog.py
   ```

## License
This project is licensed under the MIT License.
