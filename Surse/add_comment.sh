#!/bin/bash

source ./config.sh $1 $2

echo "Introduceti numele:"
read -p nume
echo "Introduceti prenumele:"
read -p prenume
echo "Introduceti comentariul:"
read -p comentariu
echo "Introduceti data:"
read -p data
echo "Introduceti ID-ul evenimentului asociat!"
read -p evnimentid
sqlite3 "$DB_FILE" "INSERT INTO Comments (Nume,Prenume,Comentariu,TimeOcurred,EventID) VALUES ('$nume', '$prenume', '$comentariu','$data','$evenimentid');"
