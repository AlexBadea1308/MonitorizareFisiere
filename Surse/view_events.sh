#!/bin/bash

source ./config.sh $1 $2

echo "Evenimentele din baza de date $2 sunt:"
sqlite3 "$DB_FILE" "SELECT * FROM Events;"
echo 
