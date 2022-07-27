#!/usr/bin/env bash

function main {
    if [ -z "$1" ]; then 
        echo "Please specify a layout file to compile."
    else 
        cat lib/begin.html.part > page.html
        lessc "$1" >> page.html
        cat lib/end.html.part >> page.html
    fi
}
main "$@"