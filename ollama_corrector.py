from ollama import chat
from pathlib import Path

# Définir le dossier courant du script
base_path = Path(__file__).parent.resolve()

# Fichiers relatifs
input_path = base_path / "input.txt"
output_path = base_path / "output.txt"

# Lire le texte depuis input.txt
with open(input_path, "r", encoding="latin-1") as f:
    text = f.read().strip()

# Préparer le prompt
#prompt = f"""Corrige les fautes d’orthographe, de grammaire et de syntaxe.

#Améliore la cohérence du texte si nécessaire (enchaînement logique, clarté), 
#mais **garde l’intention, le ton et le style d’origine**.

#N’édulcore pas le langage, ne rends pas le texte plus poli ou neutre, 
#et ne remplace pas les expressions familières ou orales.

#Réponds uniquement avec le texte corrigé, sans explication.

#Texte :
#{text}
#"""




# Appeler Ollama
response = chat(
    model='phi4',
    messages=[
        {
            'role': 'system',
            'content': (
                "Tu es un correcteur orthographique et grammatical. "
                "Tu corriges les fautes **sans changer le sens ni le style du texte**, "
                "même s'il est familier ou oral. "
                "Ne fais **aucune traduction ni explication**. "
                "Réponds uniquement avec la version corrigée."
            )
        },
        {
            'role': 'user',
            'content': text
        }
    ]
)

# Récupérer la réponse
output = response.message.content.strip()

# Écrire dans output.txt
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Résultat écrit dans output.txt")
