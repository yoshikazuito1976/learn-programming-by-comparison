#!/bin/sh
# Shell: 条件分岐の基本

score=75

if [ "$score" -ge 60 ]; then
  echo "合格です"
else
  echo "不合格です"
fi