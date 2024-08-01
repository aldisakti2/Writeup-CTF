#!/bin/bash

figlet "Intechfest Curl Service"

# Generate a random directory name
random_dir=$(mktemp -d /tmp/curl_service.XXXXXXXXXX)

# Change the current working directory to the random directory
cd "$random_dir"

while true; do
    read -e -p "Enter the curl command (or type 'exit' to quit): " curl
    if [[ "$curl" == "exit" ]]; then
        break
    fi
    if [[ "$curl" == curl* ]]; then
        $curl
    else
        echo "Invalid command. Please start with 'curl'."
    fi
done

# Clean up the temporary directory
rm -rf "$random_dir"
