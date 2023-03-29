# Python-code-reader
Questo progetto è stato creato con lo scopo di fornire codice ed istruzioni utili alla configurazione dell'editor 'Visual Studio Code' per coloro che hanno difficoltà visive e desiderano programmare in Python. Lo scopo è di rendere lo sviluppo del codice più accessibile alle loro esigenze. I sorgenti di codice che verranno citati in alcuni step sono disponibili nel folder 'files'.

# STEP 1: INSTALLARE UNO SCREEN READER

Per iniziare è necessario avere a disposizione uno screen-reader che legga il contenuto delle pagine visualizzate a schermo tramite una voce sintetizzata. Ne esistono diversi a seconda del sistema operativo che si possiede, ecco alcuni principali esempi:

  - MAC-OS -> VOICE-OVER : già presente nei dispositivi apple, non necessita download ed installazione, attivabile mediante Siri o barra dei comandi  
                           (COMMAND+SPAZIO). Link alla documentazione: https://support.apple.com/it-it/guide/voiceover/voic010/mac
                           
  - Windows -> NVDA: Da scaricare ed installare, link al download: https://www.nvaccess.org/download/ , link alla documentazione: https://www.nvda.it
  
  - Linux -> ORCA: già presente nei sistemi operativi Linux, link alla documentazione: https://help.gnome.org/users/orca/stable/index.html.en


# STEP 2: INSTALLARE VISUAL STUDIO CODE

Se non si è già in possesso dell'editor 'Visual Studio Code', lo si può scaricare in questo step mediante il seguente link: https://code.visualstudio.com/download. Una volta scaricato, sarà necessario installarlo e aprirlo per proseguire. 
È caldamente consigliato utilizzare l'editor menzionato precedentemente poichè i prossimi step faranno riferimento ad esso. 


# STEP 3: INSTALLARE PYTHON IN VISUAL STUDIO CODE

Python è il linguaggio col quale sarà possibile sviluppare codice in maniera più accessibile mediante questa guida.

Ecco qui una guida all'installazione tramite l'editor 'Visual Studio Code'.

  - Aprire Visual studio Code
  - Sulla spalla sinistra dell'editor selezionare la sezione 'estensioni'
  - Nel campo di ricerca che appare digitare 'python'
  
  <img width="550" alt="Schermata 2023-03-09 alle 10 57 42" src="https://user-images.githubusercontent.com/63148243/223986978-ac0da31f-b163-403a-a2d6-0473c554d9f4.png">
  
  - Se non lo si ha ancora installato, sarà visibile il bottone 'install', si dovrà cliccare su di     
    esso per avviare l'installazione
  - Attendere l'installazione, poi chiudere e riaprire l'editor
 
Poi si dovrà scaricare ed installare l'interprete del linguaggio Python, in base al vostro sistema operativo potete trovare la versione più adatta mediante il seguente link: https://www.python.org/downloads/

# STEP 4: ATTIVARE L'OPZIONE 'SCREEN READER OPTIMIZED' SU VISUAL STUDIO CODE

Una volta attivato lo screen reader e aperto 'Visual Studio Code', il prossimo step sarà raggiungere una migliore interazione con l'editor grazie all' attivazione della modalità 'screen reader optimized'.
  
  - Aperto l'editor, sulla spalla sinistra selezionare la sezione in basso 'impostazioni' 
    ('manage')
  - Dalle voci del menù a tendina selezionare 'settings'
  - Nella barra di ricerca che comparirà digitare 'screen reader'
  - Apparirà una voce 'Editor: Accessibility Support'
  - Impostare su 'on' se si vuole che l'editor sia sempre ottimizzato per gli screen reader, oppure 
    su 'auto' se si vuole che sia ottimizzato solo quando ne rileva uno attivo.
    
<img width="550" alt="Schermata 2023-03-09 alle 11 11 01" src="https://user-images.githubusercontent.com/63148243/223990138-b505b015-d21c-46cd-80ad-0e1b6ea0d59a.png">

Quest'opzione permetterà un'agevolazione nel movimento all'interno dell'editor e tra le varie sezioni, inoltre aggiungerà delle proprietà come quella di leggere righe di codice per intero a differenza dei normali screen reader, che tendono a leggere un testo parola per parola.

# STEP 5: SALVARE NELLA CARTELLA DI LAVORO IL FILE 'parser.py'

Ora sull'area di lavoro dell'editor, creare un nuovo file python, copiare il contenuto del file 'parser.py'.
Questo codice sviluppato da me permette di avere un parsing avanzato di codice python, in modo tale che l'utente possa poter comprendere meglio il funzionamento del codice che ha scritto, potendo ascoltare una lettura più dettagliata sul costrutto di cui vuole sapere qualcosa in più rispetto alla lettura del codice per come è scritto proposta dal suo screen reader.
Il funzionamento, senza entrare nei dettagli, è quello di aver costruito dei 'trigger' che si attivano ogni volta che rileva un costrutto principale del linguaggio Python (cicli, condizioni, variabili,...) e ,per ognuno di essi, compie una determinata azione programmata. 
Principalmente tutti i trigger hanno come azione programmata quella di inserire in una stringa globale una frase come "Ho letto la variabile 'a'", oppure "Ho appena letto un ciclo for", in modo che poi questa lunga stringa possa venire letta mediante un dispositivo come uno screen reader o un sintetizzatore vocale.

NOTE: Per il funzionamento di parser.py saranno necessarie le librerie:
  - 'ast': pre-installata dalla versione 2.5 di python -> creazione dell'albero di parsing
  - 'pyttsx3': "pip install pyttsx3" -> sintetizzatore vocale
  - 'tokenize': pre-installata dalla versione 2.2 di python -> poter effettuare il parsing anche 
     dei commenti all'interno del codice
  - 'io','os','sys' -> librerie pre-installate di python

# STEP 6: CREARE UN TASK IN VISUAL STUDIO CODE MODIFICANDO IL FILE 'task.json'

Creiamo un 'Task', ovvero una serie di eventi che vengono raccolti in un'unica azione che possiamo invocare quando vogliamo. Per fare ciò, è necessario seguire i seguenti passaggi su 'Visual Studio Code'.

 - Sulla schermata in cui è visualizzato il file scritto in Python digitare: CTRL+SHIFT+P (su MAC-OS: COMMAND+SHIFT+P)
 - Verrà aperta la 'barra dei comandi'
 - Digitare nella barra 'Configure Tasks'
 - Selezionare la voce 'Tasks: Configure Tasks'
 - Cliccare 'Create task.json file from template'

<img width="813" alt="Schermata 2023-03-13 alle 09 33 42" src="https://user-images.githubusercontent.com/63148243/224648133-274d5cd9-a4e0-4781-a252-3467b22e6dfe.png">

Si aprirà il file 'task.json'. Se lo si desidera, si può eliminare il contenuto presente nel file, non sarà utile al fine del progetto. Copiare all'interno di 'task.json' il codice del file presente in files/task.json.

Ora è stato creato nell'editor un Task che esegue 'parser.py' e prende come argomento il nome del file di cui vogliamo eseguire un parsing avanzato di una determinata riga di codice.

# STEP 7: CREARE UN COMANDO RAPIDO PER ESEGUIRE IL PARSER AVANZATO

Creiamo una combinazione di tasti rapidi che invocherà il Task creato nello step precedente.
Sempre all'interno di 'Visual Studio Code' dobbiamo preocedere nel seguente modo:
 - Sulla schermata in cui è presente il file scritto in python digitare CTRL+SHIFT+P (su MAC-OS: COMMAND+SHIFT+P)
 - Verrà aperta la 'barra dei comandi'
 - Digitare nella barra 'Open Keyboard Shortcuts'
 - Selezionare la voce: 'Preferences: Open Keyboard ShortCuts(JSON)'

<img width="624" alt="Schermata 2023-03-09 alle 11 58 46" src="https://user-images.githubusercontent.com/63148243/224004192-7853a33c-abf1-43e6-9680-61947f7b5d2f.png">


Si aprirà il file 'keybindings.json' che permette di associare ad una serie di tasti un evento, copiare all'interno di esso il contenuto del file all'interno di files/keybindings.json

É possibile impostare combinazioni di tasti differenti, l'unico suggerimento è quello di non impostare combinazioni di tasti corrispondenti ad altre keyboard-shortcuts.

# CONCLUSIONI

Ora è possibile creare del codice python, evidenziare col cursore una porzione del codice, cliccare la combinazione di tasti CTRL+SHIFT+X per poter ascoltare una lettura avanzata del pezzo di codice python.

Limiti del programma:

 - Attualmente il programma non è in grado di gestire il parsing di tutti i costrutti di python, ma è possibile implementarli nel codice una volta capita la logica del suo funzionamento. Sono dunque presenti i principali costrutti utilizzati nella programmazione di codice Python.
   
 - È necessario evidenziare col cursore un costrutto nella sua interezza affinchè il parsing avanzato venga effettuato con successo, in caso contrario il parser risponderà con un errore generico.
