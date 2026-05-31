#!/bin/sh
# Shell: 年齢による条件分岐

age=7

if [ "$age" -ge 18 ]; then
  echo "成人です"
else
  echo "未成年です"
fi
