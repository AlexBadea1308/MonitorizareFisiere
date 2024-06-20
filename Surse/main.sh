#!/bin/bash

if [[ ! -d $1 ]]
then
echo "NU ai introdus un director existent pentru main.sh"
exit 1
fi

PS3="Alege o opțiune din meniu: "

select OPTION in "Monitorizare un director" "Monitorizare un director si subdirectoarele sale" "Monitorizare + notificare email" "Creare baza de date!" "Monitorizare + stocare in baza de date" "Database Tools" "Generare raport" "Iesire"
do
case $REPLY in

    1)./monitor.sh $1 ;;
    2)./monitor_recursive.sh $1 ;;
    3)./send_mail.sh $1 ;;
    4)./create_database.sh $1 $2 ;;
    5)./load_in_database.sh $1 $2 ;;
    6)./database_meniu.sh $1 $2 ;;
    7)./generate_raport.sh $1 ;;
    8) exit 0 ;;
    *) echo "Optiune incorecta" ;;
    esac
    done
