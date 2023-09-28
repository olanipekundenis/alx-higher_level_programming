#!/bin/bash 
# script sends request passed as an argument to a URL,
# and displays only the status code of the response.
curl -sI -w '%{response_code}' "$1" -o /dev/null
