#!/bin/bash

if [[ ! -d $1 ]]
then
echo "Parametrul dat nu este un director!"
exit 2
fi

MONITORED_DIR=$1

LOG_FILE="/var/log/file_monitor.log"

DB_FILE=$2

REPORT_INTERVAL=60

EMAIL="alexxlea13@gmail.com"

EMAIL_SUBJECT="Atentie monitorizare detectata!"

EMAIL_BODY="Atentie un eveniment a fost detectat.Verificati fisierul de log pentru mai multe detalii!"

EVENTS="create,delete,modify,move,attrib,close_write,close_nowrite,access,open,move_self"

SEND_EMAIL_NOTIFICATIONS=true
