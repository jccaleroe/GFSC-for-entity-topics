#!/bin/bash
iconv -f UTF-8 -t ASCII//TRANSLIT "$1" > "$1".bak
mv "$1".bak "$1"
