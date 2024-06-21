#!/bin/bash

if [[ $# -ne 1 || ! -d $1 ]]
then
echo "Parametrul nu este un director!"
exit 1
fi

source ./config.sh $1

if [ ! -f "$LOG_FILE" ]
then
echo "Fisierul de log nu exista!"
exit 1
fi

CURRENT_DATE=$(date "+%Y-%m-%d")

REPORT="Raport Evenimente Monitorizare\n\nData: $CURRENT_DATE\n\nEvenimente inregistrate:\n"

while IFS= read -r line
do
REPORT+="$(echo "$line" | awk '{print "-",$2,$1,"-",$3}')\n"
done < "$LOG_FILE"

echo -e "$REPORT"
