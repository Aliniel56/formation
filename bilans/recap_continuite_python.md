# 🔄 Récap de continuité — Formation Python (Module 1.2)

> **Document de TRANSFERT DE CONTEXTE.** À coller au début d'une nouvelle conversation pour reprendre la formation sans perte, comme si on n'avait pas changé de conversation.
>
> **Document VIVANT** : la conversation qui le reçoit doit le **compléter** au fil de l'avancement, puis le régénérer pour la conversation suivante. Et reconduire cette consigne dans son propre récap de fin.

---

## ⚙️ INSTRUCTIONS POUR LA NOUVELLE CONVERSATION (à lire en premier)

1. **En cas de doute avant de m'aider, réclame-moi les documents manquants** plutôt que de supposer. Selon le besoin, demande-moi : le **programme complet de la formation** (`programme_formation_developpeur.md`), le **détail du fil maths**, un **bilan de module antérieur** (`~/formation/bilans/`), le **carnet de culture générale**, le **planning hebdomadaire**, ou tout document utile. Ne devine pas un contexte important : demande-le.
2. **Tiens ce document à jour** au fil de notre avancement (coche ce qui est validé, ajoute les nouveaux acquis).
3. **Reconduis ces deux consignes** (1 et 2) dans le récap de fin que tu généreras pour la conversation suivante, pour que la chaîne ne se brise jamais.
4. **Ne va jamais chercher mon code sur GitHub par fetch** (cache périmé constaté) — demande-moi de **coller mon code**.

---

## 👤 QUI JE SUIS

- **Prénom : Jeremie** · pseudo GitHub : **Aliniel56**. Débutant complet au départ.
- **Objectif** : devenir **développeur full-stack** (logiciel, jeu vidéo, web, mobile), avec objectif emploi.
- **Programme suivi** : « Programme 2 — Full-stack moderne », ~30 mois, démarré le **18/05/2026**, ~960-1000h, 4 phases.
- **Rythme réel** : 3-4 jours/semaine, sessions de **20 min à 1h** selon les jours, en parallèle des chapitres. Indisponibilités professionnelles ponctuelles (régulier malgré les coupures).
- **Budget ressources externes : gratuit uniquement.**
- **Niveau maths de départ** : collège oublié → remise à niveau intégrée (bon élève).
- **Anglais technique** : lecture lente possible.
- **Personnes pour les exemples** : Maëlle, Justine.
- **Ton rôle (Claude)** : mon formateur personnel sur le très long terme.

---

## 📐 CONVENTIONS DE TRAVAIL (à respecter)

- **Cours = PDF denses, soignés, visuels**, générés via `wkhtmltopdf` (encadrés colorés, diagrammes, exercices, récap « à retenir »). **Corrigés jamais dans les PDF.**
- **Correction des exercices** : tu **cites textuellement ma réponse** avant de la commenter. Tu n'inventes **jamais** d'erreurs.
- **Nommage des variables en anglais sans accent** (les messages affichés peuvent rester en français). Singulier pour l'élément, pluriel pour la collection (`for fruit in fruits`).
- **Interros surprises** sans prévenir (« STOP — Interro surprise » ou questions glissées), rappel espacé (intervalles croissants), **jamais deux d'affilée**. Sécher = signal de révision, esprit bienveillant. *Score Module 1.1 : 4,5/5 — à réviser : `cd` vs `mkdir`, `|` vs `&&`.*
- **Git en continu** : commits fréquents et atomiques, « réflexes Git » insérés dans les cours.
- **Maths en double fil** : (1) « juste-à-temps » avant les chapitres qui en ont besoin ; (2) « maths de fond » ~1h/sem en parallèle.
- **Exercices de consolidation** après les chapitres épineux (même si je n'ai pas de mal), et exercices **plus poussés** quand j'ai de la marge.
- **Travail hors-ligne** : les PDF permettent de bosser sans connexion.
- **Planning hebdomadaire (Bloc A)** : à régénérer à chaque nouveau module atteint.
- **Documents de fin de module** : protocole = tu repères la fin du module → tu me l'annonces → on échange (zones d'ombre) → je valide → tu génères. Deux bilans **distincts** : un **technique** (sujet du module) + le **carnet de culture générale** (transverse, vivant). Tous en **PDF + Markdown**, rangés dans `~/formation/bilans/`.

---

## 💻 ENVIRONNEMENT TECHNIQUE

- **PC maison** : Windows + WSL2 + Ubuntu 24.04 LTS (environnement principal).
- **2ᵉ machine** : **ASUS ROG sous Debian 13 + XFCE** (installée et configurée, je travaille aussi depuis là).
- **Dossier racine de TOUTE la formation** : `~/formation/` (identique sur les deux machines).
  - Code Python : `~/formation/python/chapitre-N/`
  - Bilans : `~/formation/bilans/`
- **Dépôt** : `git@github.com:Aliniel56/python_exercice.git` (SSH).
- **Git** : `Jeremie Le Dortz` / `jeremield@laposte.net`, branche `main`, SSH ed25519 (une clé par machine).
- **Rituel deux machines** : `git pull` en arrivant, `git push` en partant.
- **`.gitignore`** en place à la racine (contient `*Zone.Identifier` — parasites Windows).
- ⚠️ **Ne pas fetch le dépôt GitHub** (cache périmé) — me demander de coller mon code.

---

## 📍 OÙ J'EN SUIS (état précis)

**Module 1.1 — ✅ TERMINÉ** (bilan technique généré).

**Module 1.2 (Python) — 🔄 EN COURS :**

| Chapitre | Statut |
|---|---|
| 1.2.1 Premiers pas Python | ✅ validé |
| 1.2.2 Flux de contrôle | ✅ validé (+ jeu du nombre mystère) |
| Consolidation Boucles | ✅ validée (dont FizzBuzz) |
| 1.2.3 Fonctions | ✅ validé (9 exercices) |
| 1.2.4 Structures de données | ✅ validé (9 exercices) |
| **Consolidation Listes & Dictionnaires** | 🔄 **EN COURS** |

**Détail de la consolidation en cours :**
- **Partie A (A1 → A9)** : ✅ **TOUS validés** (moyenne formatée, inversion, filtrage, comptage, concaténation/tri ; capitales avec refacto « 4 boucles → 1 boucle », personne la plus âgée à la main, inversion de dictionnaire, compteur de votes).
- **B1 — liste de courses intelligente** : ✅ validé (dictionnaire, menu, suppression auto quand quantité ≤ 0).
- **➡️ À FAIRE — B2 — statistiques d'une classe** : **LE plus important** — pattern **liste de dictionnaires** (`students = [{"name":..., "grade":...}, ...]`). Parcours, moyenne, meilleure note, élèves en échec.
- **À FAIRE — B3 — analyseur de texte** (défi) : nb de mots, mots uniques (`set`), mot le plus long, compte de chaque mot ; idéalement découpé en fonctions.
- **À FAIRE — C1 — mini-inventaire de jeu** (optionnel) : **dictionnaire de dictionnaires**.

**➡️ ENSUITE : chapitre 1.2.5 (chaînes de caractères avancées).**

---

## 🗺️ SUITE DU MODULE 1.2

- **1.2.5** Chaînes de caractères avancées
- **1.2.6** Gestion des erreurs (`try`/`except`)
- **1.2.7** Modules + création d'exécutable (PyInstaller)
- **1.2.8** Fichiers — **PERSISTANCE** (reprendre le carnet de contacts pour le rendre persistant)
- **1.2.9** POO (programmation orientée objet) + consolidation
- **1.2.10** Projet : jeu de cartes
- **1.2.11** BONUS : Tkinter (interface graphique) + exécutable `.exe`

---

## 🧮 FIL MATHS

- **Double fil** : juste-à-temps (avant les chapitres) + maths de fond (~1h/sem).
- **Fait** : Logique booléenne (JIT) ✅ · F1 Arithmétique & algèbre ✅
- **Disponible non commencé** : F2 Géométrie & coordonnées (Pythagore, plan cartésien, distance, axe Y inversé à l'écran — utile jeu vidéo).
- **À venir** : F3 Fonctions · F4 Pourcentages · F5 Ensembles/logique · F6 Statistiques · F7 Suites/récurrence.

---

## 🎒 RESSOURCES EXTERNES (boîte à outils — planning Bloc A actif)

- **Pratique du code** : Exercism (piste Python, principale) · CheckiO · Codewars · Codingame
- **Visualisation** : Python Tutor (voir la mémoire) · VisuAlgo (algos, pour le 1.3)
- **Révision système/Git** : Learn Git Branching · Bandit / OverTheWire
- **Mémorisation** : Anki (~10 min/jour)
- **Maths** : Khan Academy
- **Lecture/référence** : Swinnen (PDF FR) · Stack Overflow · Graven / Grafikart (YouTube FR)
- **Règles** : max **2 ressources « cours »** en parallèle · anti « tutorial hell » (coder autant que consommer) · règle des trois temps (≈ 50% fondation / 30% réflexe / 20% culture).
- **Planning hebdomadaire Bloc A** : sessions complémentaires 3-4 j/sem (20 min-1h), à régénérer au prochain module.

---

## 📚 DOCUMENTS DE BILAN EXISTANTS (`~/formation/bilans/`)

- `bilan_1.1_technique` (PDF + md) — clôture du Module 1.1.
- `carnet_culture_generale` (PDF + md) — **VIVANT**, à me redonner et à compléter (API, vibe coding, modules, ressources hors-ligne, Windows/Linux…).
- `recap_continuite_python` (ce document, PDF + md) — **VIVANT**, à compléter.
- *(à venir)* `encyclopedie_linux`, `journal_git`.

---

## 🌟 MES QUALITÉS NOTÉES (pour calibrer)

Je pose des questions de fond et je cherche à **comprendre** (pas juste à faire marcher). Je débogue de plus en plus seul. Je vais volontiers **au-delà des consignes** (mais je tends parfois à **sur-complexifier** → la leçon de simplification « 4 boucles → 1 boucle » a déjà été vue, à me la rappeler si besoin). Je suis **honnête** (je signale quand je cherche une solution sur internet).

---

*Récap de continuité Python · Module 1.2 · document de transfert vivant · v1.0 — à compléter et régénérer de conversation en conversation*
