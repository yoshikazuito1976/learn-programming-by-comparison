#!/bin/sh

printf "名前を入力してください: "
read name

echo "こんにちは、${name}さん"
printf "こんにちは、%sさん\n" "$name"