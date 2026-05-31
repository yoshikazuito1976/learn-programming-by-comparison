#!/bin/sh
# Shell: 入力と条件分岐

printf "名前を入力してください: "
read name

if [ "$name" = "taro" ]; then
  echo "こんにちは、taroさん"
else
  echo "こんにちは、$name さん"
fi
