#!/bin/bash
# Send a GET request to the URL and display the body of a 200 status code response
curl -s -o /dev/stdout -w "%{http_code}" "$1"
