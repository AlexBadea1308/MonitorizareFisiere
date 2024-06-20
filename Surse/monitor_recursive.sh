#!/bin/bash

if [[ $# -ne 1 || ! -d $1 ]]
then
echo "Parametrul nu este un director!"
exit 1
fi

source ./config.sh $1

echo "Director monitorizat: $MONITORED_DIR"

sudo inotifywait -t $REPORT_INTERVAL -m -r -e $EVENTS --format '%w%f %e %T' --timefmt '%Y-%m-%d %H:%M:%S' "$MONITORED_DIR" | while read FILE EVENT TIMESTAMP
do
echo "$FILE" "$EVENT" "$TIMESTAMP" | sudo tee --append "$LOG_FILE" >/dev/null
echo "$FILE" "$EVENT" "$TIMESTAMP"
done
