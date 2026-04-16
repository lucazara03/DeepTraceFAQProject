Procedura

Il progetto è disponibile anche online pubblicamente, digitando http://51.20.118.13/

Prerequisiti
Prima di iniziare, assicurati di avere installato:
1. Python 3.10
2. pip
3. Connessione internet

Installazione (basata sul sistema Windows)
1. Andare su https://github.com/lucazara03/DeepTraceFAQProject/tree/main
2. Cliccare il tasto verde <> Code 
3. Premere "Download ZIP" ed estrarre la cartella .zip o eseguire 'git clone https://github.com/lucazara03/DeepTraceFAQProject.git'
4. Aprire la cartella estratta o clonata
5. Cliccare sulla barra degli indirizzi in alto, scrivere cmd e premere Invio. Si aprirà il prompt dei comandi già posizionato nel posto giusto
6. Scrivere: python -m venv venv
7. Scrivere: venv\Scripts\activate
8. Vedrai (venv) affianco al path
9. Scrivere: pip install -r requirements.txt
10. Attendere l'installazione
11. Scrivere: python manage.py runserver
12. Sul proprio browser, digitare: http://127.0.0.1:8000/

Nota sul Database: Il progetto è pre-configurato per connettersi a un database AWS RDS. Assicurarsi di avere una connessione internet attiva. In caso di errore OperationalError (Timeout), verificare che l'accesso al database non sia bloccato da firewall aziendali sulla porta 5432.

Istruzioni:
1. Per testare l'applicazione, digitare un'e-mail dove si vuole ricevere il report PDF. 
2. Scegliere fonte di informazioni (Caregiver, paziente o altro)
3. Compilare il form
4. Premere il tasto Invio
5. Si verrà reindirizzati sulla pagina di successo. Controllare e-mail per vedere il report
Per visualizzare lo storico dei form compilati, premere link 'Clicca qui per visualizzare i test effettuati' presente nella pagina iniziale



