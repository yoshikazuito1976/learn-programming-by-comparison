#!/bin/bash

echo "=== Environment Check ==="
check_command() {
    local name="$1"
    local command="$2"
    local version_option="${3:---version}"

    echo -n "$name: "

    if command -v "$command" > /dev/null 2>&1; then
        "$command" $version_option | head -n 1
    else
        echo "Not installed"
    fi
}




check_command "Python" "python3"
check_command "Python 3.12" "python3.12"
check_command "Java" "java"
check_command "Javac" "javac"
check_command "GCC" "gcc"
check_command "G++" "g++"
check_command "Rust" "rustc"
check_command "Cargo" "cargo"
check_command "Go" "go" "version"
check_command "Lua" "lua" "-v"
check_command "GHC" "ghc" "--version"
check_command "RunGHC" "runghc" "--version"
check_command "GHCi" "ghci" "--version"
check_command "Cabal" "cabal" "--version"
check_command "GHCup" "ghcup" "--version"