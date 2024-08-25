# Assignment 2

## Question 1

How do you display the contents of a file named `example.txt` using `cat`?

To display the contents of the file named `example.txt` in the terminal using `cat` we use the command:

```bash
cat example.txt
```

## Question 2

How do you display the contents of a file named `example.txt` one page at a time using `more`?

To display the contents of a file named `example.txt` one page at a time, we use `more` command. The command is:

```bash
more example.txt
```

## Question 3

While viewing a file with `more`, how do you advance to the next line and how do you advance by one page?

After using `more` command, to advance to the next line, we press **Enter** button. To advance by one page, we press **space bar** button.

## Question 4

How do you search for the word "error" in a file named `logfile.txt`?

To search for the word "error" in `logfile.txt`, we use the command

```bash
grep -w error logfile.txt
```

or

```bash
egrep -w error logfile.txt
```

in both commands the flag `-w` makes both the commands search for the word error in `logfile.txt`

## Question 5

How do you display the first 10 lines of a file named `example.txt`?

To display the first ten lines of the file `example.txt` the command is:

```bash

head example.txt
```

## Question 6

How do you display the last 10 lines of a file named `example.txt`?

To display the last ten lines of the file `example.txt` the command is:

```bash

tail example.txt
```

## Question 7

How do you print the text "Hello, World!" to the terminal?

To print "Hello, World!" in the terminal, we type the command:

```bash
echo "Hello, World!"
```

## Question 8

How do you search for the word "error" in a file named `logfile.txt` using `Select-String` in PowerShell?

To search for the word in "error" in the `logfile.txt` we type:

```powershell
Select-String -Pattern "error" -Path logfile.txt
```

## Question 9

How do you search for lines containing the word "success" in all `.log` files in the current directory?

To search for the lines containing the word "success" in all `.log` files in the current directory.

```bash
grep -w success *.log
```

or

```bash
egrep -w success *.log
```

both `grep` and `egrep` with the flag `-w` searches for the word success in the all the `.log`.
Here `*.log` would mean all the files in the current directory.
