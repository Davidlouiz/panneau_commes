# Panneau Site de Vol Libre de COMMES

Panneau d'information pour le site de parapente/delta de Commes (Calvados), géré par le Club AS Icare.

Version actuelle : `panneau_commes_v6.html`
Format actuel : `100 cm × 80 cm`

## ⬇️ [Télécharger le panneau en PDF](https://raw.githubusercontent.com/Davidlouiz/panneau_commes/main/panneau_commes.pdf)

![Aperçu du panneau](panneau_preview.png)

---

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `panneau_commes_v6.html` | Version active du panneau (HTML + CSS auto-contenu) |
| `panneau_commes_v4.html` | Variante de référence précédente |
| `export_pdf.sh` | Script d'export PDF de la v6 via Playwright |
| `panneau_commes_v1.jpg` | Photo aérienne du site (col. centrale) |
| `fc25943c-...jpg` | Photo parapentiste (colonne droite) |
| `orientation.svg` | Schéma d'orientation du site |
| `screenshot.py` | Script utilitaire pour régénérer l'aperçu PNG de la v6 |

---

## Modifier le panneau

Ouvrir `panneau_commes_v6.html` dans un éditeur de texte ou VS Code. Le fichier est autonome (HTML + CSS dans un seul fichier).

### Structure des colonnes

```
┌──────────────┬─────────────────────────────────────────┬──────────────┐
│  Col A       │  Image principale / avertissements      │  Col D       │
│  Infos       │  + obligations                          │  Dangers     │
│  + QR codes  │                                         │  + photo     │
└──────────────┴──────────────────────┴──────────────────┴──────────────┘
```

### Modifier les textes

- **Infos pratiques (GPS, altitude, fréquence…)** : rechercher les balises `<div class="info-label">` et `<div class="info-value">` dans la section `<!-- COL A -->`
- **QR codes** : bloc `<div class="qr-box">` dans la colonne A
- **Avertissements** : balises `<div class="warn-item">` et `<div class="warn-en">` dans `<div class="warn-box">`
- **Obligations** : listes `<ul class="bullets">` dans `<div class="col-bc-right">`
- **Dangers particuliers** : balises `<div class="danger-title">` et `<div class="danger-body">` dans `<!-- COL D -->`
- **Header / logos** : bloc `<header>` et classes `.header-*`

### Modifier les couleurs

Les couleurs sont définies dans les variables CSS en haut du fichier :

```css
:root {
  --dark-blue: #1A3A5C;   /* header, footer */
  --mid-blue:  #2E6DA4;   /* titres de section */
  --accent-red: #C0392B;  /* avertissements */
  ...
}
```

### Remplacer les photos

- **Photo aérienne** : remplacer `panneau_commes_v1.jpg` par une image de même nom (ou modifier le `url()` dans la classe `.photo-aerial`)
- **Photo parapentiste** : remplacer l'attribut `src` de la balise `<img class="photo-para">` dans la colonne D

---

## Exporter en PDF

### Prérequis (première fois)

```bash
# Créer un environnement Python
python3 -m venv .venv
.venv/bin/pip install playwright pillow
.venv/bin/playwright install chromium
```

### Générer le PDF

```bash
bash export_pdf.sh
```

Le PDF `panneau_commes.pdf` est généré dans le dossier. Format `100 cm × 80 cm`, rendu identique au navigateur.

### Régénérer l'aperçu PNG

```bash
.venv/bin/python screenshot.py
```

L'aperçu `panneau_preview.png` est généré au ratio `100 cm × 80 cm` avec un filigrane `EXEMPLE`.

---

## Licence

Photo aérienne : David L. – CC BY-SA 4.0
