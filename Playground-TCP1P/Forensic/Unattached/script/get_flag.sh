#!/bin/bash

flag=""

for id in $(git log --full-diff | grep commit | cut -d " " -f 2); do
	flag+=$(git show $id | tail -n 1 | tr -d "+")
done

echo $flag
