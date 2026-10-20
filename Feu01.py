# EVALUER UNE EXPRESSION

# Le programme evalue une expression saisie par l'utilisateur avec +, -, *, / et %.

import ast
import operator

# Associer chaque operateur autorise a la fonction Python qui l'effectue.
OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
}

def evaluer_expression(noeud):
    # Etape 1 : accepter les nombres entiers et decimaux.
    if isinstance(noeud, ast.Constant) and type(noeud.value) in (int, float):
        return noeud.value

    # Etape 2 : traiter les signes devant un nombre ou une expression, comme -3.
    if isinstance(noeud, ast.UnaryOp) and isinstance(noeud.op, (ast.UAdd, ast.USub)):
        valeur = evaluer_expression(noeud.operand)
        return valeur if isinstance(noeud.op, ast.UAdd) else -valeur

    # Etape 3 : evaluer recursivement les operations autorisees.
    # L'arbre syntaxique conserve les priorites operatoires et les parentheses.
    if isinstance(noeud, ast.BinOp) and type(noeud.op) in OPERATIONS:
        gauche = evaluer_expression(noeud.left)
        droite = evaluer_expression(noeud.right)
        return OPERATIONS[type(noeud.op)](gauche, droite)

    # Refuser toute construction qui n'est pas un nombre ou une operation autorisee.
    raise ValueError("Expression non autorisee. Utilisez uniquement des nombres et +, -, *, /, %.")


def calculer(expression):
    # Transformer l'expression en arbre, puis evaluer sa racine.
    arbre = ast.parse(expression, mode="eval")
    return evaluer_expression(arbre.body)


def main():
    # Etape 1 : demander l'expression a calculer.
    expression = input("Entrez une expression avec +, -, *, / et % : ").strip()
    if not expression:
        print("Erreur : l'expression ne peut pas etre vide.")
        return

    # Etape 2 : calculer l'expression et signaler les erreurs de syntaxe ou de calcul.
    try:
        resultat = calculer(expression)
    except SyntaxError:
        print("Erreur : expression mathematique invalide.")
        return
    except ZeroDivisionError:
        print("Erreur : division ou modulo par zero impossible.")
        return
    except ValueError as erreur:
        print(f"Erreur : {erreur}")
        return

    # Etape 3 : afficher le resultat du calcul.
    print(f"Resultat : {resultat}")


if __name__ == "__main__":
    main()
