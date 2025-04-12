# 🧹 WordCleaner 🇮🇹

Questo script Python, chiamato `WordCleaner`, è progettato per leggere un file di testo contenente un elenco di parole (presumibilmente nel formato `parola conteggio1 conteggio2`), applicare una serie di filtri per identificare e separare le parole considerate "non pulite" o "rumorose" secondo diverse regole, e scrivere le parole "pulite" rimanenti in un file separato.

## Funzionamento

Lo script opera nel seguente modo:

1.  **Configurazione Encoding:** Imposta l'encoding `ansi` per lo standard input (anche se non sembra essere utilizzato direttamente) e utilizza `ansi` per tutte le operazioni di lettura/scrittura file.
2.  **Lettura Input:** Legge **tutte** le righe dal file hardcoded `..\words+wordCounts+docCounts_V1.txt` (nota il percorso relativo `..\` che implica che lo script debba essere eseguito da una sottodirectory rispetto a dove si trova il file di input) e le carica in memoria.
3.  **Apertura File Output:** Apre diversi file di output in modalità scrittura (`w`) con encoding `ansi` nella directory corrente:
    * `ElencoParolePulite.txt`: Conterrà le righe che superano tutti i controlli.
    * Vari file `debug_*.txt`: Ognuno conterrà le righe che *non* hanno superato uno specifico controllo.
4.  **Controllo Righe (`wordcheck`):** Itera su ogni riga letta dall'input e la passa alla funzione `wordcheck`. Questa funzione applica una serie di controlli sequenziali. **Importante:** Non appena una riga corrisponde a una regola di "non pulito", viene scritta nel relativo file `debug_*.txt` e l'elaborazione per quella riga si interrompe (non vengono controllate le regole successive).
5.  **Scrittura Output Pulito:** Se una riga supera *tutti* i controlli, viene scritta in `ElencoParolePulite.txt`.

### Regole di Filtraggio e File di Debug Corrispondenti

Le righe vengono scartate e smistate nei seguenti file `debug_*.txt` in base alla *prima* regola che attivano:

* **`debug_5char.txt`**: Righe in cui la "parola" iniziale ha da 1 a 4 caratteri (pattern: `\b.{1,4}\s\d+\s\d+\b`).
* **`debug_solonum.txt`**:
    * Righe in cui la "parola" iniziale è composta solo da numeri (pattern: `\b\d+\s\d+\s\d+\b`).
    * Righe in cui la "parola" iniziale è composta da numeri e un singolo simbolo qualsiasi (pattern: `\b(\d+.\d+|\d+.|.\d+)\s\d+\s\d+\b`).
* **`debug_composte.txt`**: Righe contenenti sequenze alternate di numeri e lettere ripetute almeno due volte (es. `abc123abc123`, pattern: `\b.*([0-9]+[a-z]+|[a-z]+[0-9]+){2,}.*\s\d+\s\d+\b`).
* **`debug_consonanti.txt`**: Righe contenenti 5 o più "non vocali" (escluse anche cifre e simboli \W) consecutive (pattern: `.*[^aeiou\d\W]{5,}.*`). Nota: case-sensitive (distingue maiuscole/minuscole).
* **`debug_vocali.txt`**: Righe contenenti 4 o più vocali ('a', 'e', 'i', 'o', 'u') consecutive (pattern: `.*[aeiou]{4,}.*`). Nota: case-sensitive.
* **`debug_5cifre.txt`**: Righe contenenti 5 o più cifre numeriche consecutive (pattern: `.*[\d]{5,}.*\s\d+\s\d+\b`).
* **`debug_symbol.txt`**: Righe contenenti caratteri che non sono né cifre, né spazi, né lettere minuscole dell'alfabeto inglese, né trattino (`-`), né underscore (`_`), né le vocali accentate `àèéìòù`. Il controllo viene fatto carattere per carattere.
* **`debug.txt`**: (File generico per altri pattern considerati "rumorosi")
    * Righe in cui la "parola" iniziale è composta da numeri e due simboli qualsiasi (pattern: `\b(\d+.{2}\d+|\d+.{2}|.{2}\d+)\s\d+\s\d+\b`).
    * Righe in cui la "parola" iniziale mescola caratteri alfanumerici e almeno un numero (pattern: `\b(\w+\d|\d\w+|\w+\d\w+)\s\d+\s\d+\b`).

## Input

* **File:** Si aspetta un file chiamato `words+wordCounts+docCounts_V1.txt` situato nella **directory padre** rispetto a quella in cui viene eseguito lo script.
* **Formato:** Presumibilmente una riga per parola, nel formato `parola conteggio1 conteggio2`.
* **Encoding:** Il file **deve** essere salvato con encoding `ansi` (tipicamente `cp1252` su sistemi Windows occidentali).

## Output

Lo script crea i seguenti file nella directory corrente, tutti con encoding `ansi`:

* `ElencoParolePulite.txt`: Contiene le righe che hanno superato tutti i filtri.
* `debug.txt`: Contiene righe scartate da regole specifiche (vedi sezione Regole).
* `debug_5char.txt`: Righe scartate perché la parola iniziale è troppo corta.
* `debug_composte.txt`: Righe scartate per pattern misti numeri/lettere ripetuti.
* `debug_solonum.txt`: Righe scartate perché la parola iniziale è numerica o quasi.
* `debug_consonanti.txt`: Righe scartate per lunghe sequenze di consonanti.
* `debug_vocali.txt`: Righe scartate per lunghe sequenze di vocali.
* `debug_5cifre.txt`: Righe scartate per lunghe sequenze di numeri.
* `debug_symbol.txt`: Righe scartate per la presenza di simboli non consentiti.

## Requisiti

* Python 3

## Utilizzo

1.  Assicurati di avere Python 3 installato.
2.  Salva lo script come `WordCleaner.py`.
3.  Assicurati che il file di input `words+wordCounts+docCounts_V1.txt` (con encoding `ansi`) esista nella directory **sopra** a quella dove metterai lo script.
    * Esempio Struttura:
        ```
        Progetto/
        ├── words+wordCounts+docCounts_V1.txt
        └── Script/
            └── WordCleaner.py  <-- Esegui da qui
        ```
4.  Apri un terminale o prompt dei comandi.
5.  Naviga nella directory dove hai salvato lo script (`Script/` nell'esempio).
6.  Esegui lo script con il comando:
    ```bash
    python WordCleaner.py
    ```
7.  Controlla i file `ElencoParolePulite.txt` e i vari `debug_*.txt` generati nella stessa directory dello script.

## Limitazioni Note

* **Percorsi Hardcoded:** I nomi dei file di input e output sono fissi nel codice. Il percorso di input è relativo (`..\`) e richiede una specifica struttura di directory.
* **Encoding Fisso:** L'uso di `ansi` può causare problemi su sistemi non-Windows o con file che usano codifiche diverse (UTF-8 è generalmente preferibile).
* **Caricamento in Memoria:** L'intero file di input viene letto in memoria (`.read().splitlines()`), il che potrebbe essere problematico per file di dimensioni molto grandi.
* **Gestione File:** Lo script non usa `with open(...)` e non chiude esplicitamente i file (`.close()`), affidandosi al garbage collector di Python, che non è la pratica più robusta.
* **Case-Sensitivity:** Alcuni controlli (es. vocali/consonanti) distinguono tra maiuscole e minuscole.

---

# 🧹 WordCleaner 🇬🇧

This Python script, named `WordCleaner`, is designed to read a text file containing a list of words (presumably in the format `word count1 count2`), apply a series of filters to identify and separate entries considered "unclean" or "noisy" according to various rules, and write the remaining "clean" entries to a separate file.

## How it Works

The script operates as follows:

1.  **Encoding Configuration:** It sets the `ansi` encoding for standard input (although it doesn't seem to be used directly) and utilizes `ansi` for all file reading/writing operations.
2.  **Input Reading:** It reads **all** lines from the hardcoded file `..\words+wordCounts+docCounts_V1.txt` (note the relative path `..\` which implies the script must be run from a subdirectory relative to the input file's location) and loads them into memory.
3.  **Output File Opening:** It opens several output files in write mode (`w`) with `ansi` encoding in the current directory:
    * `ElencoParolePulite.txt`: Will contain lines that pass all checks.
    * Various `debug_*.txt` files: Each will contain lines that *failed* a specific check.
4.  **Line Checking (`wordcheck`):** It iterates through each line read from the input and passes it to the `wordcheck` function. This function applies a series of sequential checks. **Important:** As soon as a line matches an "unclean" rule, it is written to the corresponding `debug_*.txt` file, and processing for that line stops (subsequent rules are not checked).
5.  **Clean Output Writing:** If a line passes *all* checks, it is written to `ElencoParolePulite.txt`.

### Filtering Rules and Corresponding Debug Files

Lines are discarded and sorted into the following `debug_*.txt` files based on the *first* rule they trigger:

* **`debug_5char.txt`**: Lines where the initial "word" has 1 to 4 characters (pattern: `\b.{1,4}\s\d+\s\d+\b`).
* **`debug_solonum.txt`**:
    * Lines where the initial "word" consists only of digits (pattern: `\b\d+\s\d+\s\d+\b`).
    * Lines where the initial "word" consists of digits and a single arbitrary symbol (pattern: `\b(\d+.\d+|\d+.|.\d+)\s\d+\s\d+\b`).
* **`debug_composte.txt`**: Lines containing alternating sequences of digits and letters repeated at least twice (e.g., `abc123abc123`, pattern: `\b.*([0-9]+[a-z]+|[a-z]+[0-9]+){2,}.*\s\d+\s\d+\b`).
* **`debug_consonanti.txt`**: Lines containing 5 or more consecutive "non-vowels" (also excluding digits and \W symbols) (pattern: `.*[^aeiou\d\W]{5,}.*`). Note: case-sensitive.
* **`debug_vocali.txt`**: Lines containing 4 or more consecutive vowels ('a', 'e', 'i', 'o', 'u') (pattern: `.*[aeiou]{4,}.*`). Note: case-sensitive.
* **`debug_5cifre.txt`**: Lines containing 5 or more consecutive digits (pattern: `.*[\d]{5,}.*\s\d+\s\d+\b`).
* **`debug_symbol.txt`**: Lines containing characters that are neither digits, nor whitespace, nor lowercase English letters, nor hyphen (`-`), nor underscore (`_`), nor the specific accented vowels `àèéìòù`. The check is performed character by character.
* **`debug.txt`**: (Generic file for other patterns considered "noisy")
    * Lines where the initial "word" consists of digits and two arbitrary symbols (pattern: `\b(\d+.{2}\d+|\d+.{2}|.{2}\d+)\s\d+\s\d+\b`).
    * Lines where the initial "word" mixes alphanumeric characters and at least one digit (pattern: `\b(\w+\d|\d\w+|\w+\d\w+)\s\d+\s\d+\b`).

## Input

* **File:** Expects a file named `words+wordCounts+docCounts_V1.txt` located in the **parent directory** relative to where the script is executed.
* **Format:** Presumably one line per word, in the format `word count1 count2`.
* **Encoding:** The file **must** be saved with `ansi` encoding (typically `cp1252` on Western Windows systems).

## Output

The script creates the following files in the current directory, all with `ansi` encoding:

* `ElencoParolePulite.txt`: Contains lines that passed all filters.
* `debug.txt`: Contains lines discarded by specific rules (see Rules section).
* `debug_5char.txt`: Lines discarded because the initial word is too short.
* `debug_composte.txt`: Lines discarded for repeated mixed number/letter patterns.
* `debug_solonum.txt`: Lines discarded because the initial word is numeric or nearly numeric.
* `debug_consonanti.txt`: Lines discarded for long sequences of consonants.
* `debug_vocali.txt`: Lines discarded for long sequences of vowels.
* `debug_5cifre.txt`: Lines discarded for long sequences of digits.
* `debug_symbol.txt`: Lines discarded due to the presence of disallowed symbols.

## Requirements

* Python 3

## Usage

1.  Ensure you have Python 3 installed.
2.  Save the script as `WordCleaner.py`.
3.  Ensure the input file `words+wordCounts+docCounts_V1.txt` (with `ansi` encoding) exists in the directory **above** the one where you place the script.
    * Example Structure:
        ```
        Project/
        ├── words+wordCounts+docCounts_V1.txt
        └── Script/
            └── WordCleaner.py  <-- Run from here
        ```
4.  Open a terminal or command prompt.
5.  Navigate to the directory where you saved the script (`Script/` in the example).
6.  Run the script using the command:
    ```bash
    python WordCleaner.py
    ```
7.  Check the generated `ElencoParolePulite.txt` and various `debug_*.txt` files in the same directory as the script.

## Known Limitations

* **Hardcoded Paths:** Input and output filenames are fixed in the code. The input path is relative (`..\`) and requires a specific directory structure.
* **Fixed Encoding:** The use of `ansi` can cause issues on non-Windows systems or with files using different encodings (UTF-8 is generally preferred).
* **Memory Usage:** The entire input file is read into memory (`.read().splitlines()`), which could be problematic for very large files.
* **File Handling:** The script does not use `with open(...)` and does not explicitly close files (`.close()`), relying on Python's garbage collector, which is not the most robust practice.
* **Case-Sensitivity:** Some checks (e.g., vowels/consonants) are case-sensitive.
