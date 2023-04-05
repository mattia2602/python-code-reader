# Creare un nuovo trigger per un nuovo costrutto

Attualmente, i costrutti che il file [parser.py](./files/parser.py) offre, sono quelli dichiarati in [implementations.md](./implementations.md).

Per creare un nuovo trigger relativo ad un costrutto non ancora gestito in [parser.py](./files/parser.py) i passaggi sono piuttosto standard e possono essere riassunti nei seguenti step:

# Individuare quali metodo della liberia 'ast' di Python compongono il costrutto
La libreria 'ast' utilizzata in [parser.py](./files/parser.py) offre una vasta gamma di metodi per la gestione dei costrutti del linguaggio Python, in modo che molto lavoro venga eseguito direttamente dalla libreria senza dover aggiungere ulteriori modifiche. 

Facciamo un esempio pratico: si vuole implementare il trigger sull'istruzione 'continue' in Python

In questo step dobbiamo semplicemente individuare se nella libreria 'ast' esiste già un metodo che permette di individuare quando in un programma viene utilizzata l'istruzione 'continue' --> nel nostro caso il metodo esiste e viene richiamato come "ast.Continue".

# Definire una funzione per gestire il trigger del costrutto

Ora è necessario che all'interno del file [parser.py](./files/parser.py) venga inserita una nuova funzione, la quale si occuperà di gestire il trigger e le azioni da compiere una volta individuato il costrutto di interesse nel nostro programma.

Sempre tornando al nostro programma esempio: si può notare che tutte le funzioni trigger hanno come nome prefisso "visit_", seguito dal nome del costrutto, quindi in questo caso, il nome della funzione che andremo a definire sarà "visit_Continue".

 ```python
 
 def visit_Continue(self, code):
  globale parsing_trace
  if isinstance(node.value, ast.Continue): 
    parsing_trace += "istruzione continue. \n"
    
 ```
 
Dopo aver richiamato la variabile globale che si occupa di contenere tutto il "lungo commento" che verrà poi letto dallo screen reader, andiamo ad utilizzare "isinstance" della libreria 'ast' per chiederci se il nodo attuale del nostro codice è riconducibile al costrutto "continue" del linguaggio Pyhton, in caso affermativo, inseriamo nella variabile globale ciò che vogliamo venga letto dallo screen reader quando incontra questa istruzione.

# Inserire la nuova funzione nel visit delle espressioni

Per avere maggior certezza che la nostra istruzione venga "tradotta" correttamente, è necessario inserire una chiamata alla nostra funzione all'interno di "visit_Expr", poichè può accadere che la nostra istruzione sia una componente di un espressione dentro il nostro codice, quindi è necessario prima di dividere l'espressioni in blocchi più elementari, in modo che ognuno di essi possa venire conosciuto dal proprio trigger.

È necessario allora cercare in [parser.py](./files/parser.py) la riga di codice relativa all'inizio della funzione "visit_Expr" è chiamare la nostra funzione, in questo caso sempre "visit_Continue"

```python 
def visit_Expr(self, node):
   # Codice presente nel file...
   elif isistance(node,ast.Continue):
       visitor.visit_Continue(node)
   # altro codice...
```

Quindi, se l'espressione è composta anche da un costrutto "continue", esso viene riconosciuto e fatto gestire dalla sua funzione specifica.

Ora il nostro programma [parser.py](./files/parser.py) è in grado di fare il parsing avanzato di un'istruzione "continue" :)
