#!/bin/bash

set -Ce

SOURCE_DIR="leetcode"
DEST_DIR="leetcode"

mkdir -p "$DEST_DIR"

for file in "$SOURCE_DIR"/solution_*.py; do
    filename=$(basename "$file")

    # Extract the number from the filename
    number="${filename//[!0-9]/}"

    padded_number=$(printf "%05d" "$number")

    new_filename="solution_${padded_number}.py"

    batch_folder=$(printf "solutions_%05d" $((number / 300 * 300)))

    mkdir -p "$DEST_DIR/$batch_folder"

    mv "$file" "$DEST_DIR/$batch_folder/$new_filename"
done

echo "Files have been renamed and organized successfully."
