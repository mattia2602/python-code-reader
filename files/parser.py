# Librerie necessarie
import ast
import io
import os.path
import tokenize
from sys import argv
import pyttsx3
import sys

# inizializzazione del sintetizzatore
engine = pyttsx3.init()
# in questa stringa memorizzo il contenuto del parsing del codice Python in ingresso
parsing_trace = ""


# i commenti non vengono rilevati dall'albero di parsing
# con questo metodo vengono estratti dal codice
def extract_comment(source_code):
    comments = []
    for token in tokenize.tokenize(io.BytesIO(source_code.encode("utf-8")).readline):
        if token.type == tokenize.COMMENT:
            comm = token.string.strip()
            if comm.startswith("#"):
                comments.append(comm)
    return comments


# classe che definisce tutte le funzioni eseguire il parsing del mio codice
class NodeVisitor(ast.NodeVisitor):

    # trigger di un nome di una variabile
    def visit_Name(self, node):
        global parsing_trace
        parsing_trace += f"{node.id}, variabile, . "
        self.generic_visit(node)

    # trigger di un valore costante (numero, carattere, stringa)
    def visit_Constant(self, node):
        global parsing_trace
        parsing_trace += f"{node.value}, costante, . "

    # trigger di nomi costanti del linguaggio
    def visit_NameConstant(self, node):
        global parsing_trace
        # gestione dei valori booleani
        if node.value in [True, False]:
            parsing_trace += f"Valore logico {node.value}, "

    # trigger su una espressione
    def visit_Expr(self, node):
        # se l'espressione è una costante
        if isinstance(node, ast.Constant):
            visitor.visit_Constant(node)
        # se l'espressione è un assegnamento
        elif isinstance(node, ast.Assign):
            visitor.visit_Assign(node)
        # se l'espressione è una comparazione
        elif isinstance(node, ast.Compare):
            visitor.visit_Compare(node)
        # se l'espressione è una definizione di funzione
        elif isinstance(node, ast.FunctionDef):
            visitor.visit_FunctionDef(node)
        # se l'espressione è una chiamata di funzione
        elif isinstance(node, ast.Call):
            visitor.visit_Call(node)
        # se l'espressione è un operatore di assegnamento
        elif isinstance(node, ast.AugAssign):
            visitor.visit_AugAssign(node)
        # se l'espressione è una variabile
        elif isinstance(node, ast.Name):
            visitor.visit_Name(node)
        # se l'espressione è un costrutto if
        elif isinstance(node, ast.If):
            visitor.visit_If(node)
        # se l'espressione è un ciclo For
        elif isinstance(node, ast.For):
            visitor.visit_For(node)
        # se l'espressione è un ciclo While
        elif isinstance(node, ast.While):
            visitor.visit_While(node)
        # se l'espressione è un array
        elif isinstance(node, ast.List):
            visitor.visit_List(node)
        # se l'espressione è un elemento di un array
        elif isinstance(node, ast.Subscript):
            visitor.visit_Subscript(node)
        # se l'espressione è un costrutto Try-except
        elif isinstance(node, ast.Try):
            visitor.visit_Try(node)
        # se l'espressione è un import di una libreria
        elif isinstance(node, ast.Import):
            visitor.visit_Import(node)
        # se l'espressione è un istruzione yield
        elif isinstance(node, ast.Yield):
            visitor.visit_Yield(node)
        # se l'espressione è un operazione bin
        elif isinstance(node, ast.BinOp):
            visitor.visit_BinOp(node)
        # se l'espressione è un operazione bool
        elif isinstance(node, ast.BoolOp):
            visitor.visit_BoolOp(node)
        # se l'espressione è l'istanza di una classe
        elif isinstance(node, ast.ClassDef):
            visitor.visit_ClassDef(node)
        # se l'espressione è la definizione di un dizionario
        elif isinstance(node, ast.Dict):
            visitor.visit_Dict(node)
        # se l'espressione è un istruzione pass
        elif isinstance(node, ast.Pass):
            visitor.visit_Pass(node)
        # se l'espressione è un metodo di una classe
        elif isinstance(node, ast.Attribute):
            visitor.visit_Attribute(node)
        # se l'espressione è una espressione: valuto la sotto espressione
        elif isinstance(node, ast.Expr):
            visitor.visit_Expr(node.value)
        # quando la condizione è semplicemente o True o False
        elif node.value is True or node.value is False:
            visitor.visit_NameConstant(node)
        # gestione di sotto-espressione
        else:
            # sotto espressione è una chiamata di funzione
            if isinstance(node.value, ast.Call):
                visitor.visit_Call(node.value)
            # sotto espressione è una istruzione yield
            if isinstance(node.value, ast.Yield):
                visitor.visit_Yield(node.value)
            # casi non ancora gestiti
            else:
                self.generic_visit(node.value)

    # trigger operatori di comparazione
    def visit_Compare(self, node):
        global parsing_trace
        # se il valore a sinistra dell'operatore è una costante
        if isinstance(node.left, ast.Constant):
            visitor.visit_Constant(node.left)
        # se il valore a sinistra dell'operatore è una variabile
        elif isinstance(node.left, ast.Name):
            visitor.visit_Name(node.left)
        # se il valore a sinistra è un insieme di operazioni
        elif isinstance(node.left, ast.BinOp):
            visitor.visit_BinOp(node.left)
        # se il valore a sinistra è una chiamata di funzione
        elif isinstance(node.left, ast.Call):
            visitor.visit_Call(node.left)

        for op in node.ops:
            # operatore di uguaglianza  ==
            if isinstance(op, ast.Eq):
                parsing_trace += f"uguale a "
            # operatore maggiore >
            if isinstance(op, ast.Gt):
                parsing_trace += f"maggiore di "
            # operatore maggiore uguale >=
            if isinstance(op, ast.GtE):
                parsing_trace += f"maggiore uguale di "
            # operatore minore <
            if isinstance(op, ast.Lt):
                parsing_trace += f"minore di "
            # operatore minore uguale <=
            if isinstance(op, ast.LtE):
                parsing_trace += f"minore uguale di "

        # prendo il valore a destra dell'operatore
        comparators = node.comparators
        right = comparators[0]
        # se il valore a destra dell'operatore è una costante
        if isinstance(right, ast.Constant):
            visitor.visit_Constant(right)
        # se il valore a destra dell'operatore è una variabile
        elif isinstance(right, ast.Name):
            visitor.visit_Name(right)
        # se il valore a destra è un insieme di operazioni
        elif isinstance(right, ast.BinOp):
            visitor.visit_BinOp(right)
        # se il valore a destra è una chiamata di funzione
        elif isinstance(right, ast.Call):
            visitor.visit_Call(right)

    # trigger di un ciclo for
    def visit_For(self, node):
        global parsing_trace
        parsing_trace += f"ciclo For, "
        # indice del mio ciclo
        parsing_trace += f" con indice "
        visitor.visit_Expr(node.target)
        # Gestione condizione del ciclo for
        iter_ = node.iter
        if isinstance(iter_, ast.Call) and isinstance(iter_.func, ast.Name):
            # se utilizzo la funzione range per iterare, faccio il parsing di start, stop, step
            if iter_.func.id == 'range':
                parsing_trace += f" nell' intervallo: "
                start = iter_.args[0].n if len(iter_.args) >= 1 else 0
                stop = iter_.args[1].n if len(iter_.args) >= 2 else None
                step = iter_.args[2].n if len(iter_.args) >= 3 else 1
                parsing_trace += f" start uguale a {start}, stop uguale a {stop}, step uguale a {step}. "
            # altrimenti analizzo l'espressione fornita
        # se itero su una Lista, espressione, metodo, faccio il parsing dell' espressione
        else:
            parsing_trace += f"Iterando su: "
            visitor.visit_Expr(iter_)

        parsing_trace += ".\n"

        # corpo del ciclo
        for el in node.body:
            # faccio il parsing su tutte le espressioni del corpo
            visitor.visit_Expr(el)

        parsing_trace += "fine ciclo For. \n"

    # trigger di un ciclo while
    def visit_While(self, node):
        global parsing_trace
        parsing_trace += f"ciclo While "
        # condizione del ciclo
        parsing_trace += f"con condizione "
        visitor.visit_Expr(node.test)
        parsing_trace += ".\n"
        # corpo del ciclo
        for el in node.body:
            # faccio il parsing su tutte le espressioni del corpo
            visitor.visit_Expr(el)

        parsing_trace += "\n"
        parsing_trace += "fine ciclo While.\n"

    # trigger di un argomento di funzione
    def visit_arg(self, node):
        global parsing_trace
        parsing_trace += f"{node.arg}, "

    # trigger di una stringa composta da variabili
    def visit_JoinedStr(self, node):
        # faccio il parsing di ogni valore che compone la stringa
        for el in node.values:
            # se il contenuto è composto da una costante
            if isinstance(el, ast.Constant):
                visitor.visit_Constant(el)
            # casi generici
            else:
                self.generic_visit(el)

    # trigger di una definizione di funzione
    def visit_FunctionDef(self, node):
        global parsing_trace
        # definizione funzione senza alcun parametro
        if not node.args.args:
            parsing_trace += f"Definizione della funzione {node.name}, nessun parametro. \n "
        # definizione funzione con parametri passati in ingresso
        else:
            parsing_trace += f"Definizione della funzione {node.name}, con parametri: "
            for arg in node.args.args:
                visitor.visit_arg(arg)
            parsing_trace += ".\n"

        # parsing del corpo della funzione, insieme di espressioni
        for el in node.body:
            # se il corpo è un istruzione return
            if isinstance(el, ast.Return):
                visitor.visit_Return(el)
            # casi generici
            else:
                visitor.visit_Expr(el)

        parsing_trace += f"Fine corpo della funzione {node.name}. \n"

    # trigger di una chiamata di funzione
    def visit_Call(self, node):
        global parsing_trace
        # nome della funzione
        if isinstance(node.func, ast.Name):
            parsing_trace += f'Chiamata di funzione '
            for t in node.func.id:
                parsing_trace += t
            parsing_trace += " "
            parsing_trace += f", parametri: "
            # gestisco i parametri passati alla funzione
            for arg in node.args:
                # il parametro è un nome di variabile
                if isinstance(arg, ast.Name):
                    visitor.visit_Name(arg)
                # il parametro contiene un operatore
                elif isinstance(arg, ast.BinOp):
                    visitor.visit_BinOp(arg)
                # il parametro è una costante
                elif isinstance(arg, ast.Constant):
                    visitor.visit_Constant(arg)
                # il parametro è una chiamata di una seconda funzione
                elif isinstance(arg, ast.Call):
                    visitor.visit_Call(arg)
                # il parametro è una lista, array
                elif isinstance(arg, ast.Subscript):
                    visitor.visit_Subscript(arg)
                # il parametro è una stringa composta da variabili (es : f"")
                elif isinstance(arg, ast.JoinedStr):
                    visitor.visit_JoinedStr(arg)
                # Parametro non gestito
                else:
                    # se un parametro non è gestito, stampo la sua tipologia
                    print(arg)
            # Se non viene passato nessun parametro
            if not node.args:
                parsing_trace += f"vuoto. "
            parsing_trace += f".\n"

    # trigger operatori
    def visit_BinOp(self, node):
        global parsing_trace

        # se il valore a sinistra dell'operatore è una costante
        if isinstance(node.left, ast.Constant):
            visitor.visit_Constant(node.left)
        # se il valore a sinistra dell'operatore è una variabile
        elif isinstance(node.left, ast.Name):
            visitor.visit_Name(node.left)
        # se il valore a sinistra dell'operatore è una funzione
        elif isinstance(node.left, ast.Call):
            visitor.visit_Call(node.left)

        parsing_trace += f"operatore "

        # operatore +
        if isinstance(node.op, ast.Add):
            parsing_trace += f"somma con "
        # operatore -
        elif isinstance(node.op, ast.Sub):
            parsing_trace += f"sottrazione con "
        # operatore *
        elif isinstance(node.op, ast.Mult):
            parsing_trace += f"moltiplicazione con "
        # operatore /
        elif isinstance(node.op, ast.Div):
            parsing_trace += f"divisione con "
        # operatore %
        elif isinstance(node.op, ast.Mod):
            parsing_trace += f"modulo della divisione con "
        # operatore potenza
        elif isinstance(node.op, ast.Pow):
            parsing_trace += f"potenza con esponente "

        # se il valore a destra dell'operatore è una costante
        if isinstance(node.right, ast.Constant):
            visitor.visit_Constant(node.right)
        # se il valore a destra dell'operatore è una variabile
        elif isinstance(node.right, ast.Name):
            visitor.visit_Name(node.right)
        # se il valore a destra dell'operatore è una funzione
        elif isinstance(node.right, ast.Call):
            visitor.visit_Call(node.right)

    # trigger di una tupla
    def visit_Tuple(self, node):
        for el in node.elts:
            visitor.visit_Expr(el)

    # trigger assegnamento variabile
    def visit_Assign(self, node):
        global parsing_trace
        parsing_trace += f"Assegnamento a , "
        # scansione dei target di assegnamento
        for target in node.targets:
            # se il target è una variabile
            if isinstance(target, ast.Name):
                visitor.visit_Name(target)
            # se il target è una tupla di variabili
            if isinstance(target, ast.Tuple):
                visitor.visit_Tuple(target)
            # se il target è un elemento di un array
            if isinstance(target, ast.Subscript):
                visitor.visit_Subscript(target)

        parsing_trace += f"il valore "
        # il valore assegnato è un espressione con operatori
        if isinstance(node.value, ast.BinOp):
            visitor.visit_BinOp(node.value)
        # il valore assegnato è una variabile
        elif isinstance(node.value, ast.Name):
            visitor.visit_Name(node.value)
        # il valore assegnato è una costante
        elif isinstance(node.value, ast.Constant):
            visitor.visit_Constant(node.value)
        # il valore assegnato è una lista
        elif isinstance(node.value, ast.List):
            visitor.visit_List(node.value)
        # il valore assegnato è una funzione
        elif isinstance(node.value, ast.Call):
            visitor.visit_Call(node.value)
        # se il valore assegnato è una tupla di valori
        if isinstance(node.value, ast.Tuple):
            visitor.visit_Tuple(node.value)
        # se il valore assegnato è un dizionario
        if isinstance(node.value, ast.Dict):
            visitor.visit_Dict(node.value)

        parsing_trace += ".\n"

    # trigger clausola if-else
    def visit_If(self, node):
        global parsing_trace

        if isinstance(node, ast.If):
            # se siamo nel corpo del if
            parsing_trace += f"Istruzione if, "
            # prima faccio il parsing della condizione del if
            parsing_trace += f"Con condizione, "
            # se la condizione è un' operazione di confronto
            if isinstance(node.test, ast.Compare):
                visitor.visit_Compare(node.test)
            # se la condizione è un nome costante (es: True, False)
            elif isinstance(node.test, ast.NameConstant):
                visitor.visit_NameConstant(node.test)
            # se la condizione è una variabile
            elif isinstance(node.test, ast.Name):
                visitor.visit_Name(node.test)
            # se la condizione è una costante
            elif isinstance(node.test, ast.Constant):
                visitor.visit_Constant(node.test)
            # se la condizione è una chiamata di funzione
            elif isinstance(node.test, ast.Call):
                visitor.visit_Call(node.test)
            # se la condizione è un'espressione
            elif isinstance(node.test, ast.Expr):
                visitor.visit_Expr(node.test)
            elif isinstance(node.test, ast.BoolOp):
                visitor.visit_BoolOp(node.test)
            # casi da gestire
            else:
                print(node.test)

            parsing_trace += ".\n"
            # poi faccio il parsing del corpo, che è un insieme di espressioni
            for body in node.body:
                visitor.visit_Expr(body)

            parsing_trace += f"Fine istruzione if, .\n"

        # se vi è anche un istruzione elif, quanti ce ne sono
        if len(node.orelse) > 0 and isinstance(node.orelse[0], ast.If):
            if isinstance(node.orelse[0], ast.If):
                # chiamo una funzione ricorsiva che visiti tutti gli elif presenti
                self.elif_if_tree(node)

        # se vi è anche un istruzione else senza elif precedenti
        else:
            # else non ha condizioni
            parsing_trace += f"Istruzione else, \n"
            # faccio il parsing del corpo, insieme di espressioni
            for body in node.orelse:
                visitor.visit_Expr(body)

            parsing_trace += f"Fine condizione else.\n"

    def elif_if_tree(self, node):
        global parsing_trace
        parsing_trace += f"Istruzione elif, "
        # prima faccio il parsing della condizione del elif
        parsing_trace += f"Con condizione, "
        # se la condizione è un' operazione di confronto
        if isinstance(node.orelse[0].test, ast.Compare):
            visitor.visit_Compare(node.orelse[0].test)
        # se la condizione è un nome costante (es: True, False)
        elif isinstance(node.orelse[0].test, ast.NameConstant):
            visitor.visit_NameConstant(node.orelse[0].test)
        # se la condizione è una variabile
        elif isinstance(node.orelse[0].test, ast.Name):
            visitor.visit_Name(node.orelse[0].test)
        # se la condizione è una costante
        elif isinstance(node.orelse[0].test, ast.Constant):
            visitor.visit_Constant(node.orelse[0].test)
        # se la condizione è una chiamata di funzione
        elif isinstance(node.orelse[0].test, ast.Call):
            visitor.visit_Call(node.orelse[0].test)
        # se la condizione è un'espressione
        elif isinstance(node.orelse[0].test, ast.Expr):
            visitor.visit_Expr(node.orelse[0].test)
        elif isinstance(node.orelse[0].test, ast.BoolOp):
            visitor.visit_BoolOp(node.orelse[0].test)
        # casi da gestire
        else:
            print(node.orelse[0].test)

        parsing_trace += ".\n"
        # poi faccio il parsing del corpo, che è un insieme di espressioni
        for body in node.orelse[0].body:
            visitor.visit_Expr(body)

        parsing_trace += f"Fine istruzione elif, .\n"

        # se vi è un ulteriore elif di seguito a questo
        if len(node.orelse[0].orelse) > 0 and isinstance(node.orelse[0].orelse[0], ast.If):
            self.elif_if_tree(node.orelse[0])
        # se vi è un else dopo questo elif
        elif len(node.orelse[0].orelse) > 0 and isinstance(node.orelse[0].orelse[0], ast.Expr):
            # else non ha condizioni
            parsing_trace += f"Istruzione else, \n"
            # faccio il parsing del corpo, insieme di espressioni
            for body in node.orelse[0].orelse:
                visitor.visit_Expr(body)

            parsing_trace += f"Fine condizione else.\n"

    # trigger degli operatori booleani
    def visit_BoolOp(self, node):
        global parsing_trace
        # se il valore a sinistra dell'operatore è una costante
        if isinstance(node.values[0], ast.Constant):
            visitor.visit_Constant(node.values[0])
        # se il valore a sinistra dell'operatore è una variabile
        if isinstance(node.values[0], ast.Name):
            visitor.visit_Name(node.values[0])
        # se il valore a sinistra dell'operatore è una funzione
        if isinstance(node.values[0], ast.Call):
            visitor.visit_Call(node.values[0])

        # operatore and
        if isinstance(node.op, ast.And):
            visitor.visit_And(node.op)
        # operatore or
        elif isinstance(node.op, ast.And):
            visitor.visit_And(node.op)
        # operatore not
        elif isinstance(node.op, ast.And):
            visitor.visit_And(node.op)

        # se il valore a destra dell'operatore è una costante
        if isinstance(node.values[1], ast.Constant):
            visitor.visit_Constant(node.values[1])
        # se il valore a destra dell'operatore è una variabile
        if isinstance(node.values[1], ast.Name):
            visitor.visit_Name(node.values[1])
        # se il valore a destra dell'operatore è una funzione
        if isinstance(node.values[1], ast.Call):
            visitor.visit_Call(node.values[1])

    # trigger operatore AND
    def visit_And(self, node):
        global parsing_trace
        parsing_trace += f"Operatore Booleano And, "
        self.generic_visit(node)

    # trigger operatore OR
    def visit_Or(self, node):
        global parsing_trace
        parsing_trace += f"Operatore Booleano Or, "
        self.generic_visit(node)

    # trigger operatore NOT
    def visit_Not(self, node):
        global parsing_trace
        parsing_trace += f"Operatore Booleano Not, "
        self.generic_visit(node)

    # trigger di una variabile globale
    def visit_Global(self, node):
        global parsing_trace
        parsing_trace += f"Variabile globale {node.names}. \n"
        self.generic_visit(node)

    # trigger istruzione return di una funzione
    def visit_Return(self, node):
        global parsing_trace
        parsing_trace += f"Valore di ritorno, "
        self.generic_visit(node)
        parsing_trace += ".\n"

    # trigger su una creazione di una lista
    def visit_List(self, node):
        global parsing_trace
        # definizione lista
        parsing_trace += f"Array "
        # se il contenuto della lista è vuoto
        if len(node.elts) == 0:
            parsing_trace += f"Con contenuto vuoto."
        # se il contenuto è un insieme di valori
        else:
            parsing_trace += f"Di elementi: "
            for el in node.elts:
                # se l'elemento è una costante
                if isinstance(el, ast.Constant):
                    visitor.visit_Constant(el)
                # se l'elemento è una variabile
                elif isinstance(el, ast.Name):
                    visitor.visit_Name(el)
            print(", .")

    # trigger su un elemento di una lista
    def visit_Subscript(self, node):
        global parsing_trace
        # indice della lista
        parsing_trace += "elemento di indice "
        # se l'indice è una costante
        if isinstance(node.slice, ast.Constant):
            visitor.visit_Constant(node.slice)
        # se l'indice è una variabile
        if isinstance(node.slice, ast.Name):
            visitor.visit_Name(node.slice)
        # nome della lista
        parsing_trace += "dell' array "
        visitor.visit_Name(node.value)

    # trigger dell' operatore try-except
    def visit_Try(self, node):
        global parsing_trace
        # nome istruzione
        parsing_trace += f"Istruzione Try, \n"
        # itero sul corpo del try
        for el in node.body:
            visitor.visit_Expr(el)
        parsing_trace += f"Fine Istruzione Try. \n"

        # istruzione except
        parsing_trace += f"Istruzione Except, "
        # nome del exception catturata dal handler
        parsing_trace += f"Con Handler di errore di tipo: "
        visitor.visit_ExceptHandler(node.handlers[0])
        parsing_trace += ", \n"
        # corpo del except
        for el in node.handlers[0].body:
            visitor.visit_Expr(el)
        parsing_trace += f"Fine Istruzione Except. \n"

    # trigger del tipo di exceptionHandler
    def visit_ExceptHandler(self, node):
        global parsing_trace
        # Gestione del nome del Handler
        parsing_trace += f"{node.type.id} "

    # trigger degli operatori assegnamento
    def visit_AugAssign(self, node):
        global parsing_trace
        # valore a sinistra dell' operatore
        visitor.visit_Name(node.target)

        # trigger operatore incremento
        if isinstance(node.op, ast.Add):
            parsing_trace += f"incrementato di, "
        # trigger operatore decremento
        if isinstance(node.op, ast.Sub):
            parsing_trace += f"decrementato di , "

        # valore a destra dell' operatore
        # se il valore è una costante
        if isinstance(node.value, ast.Constant):
            visitor.visit_Constant(node.value)
        # se il valore è una variabile
        elif isinstance(node.value, ast.Name):
            visitor.visit_Name(node.value)

        parsing_trace += "\n"

    # trigger del nome di una libreria
    def visit_alias(self, node):
        global parsing_trace
        parsing_trace += node.name

    # tigger sull'importazione di una libreria
    def visit_Import(self, node):
        global parsing_trace
        parsing_trace += f"Importazione della libreria: "
        for name in node.names:
            visitor.visit_alias(name)
        parsing_trace += ".\n"

    # trigger sull' istruzione Yield
    def visit_Yield(self, node):
        global parsing_trace
        parsing_trace += f"Istruzione yield con: "
        visitor.visit_Expr(node.value)
        parsing_trace += ", . \n"

    # trigger sulla definizione di una classe
    def visit_ClassDef(self, node):
        global parsing_trace
        # istanza della classe e nome della classe
        parsing_trace += f"Definizione della classe: {node.name}. \n"
        parsing_trace += f"corpo della classe: \n"
        # parsing del corpo della classe
        for el in node.body:
            visitor.visit_Expr(el)
        parsing_trace += f"Fine corpo della classe: {node.name}. \n"

    # trigger sulla definizione di un dizionario
    def visit_Dict(self, node):
        global parsing_trace
        # definizione di un dizionario
        parsing_trace += f"Dizionario, con valori: ,"
        # corpo del dizionario
        for key, value in zip(node.keys, node.values):
            parsing_trace += f". Nome Chiave: ,  "
            visitor.visit_Constant(key)
            parsing_trace += f" Valore assegnato: ,  "
            visitor.visit_Constant(value)
        parsing_trace += f"Fine definizione dizionario."

    # trigger sull'invocazione di un metodo di una classe
    def visit_Attribute(self, node):
        global parsing_trace
        parsing_trace += f"Metodo della classe o libreria: {node.value.id}, "
        parsing_trace += f"Con nome : ,  {node.attr} ."
        
    # trigger su un istruzione pass
    def visit_Pass(self, node):
        global parsing_trace
        # pass: lo screen reader non lo annuncia
        parsing_trace += ""
        


if __name__ == '__main__':
    print(argv[3])
    # controllo che sia stato passato il nome di un file
    if len(sys.argv) < 3:
        print("Nome file non esplicitato")
    else:
        # prendo la selezione di testo evidenziato
        code = argv[3]

        try:
            # faccio il parsing del blocco di codice
            tree = ast.parse(str(code).strip())
        except:
            # il blocco di codice passato è parziale rispetto alla sua sintassi:
            # es: passare la riga di condizione del if senza il suo corpo, o solo l'istruzione else
            engine.say("Il blocco di codice passato è parziale, è necessario passare un intero costrutto del linguaggio affinchè l'analisi venga eseguita.")
            engine.runAndWait()
            exit(1)
        
        visitor = NodeVisitor()
        visitor.visit(tree)

        # stampo il parsing ottenuto
        print(parsing_trace)
        # riproduco con il sintetizzatore il parsing ottenuto
        engine.say(parsing_trace)

        # stampa dei commenti trovati nel codice
        engine.say("\nCommenti trovati all'interno del codice: \n")
        comments_in_code = extract_comment(code)
        print(comments_in_code)
        # Lettura dei commenti trovati nel codice
        for comment in comments_in_code:
            engine.say("Nuovo commento, contenuto: , ")
            engine.say(comment + ".\n")

        engine.runAndWait()
