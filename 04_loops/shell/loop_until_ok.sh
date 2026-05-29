#!/bin/sh

while true
do
    printf "yes と入力してください: "
    read answer

    if [ "$answer" = "yes" ]; then
        echo "OKです"
        break
    fi

    echo "入力が違います。もう一度入力してください。"
done

echo "処理を終了します"
