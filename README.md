# Project AutoVPN

## Summary

Simple script to automate VPN connections via CLI.
The idea is pretty simple: most VPN CLIs prompt user for username, password (and sometimes OTP codes). Instead of calling the CLI, you can call this script that automaticaaly awaits for the prompts and inputs data stored via environment variables (or a `.env` file).


## Installation

Install pipenv: `pip3 install pipenv`

Install python virtual environment and projects dependencies: `make install`

Set the environment variables listed in `src/.env.example` according to your needs. Alternatively, you can create a `.env` file in the same location.

**DISCLAIMER**: it's NOT SAFE to store passwords and secrets in plain text files, USE AT YOU OWN RISK!

Call the script using `make run`