#!/bin/bash
#this takes a url, sendas a request to the url and displays the qsize of the body of response
curl -sI "$1" | grep Content-Length | cut -d " " -f2