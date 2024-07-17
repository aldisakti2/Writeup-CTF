#!/bin/bash

# Loop through all compressed files matching the pattern
for file in attached_attachment*; do
    # Decompress the file
    zlib-flate -uncompress < "$file" > "output/$file"

    # Display the object content using git cat-file
    #echo "cat output/$file"

done
