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
 
Se è necessario anche l'interprete per python, in base al vostro sistema operativo installarlo mediante il seguente link: https://www.python.org/downloads/

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

