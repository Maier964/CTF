#!/bin/bash

current_zip = "24107.zip"

while unzip -Z1 "$current_zip" | grep "\.zip$";
do
	next_zip = "$(unzip -Z1 "$current_zip" | head -n1)"
	unzip -P "${next_zip%.*}" "$current_zip"
	current_zip = "$next_zip"
done
