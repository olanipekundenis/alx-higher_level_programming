#!/bin/bash
# script sends a JSON POST request to a URL passed it as
# the first argument, then displays the body of the response.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
