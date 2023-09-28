#!/bin/bash 
# script sends request passed as an argument to a URL,
# and displays only the status code of the response.

curl -s -L -X HEAD -w "%{http_code}" "$1"
