import os
import re

def remove_concurrent_text(directory, text_to_remove):
    """
    Rename files in the specified directory by removing specific consecutive duplicate text in filenames.

    Args:
        directory (str): Path to the directory containing the files.
        text_to_remove (str): The specific text to remove when consecutive.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Escape the text to remove for regex
    escaped_text = re.escape(text_to_remove)

    success = False

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Ignore directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Use regex to find and remove consecutive duplicate text
        pattern = rf'({escaped_text})(?:\s*\1)+'
        new_filename = re.sub(pattern, r'\1', filename)

        # Only rename if the name changes
        if new_filename != filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                success = True
            except Exception as e:
                print(f"Failed to rename '{filename}': {e}")

    if success:
        print("All applicable files were successfully renamed.")
    else:
        print("No files were renamed.")

if __name__ == "__main__":
    # Replace with your target directory
    target_directory = input("Enter the directory path: ").strip()
    text_to_remove = input("Enter the text to remove if consecutive: ").strip()
    remove_concurrent_text(target_directory, text_to_remove)
