# Creare un nuovo trigger per un nuovo costrutto

Attualmente, i costrutti che il file [parser.py](./files/parser.py) offre, sono quelli dichiarati in [implementations.md](./implementations.md).

Per creare un nuovo trigger relativo ad un costrutto non ancora gestito in [parser.py](./files/parser.py) i passaggi sono piuttosto standard e possono essere riassunti nei seguenti step:

# Individuare quali metodo della liberia 'ast' di Python compongono il costrutto
La libreria 'ast' utilizzata in [parser.py](./files/parser.py) offre una vasta gamma di metodi per la gestione dei costrutti del linguaggio Python, in modo che molto lavoro venga eseguito direttamente dalla libreria senza dover aggiungere ulteriori modifiche. 

Facciamo un esempio pratico: si vuole implementare il trigger sull'istruzione 'continue' in Python

In questo step dobbiamo semplicemente individuare se nella libreria 'ast' esiste già un metodo che permette di individuare quando in un programma viene utilizzata l'istruzione 'continue' --> nel nostro caso il metodo esiste e viene richiamato come "ast.Continue".

# Definire una funzione per gestire il trigger del costrutto

Ora è necessario che all'interno del file [parser.py](./files/parser.py) venga inserita una nuova funzione, la quale si occuperà di gestire il trigger e le azioni da compiere una volta individuato il costrutto di interesse nel nostro programma.

Sempre tornando al nostro programma esempio: si può notare che tutte le funzioni trigger hanno come nome prefisso "visit_", seguito dal nome del costrutto, quindi in questo caso, il nome della funzione che andremo a definire sarà "visit_continue".

 ```python
 
 def visit_continue(self, code):
  globale parsing_trace
  if isinstance(node.value, ast.Continue): 
    parsing_trace += "istruzione continue. \n"
    
 
 ```
