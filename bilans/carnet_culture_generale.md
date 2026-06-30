# 📓 Carnet de culture générale — Formation Développeur

> **Document VIVANT et ÉVOLUTIF.** Il n'est lié à aucun module en particulier : il regroupe toutes mes questions transverses (qui ne portent pas sur le sujet technique du moment).
>
> **Protocole d'utilisation :**
> 1. Je donne ce fichier à chaque nouvelle conversation.
> 2. À la fin d'une conversation (ou d'un module), Claude le **complète** avec mes nouvelles questions transverses.
> 3. Je le re-commit dans `~/formation/bilans/` à chaque mise à jour.
>
> Ainsi il grandit tout au long de la formation sans jamais se perdre, et reste consultable hors-ligne.

---

## Comment ajouter une entrée (format)

Chaque entrée suit ce gabarit :

```
### [Sujet] — (surgi au Module X.Y)
**La question :** ...
**La réponse en bref :** ...
**À retenir :** ...
```

---

## Entrées

### API (Application Programming Interface) — (surgi au Module 1.2)

**La question :** « Je vois souvent ce terme, qu'est-ce que c'est ? »

**La réponse en bref :** Une API est une façon pour deux programmes de communiquer entre eux — un intermédiaire qui cache la complexité. Image : le serveur au restaurant, qui prend ta commande (via le menu) et te rapporte ton plat sans que tu ailles en cuisine. Deux grands sens :
- **API locales** (bibliothèques) : quand tu appelles `random.randint()` ou `.append()`, tu utilises l'API de ces outils sans savoir comment ils marchent à l'intérieur.
- **API web** (services distants) : ton programme demande des données à un serveur sur internet (météo, carte, paiement…). La réponse arrive souvent en **JSON**, qui ressemble exactement à des dictionnaires/listes Python imbriqués.

**À retenir :** Le JSON (format d'échange universel) = des dictionnaires et des listes. D'où l'importance de maîtriser ces structures. On apprend à **utiliser** les API en Phase 2, puis à en **créer** (Module 2.4, API REST).

---

### Vibe coding — (surgi au Module 1.2)

**La question :** « C'est quoi le "vibe coding" ? »

**La réponse en bref :** Terme inventé par Andrej Karpathy (février 2025). Coder en décrivant ce qu'on veut en langage naturel à une IA, qui génère le code — dans sa version extrême, sans même relire le code produit. Outil puissant **pour un expert** (qui sait lire et corriger ce que l'IA sort), mais **pas une façon d'apprendre** : un débutant qui s'en sert saute la construction des fondations.

**À retenir :** Analogie du robot-chef : il est utile à qui sait déjà cuisiner. La bonne façon de tirer parti de l'IA en programmation, c'est de savoir programmer sans elle d'abord. À garder pour plus tard, une fois les bases solides.

---

### Module / bibliothèque — (surgi au Module 1.2)

**La question :** (au fil de l'eau, sur `random`, `datetime`…)

**La réponse en bref :** Un module (ou une bibliothèque) est un ensemble de fonctions toutes prêtes que quelqu'un d'autre a écrites, et que tu peux importer pour t'en servir sans réinventer la roue. `random` (nombres aléatoires), `datetime` (dates/heures) en sont des exemples. Tu les utilises via leur API (voir entrée API).

**À retenir :** `import module` puis `module.fonction()`. Tu profites du travail des autres ; c'est le principe des « briques Lego » de la programmation.

---

### Ressources hors-ligne & livres — (surgi au Module 1.2)

**La question :** « Quels livres / manuels puis-je utiliser hors connexion ? »

**La réponse en bref :** Gérard Swinnen, *Apprendre à programmer avec Python* (PDF gratuit en français, imprimable). Pour les maths : manuels scolaires de seconde/première. Et l'idée d'imprimer les PDF de cours générés pour travailler sur papier. La pratique du code sur papier est valorisée.

**À retenir :** Travailler hors-ligne est possible et formateur. Le papier aide à ancrer.

---

### Différences Windows / Linux — (surgi au Module 1.2, lors du passage à Debian)

**La question :** « Qu'est-ce qui change entre Windows et Linux en termes de programmes / fonctionnalités ? »

**La réponse en bref :** Windows = produit fermé, livré clé en main mais on subit les choix de l'éditeur. Linux = système ouvert et libre, contrôle total mais on met parfois les mains dedans. Pour **apprendre à coder**, les deux sont équivalents à ~95 % : VS Code, Git, Python sont identiques, le code est le même, GitHub fait le pont. Linux ajoute une couche de compréhension du système précieuse pour un développeur.

> **Cette entrée est volontairement résumée. Le détail complet (compatibilité des programmes, Wine, machines virtuelles, alternatives natives, dual boot, bascule Windows → Linux) se trouve dans le document dédié : `encyclopedie_linux`.**

---

## 🆕 Espace pour les prochaines entrées

*(Claude ajoute ici les nouvelles questions transverses au fil des conversations, en respectant le gabarit ci-dessus.)*

---

*Carnet de culture générale · Formation Développeur Full-Stack · démarré au Module 1.1–1.2 · document évolutif*
