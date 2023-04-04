#!/bin/bash
#read -p "Please Enter Path:" r1
#parent=$(dirname "$r1")
#cd "$parent"


function modify {

	# Prompt the user to enter the directory path to be monitored

	echo "Enter the directory path to be monitored:"

	read data

	# Check if the directory exists

	if [ ! -d "$data" ]; then

		echo "Error: Directory '$data' does not exist"

		exit 1

	fi

	# Monitor the directory for changes using inotifywait

	echo "Monitoring directory '$data' for changes..."

	while RES=$(inotifywait -r -e modify,create,delete,move $data); do

		echo " in Directory '$data' modification is done in file $RES at `date`"
		#cp  $RES ./output

	done

}

modify
