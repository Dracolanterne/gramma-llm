^!l:: ; Ctrl + Alt + L
clipboard := ""         
Send, ^c
Sleep, 300
ClipWait, 2

if ErrorLevel {
    MsgBox, Rien n’a été copié dans le presse-papiers.
    return
}

; Définir les chemins relatifs au dossier du script
rewritePath := A_ScriptDir
pythonExe := rewritePath . "\.conda\python.exe"
script := rewritePath . "\ollama_corrector.py"
inputFile := rewritePath . "\input.txt"
outputFile := rewritePath . "\output.txt"

; Écrit le contenu copié dans un fichier temporaire
FileDelete, %inputFile%
FileAppend, %clipboard%, %inputFile%

; Supprime l’ancienne sortie
FileDelete, %outputFile%

; Appelle le script Python (pas de redirection, il gère input/output)
RunWait, "%pythonExe%" "%script%",, Hide

; Lire le résultat dans output.txt
if !FileExist(outputFile) {
    MsgBox, ❌ Le fichier output.txt n’a pas été généré.
    return
}

FileEncoding, UTF-8
FileRead, newtext, %outputFile%

if (newtext = "") {
    MsgBox, ❌ Erreur : le modèle n’a retourné aucun texte.
    return
}

; Nettoie les retours à la ligne
StringReplace, newtext, newtext, `r`n, %A_Space%, All

Send, %newtext%
return
