#!/bin/sh

printf "年齢を入力してください: "
read age

case "$age" in
    ''|*[!0-9]*)
        echo "半角数字で入力してください"
        exit 1
        ;;
esac

next_age=$((age + 1))

printf "来年は%s歳です\n" "$next_age"
