#!/bin/bash

PS3="Alege o opțiune din meniu: "

select OPTION in "Vizualizare Evenimente" "Vizualizare Comentarii" "Adaugare comentariu" "Stergere eveniment" "Stergere Comentariu" "Iesire"
do
case $REPLY in

    1)./view_events.sh $1 $2 ;;
    2)./view_comments.sh $1 $2;;
    3)./add_comment.sh $1 $2;;
    4)./delete_events.sh $1 $2;;
    5)./delete_comments.sh $1 $2;;
    6)exit 0 ;;
    *) echo "Optiune incorecta" ;;
    esac
    done
