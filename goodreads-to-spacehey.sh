#!/usr/bin/env bash


function main {
    local url="${1}"
    local book_html="book.html"

    if [ -n $url ]; then 
        
        local base_name="$(basename $url)"
        local id="$(echo ${base_name} | grep -Eo '^[0-9]+')"

        # echo "$id"

        curl -sSL "${url}" -o "${book_html}"
        local title_tag="$(cat ./${book_html} | grep -E title | head -n1)"
        # echo "$title_tag"
        local title_and_by_line="$(echo ${title_tag} | sed -E 's/<\/?title>//g')"
        # echo "$title_and_by_line"
        local title="$(echo ${title_and_by_line} | grep -Eo '^.*by' | sed 's/ by$//')"
        # echo "$title"
        local author="$(echo ${title_and_by_line} | grep -Eo 'by.*$' | sed 's/^by //')"
        # echo "$author"

        local image_tag="$(cat ./${book_html} | grep -E .*alt=\"${id}.*)"
        # echo "$image_tag"
        local image_url="$(echo ${image_tag} | grep -Eo [A-Za-z0-9\/:\.\_\-]+\.jpg)"
        # echo "$image_url"


        echo "<!--"
        echo "${title}"
        echo "${author}"
        echo "-->"
        echo "<a href=\"${url}\">"
        echo "<img height=\"150\" src=\"${image_url}\" />"
        echo "</a>"



    else
        echo "No URL provided."
    fi 


}
main "$@"
