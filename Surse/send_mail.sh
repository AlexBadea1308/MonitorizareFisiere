#!/bin/bash

source ./config.sh $1

function send_email
{
echo "$1" | mail -s "$2" "$3"
}

function log_and_notify
{
echo "$FILE" "$EVENT" "$TIMESTAMP" | sudo tee --append "$LOG_FILE" >/dev/null

if [ "$SEND_EMAIL_NOTIFICATIONS" = true ]
then
send_email "Eveniment: $2 - Fișier: $1 - Timp: $3" "$EMAIL_SUBJECT" "$EMAIL"
fi
}

inotifywait -t $REPORT_INTERVAL -m -r -e $EVENTS --format '%w%f %e %T' --timefmt '%Y-%m-%d %H:%M:%S' "$MONITORED_DIR" |
while read FILE EVENT TIMESTAMP;
do
log_and_notify "$FILE" "$EVENT" "$TIMESTAMP"
echo "$FILE" "$EVENT" "$TIMESTAMP"
done
