#!/bin/bash

source ./config.sh $1 $2

echo "Introduceti numele:"
read nume
echo "Introduceti prenumele:"
read prenume
echo "Introduceti comentariul:"
read comentariu
echo "Introduceti data:"
read data
echo "Introduceti ID-ul evenimentului asociat!"
read evnimentid
sqlite3 "$DB_FILE" "INSERT INTO Comments (Nume,Prenume,Comentariu,TimeOcurred,EventID) VALUES ('$nume', '$prenume', '$comentariu','$data','$evenimentid');"
