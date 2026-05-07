# Install Guide for AlmaLinux

This document describes how to set up the development environment for this repository on AlmaLinux.

## Update packages

```bash
sudo dnf update -y

```

sudo dnf groupinstall "Development Tools" -y

Install development tools
sudo dnf groupinstall "Development Tools" -y

This installs tools such as gcc, g++, make, and other build tools.

Install Git
sudo dnf install git -y

Check:

git --version
Python

AlmaLinux may already include system Python as python3.

Check:

python3 --version
Install Python 3.12

Install Python 3.12 separately without replacing the system Python.

sudo dnf install python3.12 -y

Check:

python3.12 --version
Install pip for Python 3.12
sudo dnf install python3.12-pip -y

Check:

python3.12 -m pip --version
Install Java

Install OpenJDK 21.

sudo dnf install java-21-openjdk java-21-openjdk-devel -y

Check:

java --version
javac --version
C and C++

C and C++ compilers are included in Development Tools.

Check:

gcc --version
g++ --version
Install Rust

Install Rust using rustup.

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

After installation, load the Rust environment:

source "$HOME/.cargo/env"

Check:

rustc --version
cargo --version
Check all tools

Run the environment check script:

./scripts/check_environment.sh

Expected tools:

Python
Python 3.12
Java
Javac
GCC
G++
Rust
Cargo
