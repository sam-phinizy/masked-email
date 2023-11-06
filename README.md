# Masked Email

A simple wrapper around [jmapc](https://pypi.org/project/jmapc/) to provide a 'cli' command to generate a masked email
for Fastmail.

## To install

```bash
pipx install git+https://github.com/sam-phinizy/masked-email
```

## To use

### Basic usage
```bash
masked-email
```
Returns a masked email address for Fastmail.

### With description
```bash
masked-email --description "My new masked email"
```

### Copy to clipboard
```bash
masked-email --copy
```
### With 1password

You can inject your `JMAP_API_KEY` and `JMAP_HOST` using 1password by setting the following environment variables:

```bash
export JMAP_API_KEY="op://VAULT/SECRET_REFERNCE/api_key
export JMAP_HOST="op://VAULT/SECRET_REFERNCE/hostname"
```
and then running the command like this:

```bash
op-run -- masked-email
```



## To develop

```bash
git clone https://github.com/sam-phinizy/masked-email
cd masked-email
poetry install
```
