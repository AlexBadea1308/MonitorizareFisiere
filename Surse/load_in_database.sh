#!/bin/bash

if [[ $# -ne 2 || ! -d $1 ]]
then
echo "Parametrul nu este un director!"
exit 1
fi

exists=`file $2 | egrep -wo "database"`

if [[ -z "$exists" ]]
then
echo "Al doilea parametru trimis nu este o baza de date!"
exit 1
else
source ./config.sh $1 $2
fi

echo "Director monitorizat: $MONITORED_DIR"
echo $DB_FILE

inotifywait -t $REPORT_INTERVAL -m -r -e $EVENTS --format '%w%f %e %T' --timefmt '%Y-%m-%d %H:%M:%S' "$MONITORED_DIR" | while read FILE EVENT TIMESTAMP
do
sqlite3 "$DB_FILE" "INSERT INTO Events (File, EventType,TimeOcurred) VALUES ('$FILE', '$EVENT', '$TIMESTAMP')"
echo $FILE $EVENT $TIMESTAMP
done
