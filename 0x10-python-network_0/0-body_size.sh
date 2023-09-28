#!/bin/bash
# script takes in a URL, sends it a request, 
# then displays size of the body of the response.
curl -s "$1" | wc -c
