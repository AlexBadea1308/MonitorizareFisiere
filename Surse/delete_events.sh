#!/bin/bash

source ./config.sh $1 $2

echo "Introduceti id-ul evenimentului pe care doriti sa il stergeti:"
read evenimentid
sqlite3 "$DB_FILE" "DELETE FROM Events WHERE EventId = $evenimentid;"

echo "Evenimentul a fost sters cu succes!"
