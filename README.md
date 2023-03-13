# Configurare-Vs-Code-per-utenti-ipovedenti-programmatori-python-
Questa guida offre una guida alla configurazione dell'editor 'Visual Studio Code' per utenti con difficoltà visive che desiderano programmare nel linguaggio python, in modo che la piattaforma risulti più accessibile alle loro esigenze

Le azioni da eseguire per configurare l'editor al meglio sono spiegate nei seguenti step:

# STEP 1: INSTALLARE UNO SCREEN READER

Per iniziare avremo bisogno di uno screen-reader che legga il contenuto delle pagine che visualizzeremo tramite una voce sintetizzata. Ve ne sono diversi a seconda del sistema operativo che si possiede, ecco alcuni dei principali esempi:

  - MAC-OS -> VOICE-OVER : già presente nei dispositivi apple, non necessita download ed installazione, attivabile mediante Siri o barra dei comandi  
                           (COMMAND+SPAZIO). Link alla documentazione: https://support.apple.com/it-it/guide/voiceover/voic010/mac
                           
  - Windows -> NVDA: Da scaricare ed installare, link al download: https://www.nvaccess.org/download/ , link alla documentazione: https://www.nvda.it
  
  - Linux -> ORCA: già presente nei sistemi operativi Linux, link alla documentazione: https://help.gnome.org/users/orca/stable/index.html.en


# STEP 2: INSTALLARE VISUAL STUDIO CODE

Secondo passaggio sarà procurarsi l'editor apposito per la configurazione, se non lo si ha ancora fatto si può scaricare Visual studio code mediante il seguente link: https://code.visualstudio.com/download. Una volta scaricato, sarà necessario installarlo e aprirlo per proseguire col prossimo step

# STEP 3: INSTALLARE PYTHON IN VISUAL STUDIO CODE

Se python non è ancora presente nel vostro pc e/o nel vostro editor, potete seguire i seguenti passaggi:

  - Aprire Visual studio Code
  - Sulla spalla sinistra dell'editor selezionare la sezione 'estensioni'
  - Nel campo di ricerca che appare digitare 'python'
  <img width="550" alt="Schermata 2023-03-09 alle 10 57 42" src="https://user-images.githubusercontent.com/63148243/223986978-ac0da31f-b163-403a-a2d6-0473c554d9f4.png">
  
  - Se non ancora installato sarà visibile il bottone 'install', si dovrà cliccare su di esso
  - Attendere l'installazione, poi chiudere e riaprire l'editor
 
Se è necessario anche l'interprete per python, è possibile scaricarlo in base al vostro sistema operativo mediante il seguente link: https://www.python.org/downloads/

# STEP 4: ATTIVARE L'OPZIONE 'SCREEN READER OPTIMIZED' SU VISUAL STUDIO CODE

Una volta attivato lo screen reader e aperto l'editor Visual Studio Code, seguiamo i seguenti passi per attivare la modalità 'screen reader optimized'
  
  - Aperto l'editor, sulla spalla sinistra selezionare la sezione in basso 'impostazioni' ('manage')
  - Dalle voci del menù a tendina selezionare 'settings'
  - Nella barra di ricerca che comparirà digitare 'screen reader'
  - Apparirà una voce 'Editor: Accessibility Support'
  - Impostare su 'on' se si vuole che l'editor sia sempre ottimizzato per gli screen reader, oppure su 'auto' se si vuole che sia ottimizzato solo    
    quando ne rileva uno attivo.
<img width="550" alt="Schermata 2023-03-09 alle 11 11 01" src="https://user-images.githubusercontent.com/63148243/223990138-b505b015-d21c-46cd-80ad-0e1b6ea0d59a.png">

Questa opzione permetterà un'agevolazione nel movimento all'interno dell'editor tra le varie sezioni, inoltre aggiungerà delle proprietà come quella di leggere le righe del codice per intero.

# STEP 5: SALVARE NELLA CARTELLA DI LAVORO IL FILE 'parser.py'

Ora sulla vostra area di lavoro, creare un nuovo file python, in cui all'interno dovrete copiare il contenuto del file files/parser.py.
Questo codice permette di avere un parsing avanzato di codice python, in modo tale che l'utente possa poter comprendere meglio il funzionamento del codice che ha scritto, potendo ascoltare una lettura più dettagliata sul costrutto di cui vuole sapere qualcosa in più rispetto alla lettura del codice per come è scritto proposta dal suo screen reader.

NOTE: Per il funzionamento di parser.py saranno necessarie le librerie:
  - 'ast': "pip install ast" -> creazione dell'albero di parsing
  - 'pysstx3': "pip install pysstx3" -> sintetizzatore vocale
  - 'tokenize': "pip install tokenize" -> poter effettuare il parsing anche dei commenti all'interno del codice
  - 'io','os','sys'

# STEP 6: CREARE UN TASK IN VISUAL STUDIO CODE MODIFICANDO IL FILE 'task.json'

I seguenti step ci aiuteranno a far in modo che il parsing avanzato di un nostro programma scritto in python possa avvenire nella maniera più semplice  possibile. Per far ciò legeremo questa nostra azione ad un Task di Visual studio code, attraveros il seguente procedimento:

 - Sulla schermata dove stiamo visualizzando il nostro file scritto in python digitare CTRL+SHIFT+P (su MAC-OS: COMMAND+SHIFT+P)
 - Verrà aperta la 'barra dei comandi'
 - Digitare nella barra 'Configure Tasks'
 - Selezionare la voce 'Tasks: Configure Tasks'
 - Cliccare 'Create task.json file from template'

<img width="813" alt="Schermata 2023-03-13 alle 09 33 42" src="https://user-images.githubusercontent.com/63148243/224648133-274d5cd9-a4e0-4781-a252-3467b22e6dfe.png">

Di fronte a noi apparirà il file 'task.json' dell'editor Visual studio code, se si vuole si può eliminare il contenuto presente nel file per evitare confusione, poi copiare all'interno di esso il contenuto del file che trovate all'interno di files/task.json.

Ora abbiamo creato un Task che richiama il nostro file 'parser.py' con argomento il file di cui vogliamo eseguire un parsing avanzato di una determinata riga di codice

# STEP 7: CREARE UN COMANDO RAPIDO PER ESEGUIRE IL PARSER AVANZATO

Ora vogliamo assegnare ad una combinazione di tasti il nostro processu su Visual Studio Code, per farlo:
 - Sulla schermata dove stiamo visualizzando il nostro file scritto in python digitare CTRL+SHIFT+P (su MAC-OS: COMMAND+SHIFT+P)
 - Verrà aperta la 'barra dei comandi'
 - Digitare nella barra 'Open Keyboard Shortcuts'
 - Selezionare la voce: 'Preferences: Open Keyboard ShortCuts(JSON)'

<img width="624" alt="Schermata 2023-03-09 alle 11 58 46" src="https://user-images.githubusercontent.com/63148243/224004192-7853a33c-abf1-43e6-9680-61947f7b5d2f.png">


Di fronte a noi apparirà il file 'keybindings.json' dell'editor Visual studio code, copiare all'interno di esso il contenuto del file che trovate all'interno di files/keybindings.json

É possibile impostare combinazioni di tasti differenti, unico suggerimento è quello di non impostare combinazion i di tasti corrispondenti ad altre shortcuts

# CONCLUSIONI

Ora è possibile creare del codice python, evidenziare col cursore una porzione del codice, cliccare la combinazione di tasti CTRL+SHIFT+X per poter ascoltare una lettura avanzata del pezzo di codice python.

Limiti del programma:

 - Attualmente il programma non è in grado di gestire il parsing di tutti i costrutti di python, ma è possibile implementarli nel codice una volta  
   capita la logica del suo funzionamento. Sono comunque presenti i principali costrutti utilizzati.
   
 - È necessario passare un costrutto nella sua interezza affinchè il parsing avanzato venga effettuato con successo, in caso contrario il parser 
   risponderà con un errore


