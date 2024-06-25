#!/bin/bash

exists=` file $2 | egrep -w "database" `
if [[ -z "$exists" && -f "$2" ]]
then
echo "Baza de date exista deja. Nu este necesara recrearea tabelelor."
exit 1
fi

fullpath=`realpath $2`
echo $fullpath
source ./config.sh $1 $fullpath

sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS Events (
EventID INTEGER PRIMARY KEY AUTOINCREMENT,
File TEXT,
EventType TEXT,
TimeOcurred TEXT
);

CREATE TABLE IF NOT EXISTS Comments (
CommentID INTEGER PRIMARY KEY AUTOINCREMENT,
Nume TEXT,
Prenume TEXT,
Comentariu TEXT,
TimeOcurred TEXT,
EventID INTEGER,
FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

EOF

echo "Baza de date a fost creata cu succes!"
