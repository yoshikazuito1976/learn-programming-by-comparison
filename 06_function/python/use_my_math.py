# use_my_math.py
import my_math #同じディレクトリ内にあるmy_math.pyをインポートする

print(my_math.add(1, 2))
print(my_math.sub(5, 3))
print(my_math.mul(4, 6))
print(my_math.div(8, 2))

'''
This is a simple example of using a custom math module.
import は「ファイル名を書けば何でも読める」わけではありません。
Python は、決められた場所からモジュールを探します。

pip で入れた外部モジュールは、Python が探せる場所に入るので import しやすいです。
しかし、自分で作った .py ファイルは、置き場所によって import できたりできなかったりします。

'''

