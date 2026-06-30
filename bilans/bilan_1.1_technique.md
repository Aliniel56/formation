# Bilan technique — Module 1.1 : Mise en place de l'environnement

> **Statut du module : ✅ TERMINÉ et VALIDÉ**
> Interro surprise passée : **4,5 / 5** (points à réviser notés en Partie 2).
> Document de référence — à archiver dans `~/formation/bilans/` et à imprimer.

---

## À quoi sert ce document

Ce n'est pas un cours, c'est un **aide-mémoire de clôture**. Quand, dans plusieurs mois, tu seras sur un projet et qu'un doute surgira sur une commande, un réflexe Git ou une configuration vue au tout début, tu ouvres ce fichier plutôt que de tout relire. Il condense : ce que tu as appris, les erreurs que tu as commises (et comment les éviter), et l'état final de ton environnement.

---

## Partie 1 — Ce que tu as appris (notions clés)

### 1.1 — L'ordinateur et les systèmes

- **Système d'exploitation (OS)** : la couche logicielle qui fait le pont entre le matériel et tes programmes (Windows, Linux, macOS).
- **WSL2** (Windows Subsystem for Linux) : un vrai noyau Linux qui tourne à l'intérieur de Windows. Ce n'est pas une simulation — c'est du Linux authentique. Tu y as installé **Ubuntu 24.04 LTS**.
- **Différence mémoire vive / stockage** : la RAM est volatile (vidée à l'extinction), le disque est persistant. Notion clé qui reviendra pour la persistance des données (fichiers, chapitre 1.2.8).

### 1.2 — La ligne de commande (le terminal)

Le terminal, c'est piloter l'ordinateur par du texte plutôt que par la souris. Les commandes maîtrisées :

| Commande | Rôle |
|---|---|
| `pwd` | Affiche où tu te trouves (print working directory) |
| `ls` / `ls -la` / `ls -lh` | Liste les fichiers (avec détails / tailles lisibles) |
| `cd dossier` | **Se déplacer** dans un dossier (change directory) |
| `cd ..` | Remonter d'un niveau |
| `mkdir dossier` | **Créer** un dossier (make directory) |
| `touch fichier` | Créer un fichier vide |
| `cat fichier` | Afficher le contenu d'un fichier |
| `cp` / `mv` / `rm` | Copier / déplacer / supprimer |
| `sudo` | Exécuter en administrateur (demande le mot de passe) |
| `apt` | Le gestionnaire de paquets (installer/mettre à jour des logiciels) |

**Deux opérateurs de chaînage à ne pas confondre :**
- `|` (le **pipe**) : prend la **sortie** de la commande de gauche et la donne en **entrée** à celle de droite. Sert à enchaîner un flux de données. Ex : `ls | grep ".py"`.
- `&&` : exécute la commande de droite **seulement si** celle de gauche a réussi. Sert à enchaîner des exécutions conditionnellement. Ex : `apt update && apt upgrade`.

### 1.3 — VS Code

- Lancer l'éditeur sur un fichier : `code fichier.py`
- **Terminal intégré** : coder et lancer ses commandes dans la même fenêtre.
- **Connexion à WSL** : VS Code tourne côté Windows mais édite les fichiers Linux de façon transparente.
- **Extensions installées** : Python, Pylance, GitLens, Better Comments, Code Spell Checker (+ dictionnaire français), indent-rainbow, Material Icon Theme, Dracula (thème), French Language Pack, WSL.

### 1.4 — Git & GitHub

Git versionne ton code (historique de toutes tes modifications) ; GitHub héberge ce dépôt en ligne (sauvegarde + pont entre machines).

| Commande | Rôle |
|---|---|
| `git init` | Démarrer le suivi d'un dossier |
| `git status` | Voir l'état (fichiers modifiés, prêts à commit…) |
| `git add .` | Préparer les fichiers pour le prochain commit |
| `git commit -m "message"` | Enregistrer un instantané avec un message |
| `git log` | Voir l'historique des commits |
| `git branch` | Lister les branches |
| `git checkout -b nom` | Créer une branche **et** s'y placer |
| `git merge X` | Fusionner la branche **X dans la branche courante** |
| `git push` | Envoyer vers GitHub |
| `git pull` | Récupérer depuis GitHub |
| `git clone <url>` | Copier un dépôt distant en local |

**Réflexes acquis :**
- Commits **fréquents et atomiques** (un commit = une idée), avec messages clairs.
- Workflow par **branches** maîtrisé.
- **Sens du merge** compris : « destination d'abord, puis merge la source ». `git merge X` ramène X dans la branche où tu te trouves.
- Synchroniser sa branche de travail en récupérant `main` dedans = réflexe pro.
- Clé **SSH ed25519** pour s'authentifier auprès de GitHub sans mot de passe à chaque fois (une clé par machine).

### 1.5 — Ton environnement final (récap config)

- **OS de travail** : WSL2 + Ubuntu 24.04 LTS (PC maison) ; **+ ASUS ROG sous Debian 13 + XFCE** (seconde machine).
- **Git** : `user.name = Jeremie Le Dortz`, `user.email = jeremield@laposte.net`, branche par défaut `main`, authentification SSH ed25519.
- **Dépôt** : `git@github.com:Aliniel56/python_exercice.git`
- **Dossier racine de formation** : `~/formation/` (identique sur les deux machines), avec `~/formation/python/chapitre-N/`.

---

## Partie 2 — Erreurs commises & méthodes de résolution

### Erreur 1 — Confusion `cd` et `mkdir` (relevée à l'interro)

- **Le problème** : utiliser l'une pour l'autre. `cd` se **déplace**, `mkdir` **crée**.
- **Solution directe** : `cd` = *change directory* (se rendre quelque part) ; `mkdir` = *make directory* (fabriquer un dossier).
- **Méthode pour ne plus se tromper** : traduis le mot anglais. « make » = fabriquer → création. « change directory » = changer de dossier → déplacement. Si tu hésites, `pwd` + `ls` te montrent où tu es et ce qu'il y a, avant d'agir.

### Erreur 2 — Confusion `|` (pipe) et `&&` (relevée à l'interro)

- **Le problème** : mélanger les deux opérateurs de chaînage.
- **Solution directe** : `|` fait circuler des **données** (sortie → entrée) ; `&&` enchaîne des **exécutions** (« et ensuite, si ça a marché »).
- **Méthode pour ne plus se tromper** : pose-toi la question « est-ce que je veux passer un *résultat* à la commande suivante (→ `|`), ou *lancer* la commande suivante seulement si la première réussit (→ `&&`) ? ».

> **Note** : ton historique Git est propre, tu n'as quasiment pas commis d'erreurs sur la partie versionnement. Les deux points ci-dessus sont les seuls vrais accrocs du module, tous deux sur la ligne de commande.

---

## Partie 3 — Questions posées & réponses (spécifiques au module)

*(Les questions transverses — API, vibe coding, etc. — sont dans le `carnet_culture_generale`, pas ici.)*

- **« Pourquoi une clé SSH par machine et pas la même partout ? »** → Chaque machine génère sa propre clé ; on n'en copie pas une d'un PC à l'autre. C'est plus sûr (on peut révoquer l'accès d'une seule machine) et c'est la pratique standard.
- **« Dans quel sens va `git merge` ? »** → `git merge X` fusionne X **dans la branche courante**. D'où le réflexe : se placer d'abord sur la branche de destination, puis merger la source.

---

## Partie 4 — À retenir absolument (la checklist)

1. **Le terminal est ton outil central** : `pwd` pour savoir où tu es, `ls` pour voir, `cd` pour te déplacer, `mkdir` pour créer.
2. **`|` = données, `&&` = exécution conditionnelle.**
3. **Git en continu** : commits fréquents, atomiques, bien nommés.
4. **`git merge X` ramène X dans la branche courante** : destination d'abord.
5. **Rituel deux machines** : `git pull` en arrivant, `git push` en partant.
6. **Une clé SSH par machine**, ajoutée à GitHub.
7. **Ton dossier de travail est `~/formation/`** sur toutes tes machines.

---

*Bilan technique Module 1.1 · Formation Développeur Full-Stack · v1.0*
