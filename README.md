# MonitorizareFisiere
# Monitorizare fisiere dintr-un director folosind inotify-tools

# 18.06.2024 

# Am reusit sa analizez toate temele propuse si am ales sa lucrez la urmatorul proiect:  Scripting 02-Monitorizare fisiere dintr-un director folosind inotify-tools
# De asemenea am studiat man page ul lui inotify-tools (parametrii si intrebuinta)

# 19.06.2024

# Am realizat schema componentelor proiectului astfel incat acesta sa indeplineasca mai multe cerinte decat ce poate face inotify-tools.

# Proiectul va avea un main script care va contine mai multe optiuni:
# -monitorizarea unui director;
# -monitorizarea unui director si a subdirectoarelor acestuia;
# -stocarea informatiilor intr un director de loguri;
# -posibilitatea de a trimite email uri de informare atunci cand un eveniment se realizeaza asupra unui director dat ca parametru scriptului
# -posibilitatea crearii unei baze de date si stocarea informatiilor despre evenimente in ea
# -generarea unui raport local al tuturor evenimentelor efectuate asupra unui director
# -creearea unei interfete grafice (daca mai am timp)

# 20.06.2024

# Am inceput sa creez structura proiectului: am realizat un main script care contine un meniu cu toate optiunile prezentate mai sus, un script de config unde am mai multe variabile de care ma voi folosi in alte scripturi create in viitor si primele doua functionalitati ale proiectului si anume monitorizarea unui director (doar el) si a directorului impreuna cu subdirectoarele sale. 

# 21.06.2024

# Am reusit sa implementez functia de send_mail.sh prin efectuarea mai multor pasi:
# -am instalat tool ul de ssmtp
# - am configurat fisierul /etc/ssmtp/ssmtp.conf pentru a putea transmite emailuri de pe o adresa stabila (un cont creat special pentru proiect )
# -root=postmaster
# -mailhub=smtp.gmail.com:587
# -AuthUser=ssmtptest13@gmail.com
# -AuthPass=adbgljmabvofuqan
# -UseSTARTTLS=YES
# -FromLineOverride=YES
# -am acordat permisiuni de executie pentru acest fisier

# -de asemenea am implementat functia de generate_raport care afiseaza evenimentele care au avut loc asupra unui director intr un format mai ordonat

# 22.06.2024-24.06.2024

# In aceste trei zile am studiat mai multe proprietati ale lui sqlite3 pe care l am folosit in scopul stocarii evenimentelor executate asupra unui director atunci cand rulam comanda inotify-tools

# am realizat crearea bazei de date in scriptul create_database precum si a tabelelor necesare;
# am realizat scriptul care adauga in baza de date toate modificarile care au loc asupra directorului mentionat;
# am realizat script pentru a opera cu meniu al bazei de date in care practic vom executa querry-uri basic (add,delete,view)
# am adaugat un fisier in care am atribuit link uri care m au ajutat sa invat aceste noi tool-uri;

# 25.06.2024

# Am inceput sa lucrez la interfata grafica a proiectului. Am folosit python3 ca si interpretor al limbajului Python si PyQt5 pentru a realiza mult mai usor interfata grafica (PyQt5 este un set de legaturi Python pentru Qt)

# sudo apt install python3-pip
# pip install PyQt5
# sudo apt install python3

# Interfata grafica va contine in totalitate aceleasi optiuni pe care scriptul le are atunci cand il rulam in terminal, doar ca optiunile vor fi constituite de niste butoane, fiecare fiind conectate la o fereastra in care vom putea vedem modificarile care au loc asupra unui director selectat.