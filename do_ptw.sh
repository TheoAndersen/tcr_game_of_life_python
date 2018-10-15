#!/bin/sh
ptw --onpass ./success.sh --onfail "git reset --hard && git clean -fd && ./notify_fail.sh"

