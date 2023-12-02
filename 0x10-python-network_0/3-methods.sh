#!/bin/bash
# Display all HTTP methods the server will accept for the specified URL
curl -s -I -X OPTIONS "$1" | grep -i 'Allow' | cut -d ' ' -f 2-
