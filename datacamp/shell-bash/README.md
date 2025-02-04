# Introduction to Shell

> **Note: This is the first course. The second course is "Introduction to Bash Scripting", see [BASH-SCRIPTING.md](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/shell-bash/BASH-SCRIPTING.md)**

E.g in the directory there are 4 files in folder `seasonal`: `summer.csv`, `spring.csv`, `autumn.csv`, `winter.csv`

## Wildcards (`*`, `[]`, `{}`, `?`)

`cut -d , -f 1 seasonal/s*.csv`

* select the first column with delimiter "," (comma-separated) of all the files spring.csv and summer.csv, files beginning with letter "s" (but not autumn.csv and winter.csv)

<div>
<img src="https://user-images.githubusercontent.com/51282928/82152501-d46cd600-988b-11ea-8a31-ba3884d53957.png" width="700"/>
</div>

## Implementations of pipeline

Piping is putting two or more commands in a single line

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 10`

* select the first column from the summer data
* remove the header line containing the word "Tooth"
* select the first 10 lines of actual data.

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | sort -r`

* select the first column from the summer data
* remove the header line containing the word "Tooth"
* sort in reverse order

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | sort | uniq -c`

* get the second column from seasonal/winter.csv,
* remove the word "Tooth" from the output so that only tooth names are displayed,
* sort the output so that all occurrences of a particular tooth name are adjacent; and
* display each tooth name once along with a count of how often it occurs.

<div>
<img src="https://user-images.githubusercontent.com/51282928/82152536-17c74480-988c-11ea-8c2a-cad98c85ddd5.png" width="500"/>
</div>

`grep "2017-07" seasonal/spring.csv | wc -l`

* search "2017-07" in spring.csv
* count how many "2017-07" in lines (word count)

## Wrapping Up pipelines

1. Use wc with appropriate parameters to list the number of lines in all of the seasonal data files. (Use a wildcard for the filenames instead of typing them all in by hand.)

Script: `wc -l seasonal/*.csv`

2. Add another command to the previous one using a pipe to remove the line containing the word "total".

Script: `wc -l seasonal/*.csv | grep -v total`

3. Add two more stages to the pipeline that use sort -n and head -n 1 to find the file containing the fewest lines.

Script: `wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1`


## Batch Processing

Store a variable and print it:
* Declare a variable: `colors`: `red, green, blue`
* Print the variable: `echo $colors`

For loop (to print all `.csv` files in the folder `seasonal`)

Script 1: `for filename in seasonal/*.csv; do echo $filename; done`

Script 2:<br>
```
seasons = seasonal/*.csv
for filename in $seasons; do echo $filename; done
```


Write a loop that prints the last entry from July 2017 (2017-07) in every seasonal file.

Script: `for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done`

## Bash Scripting

* Open a GNU Nano text editor and create a bash file: `nano file.sh`
* Enter the script there, then save and exit (use keyboard keys below)
* To run the shell file: `bash file.sh`
* To redirect the output of that running that shell file *to* another new created file: `bash file.sh > filenew.sh`. 

> Important: Redirect `>` to an output file is *different* from Piping `|`

* The use of `$@`

<div>
<img src="https://user-images.githubusercontent.com/51282928/82154985-d8a0ef80-989b-11ea-8edd-fde2e5aea76d.png" width="700"/>
</div>

* The use of `$1`, `$2`, and so on to symbolize the order of `$@`

<div>
<img src="https://user-images.githubusercontent.com/51282928/82155011-20277b80-989c-11ea-93a5-f00c28622209.png" width="700"/>
</div>

## GNU Nano for Text Editor Keyboard Keys

* `CTRL K` to copy
* `CTRL P` to paste, do twice
* `CTRL O` to save, then click `ENTER`
* `CTRL X` to exit

## And finally, do `CTRL C` to terminate a running program
