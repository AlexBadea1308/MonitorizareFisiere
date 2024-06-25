#!/bin/bash

source ./config.sh $1 $2

echo "Introduceti id-ul comentariului pe care doriti sa il stergeti:"
read -p commid
sqlite3 "$DB_FILE" "DELETE FROM Comments WHERE CommentID=$commid;"

echo "Comentariul a fost sters cu succes!"
