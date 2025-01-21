import os

# Default file path
# default_directory = "/Users/mastersteve/Downloads/Music"
default_directory = r"C:\Users\steve\Downloads\Music"


# Prompt the user to use the default path or enter their own
use_default = (
    input(f"Do you want to use the default path: {default_directory}? (yes/no): ")
    .strip()
    .lower()
)

# Determine the directory to use
if use_default == "yes":
    directory = default_directory
else:
    directory = input(
        "Enter the path to the folder containing your music files: "
    ).strip()

# Check if the selected path is valid
if not os.path.exists(directory):
    print("Error: The selected path does not exist. Please check and try again.")
else:
    # Prompt the user to enter the prefix or string to remove
    prefix_to_remove = input(
        "Enter the prefix or string to remove from filenames (including spaces): "
    ).strip()

    # Variable to track if any files were renamed
    renamed_files = False

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file name starts with the specified prefix
        if filename.startswith(prefix_to_remove):
            # Remove the prefix from the file name
            new_name = filename.replace(prefix_to_remove, "", 1)
            # Get the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: "{filename}" to "{new_name}"')
            renamed_files = True

    # Check if no files were renamed
    if not renamed_files:
        print("All files are clean!")
    else:
        print("Renaming completed!")
