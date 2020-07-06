#!/bin/bash
APP=metrus
DEPLOY="/var/weblogic-external-data/$APP/deploy"

for filename in $DEPLOY/*.ear; do
    if [ -f "$filename" ] && [ "$filename" -nt "$NEWEST" ]; then
        NEWEST=$filename
    fi
done

if [[ "$NEWEST" =~ \ |\' ]]    #  slightly more readable: if [[ "$string" =~ ( |\') ]]
then
   echo "O arquivo $NEWEST possui espaço, por favor corrija!"
fi