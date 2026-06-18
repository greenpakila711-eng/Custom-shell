# 🐚 Mini Shell (Python)

Ekta lightweight Unix-style shell, Python diye banano — `bash`-er moto basic kaj korte pare: builtin commands, external programs run kora, ar directory navigation handle kora.

## ✨ Features

- **Builtin Commands**
  - `echo` — arguments print kore
  - `pwd` — current working directory dekhay
  - `cd` — directory change kore (relative path, absolute path, ar `~` home directory support kore)
  - `type` — bole kono command builtin naki external executable, ar thakle path o dekhay
  - `exit` — shell theke bairhoye jay

- **External Command Execution**
  - `$PATH`-e thaka kono executable (jemon `ls`, `cat`, `grep`) shorashori run kora jay

- **Output Redirection**
  - `>` ar `1>` operator diye command-er output file-e likha jay

## 🚀 Kibhabe Run Korbe

```bash
python3 shell.py
```

Shell start hole `$` prompt dekha jabe — shekhane command type korle execute hobe:

```
$ pwd
/home/user
$ cd /tmp
$ echo Hello World
Hello World
$ type cd
cd is a shell builtin
$ ls
$ exit
```

## 🧠 Kibhabe Kaj Kore (Internals)

- `shlex.split()` use kore prompt-e likha command line-take properly tokenize kora hoy (quotes handle kore).
- `get_absolute_path()` function-e regex use kore check kora hoy path-ta valid directory name pattern follow kore kina, tarpor `os.path.abspath()` diye absolute path resolve kora hoy.
- `get_executable_path()` `$PATH` environment variable-er shob directory loop kore dekhe kono matching executable file ache kina.
- Builtin na hole, command-take `subprocess.run()` diye child process e execute kora hoy.

## ⚠️ Known Limitations

Ei version-ta ekta learning/practice project — kichu jinish ekhono perfect na:

- **Redirection logic-e bug ache**: `>` thakle pura line `os.system()`-ke diye dewa hoy, mane custom builtin-gulo (jemon `cd`, `echo`) shei somoy actual shell-er nijer logic use na kore OS-er default behavior follow kore.
- **`cd` korar pore external command-gulo purono directory-tei thake** — karon `current_directory` variable update hoy, kintu Python process-er actual working directory (`os.chdir()`) change hoy na.
- Argument na diye `type` ba `cd` likhle crash korte pare (`IndexError`).
- Quote-er bhetorer `>` character thakleo (jemon `echo "a > b"`) bhul kore redirection mone kore felte pare.

## 🛠️ TODO / Future Improvements

- [ ] Token-level redirection parsing (`>`, `>>`, `2>`, `2>>` properly support kora)
- [ ] `os.chdir()` use kore actual process directory sync rakha
- [ ] Pipe (`|`) support add kora
- [ ] Missing argument-er jonno graceful error handling
- [ ] Command history (up/down arrow)

## 📂 File Structure

```
shell.py    # Main shell implementation
README.md   # Ei file
```

## 📜 License

Free to use, modify, ar learning-er jonno share korte paren.
