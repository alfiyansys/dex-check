# DEX Check (Domain Expiration Checker)

Check domain (list) expiration date and send notification by Telegram.
## Compatibility
Developed using Python 3.10, you may also use docker and build the image with included Dockerfile.
## Installation
Create virtualenv in .venv

```
$ python -m venv venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
## Usage
### Configuration
Copy config.ini.example to config.ini and modify configuration items as in example file.
### Run
Run by:

```
$ ./run.sh
```

## Docker
Alternatively, you may use docker and build the image.

```
$ docker build -t dex-check .
$ docker run dex-check
```