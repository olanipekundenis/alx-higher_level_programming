#!/bin/bash
# script that takes in a URL and displays all HTTP method
curl -Is "$1" | grep "Allow: " | cut -d ' ' -f 2-
