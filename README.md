
# Brute Force Login Script(--BRUTI5--)

This Python script performs a basic username-password brute force attack on a target URL's login page using a provided wordlist.

## Description

The script is designed to automate the process of attempting different username and password combinations from a wordlist against a specified target URL's login page. It uses the `requests` library to simulate login attempts and checks for successful login responses.

## Prerequisites

- Python 3.x
- `requests` library (Install using `pip install requests`)
- Display banner (Install using `pip install pyfiglet`)

## Usage

1. Clone the repository or download the Python script `bruti5.py`.
2. Run the script from the command line, passing the required arguments:
    ```bash
    python bruti5.py -t <target_url> -w <wordlist_file>
    ```
    - `-t <target_url>` or `--target <target_url>`: Specifies the target URL where the login form exists.
    - `-w <wordlist_file>` or `--wlist <wordlist_file>`: Specifies the file containing username:password pairs.
## Example 
```bash 
    username1 : password1
    username2 : password2
  ```

You can alter the below python script for data  values. In this part you take data from using inpect element or brupsuit.
chang user_name to your_target_user_name_field and password to your_target_user_password_field
## Example 
```bash 
data = {'user_name': user, 'user_pwd': password, 'login': 'Sign+In'}
  ```
## Command

```bash
python bruti5.py -t https://example.com/login -w wordlist.txt
```
## Authors

- [@ASIF](https://github.com/asif-cods)
