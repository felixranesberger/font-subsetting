# Font Subsetter
Creates subsets of fonts to increase pagespeed score.

The script is from this [blogpost](https://www.naiyerasif.com/post/2024/06/27/how-i-subset-fonts-for-my-site)

## Build docker image
```bash
docker build -t fontoptim .
```

## Run script

```bash
docker run --rm -v .:/app fontoptim
```
