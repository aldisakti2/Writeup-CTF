#!/bin/bash

num=15 #skipping the latest s3 versioning or very top in output.txt
id=""
flag=""

# Read the contents of output.txt into an array
readarray -t data < ../output/output.txt

# Loop through the array elements
for ((i=0; i<${#data[@]}; i++)); do
    # Calculate the index to access
    index=$((num))

    # Check if the index is within the bounds of the array
    if (( index < ${#data[@]} )); then

	    # Get Version Id object
	    id=$(echo ${data[$index]} | awk '{print $2}' | tr -d ",")
	    echo $id

	    # Download object with Version Id
	    aws s3api get-object --bucket forever.lychnobyte.my.id --key "myheart.txt" --version-id $id myheart.txt --no-sign-request

	    # Insert flag value on object file into variable Flag
	    flag+=$(cat myheart.txt)

	    # Remove the file
	    rm myheart.txt
    fi

    # Increment num by 9 according to range between index of VersionId
    num=$((index + 9))

done

echo $flag
