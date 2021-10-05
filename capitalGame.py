# On défini les pays
pays = ['Espagne', 'Italie', 'Belgique', 'France']
# on défini alors les capitales dans les même ordre que les pays ci-dessus
# pour éviter le problème de comparaison avec majuscule ou pas ? On prend
# le plis de tout mettre en minuscule
capitales = ['madrid', 'rome', 'bruxelles', 'paris']

# On initialise le score à 0
score = 0
# avec la commande suivante on permet au joueur de rentrer son nom
nomJoueur = input('Bonjour, comment t\'appelles-tu ?')

print("\n\n=> Ok %s, on va voir si tu connais ta géographie ?" % nomJoueur)

# on fait une boucle sur la longuer du vecteur contenu dans pays. En fait il s'agit d'une itération
# sur le contenu du vecteur dans la variable pays.
# pour chaque élément dans pays
for item in pays:
    # item est la valeur trouvée a chaque iteration par la boucle for
    # c'est un nom de variable arbitraire
    # la première fois, item vaudra Espagne...et ainsi de suite
    question = input("\n\n Quel est la capitale du pays appelé %s" % item)
    # pays.index permet de retourner la valeur de l'index du nom du pays
    # par exemple pour Belgique ce sera 3, du coup avec capitales[3] on obtient ...bruxelles
    # avec question.lower() on met tout en minuscule au cas ou le joueur a entré des majuscules
    if question.lower() == capitales[pays.index(item)]:
        print("Mais ouiiii, bien joué !")
        score += 1  # on incrémente le score de 1 on aurait pu écrire score = score + 1
    else:
        print("Houlaa...va falloire revoir ta géographie")

# Le jeux est fini. On donne le score avec le nom
print("\n\n\nVoilà, le jeux est fini.")
print('%s, ton score est de %s sur 4' % (nomJoueur, score))
