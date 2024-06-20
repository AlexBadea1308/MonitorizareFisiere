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