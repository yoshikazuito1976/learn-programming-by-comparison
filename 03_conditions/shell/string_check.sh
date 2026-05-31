#!/bin/sh
# Shell: 文字列の条件分岐

name="taro"

if [ "$name" = "taro" ]; then
  echo "こんにちは、taroさん"
else
  echo "別の名前です"
fi
