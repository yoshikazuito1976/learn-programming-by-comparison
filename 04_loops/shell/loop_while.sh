#!/bin/sh

count=1

while [ "$count" -le 5 ]
do
    echo "${count}回目の処理です"
    count=$((count + 1))
done
