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

## To develop

```bash
git clone https://github.com/sam-phinizy/masked-email
cd masked-email
poetry install
```
