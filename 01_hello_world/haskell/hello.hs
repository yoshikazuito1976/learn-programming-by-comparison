main :: IO ()
main = do
    putStrLn "Hello, Haskell!"

    let name = "Yoshikazu"
    putStrLn ("Hello, " ++ name ++ "!")

    let language = "Haskell"
    putStrLn ("This language is " ++ language ++ ".")
