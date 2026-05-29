#!/bin/sh

printf "年齢を入力してください: "
read age

next_age=$((age + 1))

printf "来年は%s歳です\n" "$next_age"
