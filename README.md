# Correcteur Automatique de Texte avec Ollama

Un outil de correction automatique de texte qui utilise Ollama et l'IA pour corriger les fautes d'orthographe, de grammaire et de syntaxe tout en préservant le style et le ton d'origine.

## 🚀 Fonctionnalités

- **Correction automatique** : Corrige les fautes d'orthographe, de grammaire et de syntaxe
- **Préservation du style** : Garde l'intention, le ton et le style d'origine du texte
- **Raccourci clavier** : Correction rapide avec `Ctrl + Alt + L`
- **Modèle IA** : Utilise le modèle Phi-4 d'Ollama pour des corrections intelligentes
- **Interface simple** : Copiez votre texte, appuyez sur le raccourci, obtenez le texte corrigé

## 📋 Prérequis

- [Ollama](https://ollama.com/) installé sur votre système
- Le modèle `phi4` téléchargé dans Ollama
- Python 3.x
- AutoHotkey (pour Windows)

## 🛠️ Installation

1. **Installer Ollama** :
   ```bash
   # Windows
   # Téléchargez et installez depuis https://ollama.com/download/OllamaSetup.exe
   
   # macOS
   # Téléchargez depuis https://ollama.com/download/Ollama-darwin.zip
   
   # Linux
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Télécharger le modèle Phi-4** :
   ```bash
   ollama pull phi4
   ```

3. **Installer les dépendances Python** :
   ```bash
   pip install ollama
   ```

4. **Installer AutoHotkey** (Windows uniquement) :
   - Téléchargez depuis [autohotkey.com](https://www.autohotkey.com/)

## 🎯 Utilisation

### Méthode 1 : Raccourci clavier (recommandé)

1. Sélectionnez le texte à corriger dans n'importe quelle application
2. Appuyez sur `Ctrl + Alt + L`
3. Le texte corrigé remplace automatiquement votre sélection

### Méthode 2 : Fichiers manuels

1. Placez votre texte dans le fichier `input.txt`
2. Exécutez le script Python :
   ```bash
   python ollama_corrector.py
   ```
3. Le texte corrigé apparaît dans `output.txt`

## 📁 Structure du projet

```
├── ollama_corrector.py    # Script principal de correction
├── copilot.ahk           # Script AutoHotkey pour le raccourci clavier
├── input.txt             # Fichier d'entrée pour le texte à corriger
├── output.txt            # Fichier de sortie avec le texte corrigé
└── README.md             # Ce fichier
```

## ⚙️ Configuration

### Changer le modèle IA

Pour utiliser un autre modèle Ollama, modifiez la ligne suivante dans `ollama_corrector.py` :

```python
response = chat(
    model='phi4',  # Remplacez par le nom de votre modèle préféré
    # ...
)
```

### Modifier le prompt de correction

Vous pouvez personnaliser le prompt de correction en modifiant le contenu du message système dans `ollama_corrector.py`.

## 🔧 Dépannage

### Ollama ne répond pas
- Vérifiez qu'Ollama est en cours d'exécution : `ollama serve`
- Vérifiez que le modèle est téléchargé : `ollama list`

### Erreur de modèle non trouvé
- Téléchargez le modèle : `ollama pull phi4`
- Ou changez le modèle dans le script

### Le raccourci clavier ne fonctionne pas
- Vérifiez qu'AutoHotkey est installé
- Relancez le script `copilot.ahk`
- Vérifiez qu'aucun autre programme n'utilise le raccourci `Ctrl + Alt + L`

## 📝 Exemple d'utilisation

**Texte original** :
```
franchement c'est meilleur mnt que je lui definie le role ainsi vraiment meilleur, il me fait mois de fraiyeur.
```

**Texte corrigé** :
```
Franchement, c'est mieux maintenant que je lui définis le rôle ainsi, vraiment mieux, il me fait moins de frais.
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouveaux modèles de correction

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

- [Ollama](https://ollama.com/) pour l'infrastructure d'IA locale
- [AutoHotkey](https://www.autohotkey.com/) pour l'automatisation Windows
- Le modèle Phi-4 de Microsoft pour les capacités de correction
