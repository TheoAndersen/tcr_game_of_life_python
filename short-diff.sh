#!/bin/sh
git diff --unified=0 --word-diff-regex=. --word-diff=porcelain | grep -Ev '^\+\+\+' | sed -n -e 's/^\+\(.*\)$/\1/p' | awk '{$1=$1};1' | tr '\n' ' ' | cut -c 1-50
