#!/bin/sh
SHORTDIFF=$(./short-diff.sh)
echo $SHORTDIFF && git add . && git commit -am "TCR $SHORTDIFF" && ./notify_ok.sh "$SHORTDIFF"
