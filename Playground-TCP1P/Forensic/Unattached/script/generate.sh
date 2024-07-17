#!/bin/bash

# Loop through each file with the format attached_attachment<number>
for file in output/attached_attachment*; do
  # Get the SHA-1 hash of the file
  hash=$(sha1sum "$file" | awk '{print $1}')
  
  # Extract the first two characters of the hash as the directory name
  dir_name=${hash:0:2}
  
  # Extract the remaining characters of the hash as the file name
  file_name=${hash:2}
  
  # Create the directory inside objects/ if it doesn't exist
  mkdir -p ".git/objects/$dir_name"
  
  # Copy the file from the repo/ directory to the new location
  mv "about-git.dump/attachments/$file" ".git/objects/$dir_name/$file_name"
done
