#!/bin/bash

source ./config.sh $1 $2

echo "Comentariile din baza de date $2 sunt:"

sqlite3 "$DB_FILE" "SELECT * FROM Comments;"

echo
