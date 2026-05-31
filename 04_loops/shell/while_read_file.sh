#!/bin/sh
# Shell: while と read でファイルを1行ずつ読む

while read line
do
  echo "読み取った行: $line"
done < file.txt
