#!/bin/bash
# script takes in a URL, sends it a request, 
# then displays size of the body of the response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
