#!/bin/bash
zipfile="24107.zip"
while unzip -Z1 "$zipfile" | head -n1 | grep "\.zip$"; do
    next_zipfile="$(unzip -Z1 "$zipfile" | head -n1)"
    unzip -P "${next_zipfile%.*}" "$zipfile"
    zipfile="$next_zipfile"
done
