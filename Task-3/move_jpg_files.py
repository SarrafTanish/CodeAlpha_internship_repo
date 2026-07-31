
import os
import shutil
import sys


def move_jpg_files(source_folder: str, destination_folder: str) -> None:
    """Move every .jpg (and .jpeg) file from source_folder into destination_folder."""

    # 1. Make sure the source folder actually exists
    if not os.path.isdir(source_folder):
        print(f"Error: source folder does not exist -> {source_folder}")
        return

    # 2. Create the destination folder if it doesn't exist yet
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0
    skipped_count = 0

    # 3. Loop through every item in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Only act on files (skip sub-folders) with a .jpg/.jpeg extension
        if os.path.isfile(source_path) and filename.lower().endswith((".jpg", ".jpeg")):
            destination_path = os.path.join(destination_folder, filename)

            # Avoid overwriting a file that already exists at the destination
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                    counter += 1

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {destination_path}")
            moved_count += 1
        else:
            skipped_count += 1

    print(f"\nDone. {moved_count} .jpg file(s) moved, {skipped_count} item(s) skipped.")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        src, dst = sys.argv[1], sys.argv[2]
    else:
        # Fallback to interactive input if no command-line args were given
        src = input("Enter source folder path: ").strip()
        dst = input("Enter destination folder path: ").strip()

    move_jpg_files(src, dst)
