#!/usr/bin/env bash

function main {
    local layout_name="${1}"

    if [ -z "${layout_name}" ]; then 
        echo "Please specify a layout to compile."
    else 
        cd "${layout_name}"
        mkdir -p "gen"

        local output_name="gen/${layout_name}.html"

        echo "" > $output_name

        while IFS="" read -r line || [ -n "$line" ]
        do
            # echo $line
            placeholder="$(echo $line | grep -Eo @@[a-z]+)"
            if [ -n "$placeholder" ]; then 
                case "$placeholder" in 
                    "@@style")
                        style_output="gen/style.css"
                        lessc "style.less" $style_output
                        echo "<style>$(cat $style_output)</style>" >> $output_name
                    ;;
                    *)
                        if [ -d "${placeholder}" ]; then 
                            placeholder_output="gen/${placeholder}.html"
                            jinja -d "${placeholder}/data.yaml" -f yaml "${placeholder}/template.j2" > $placeholder_output
                            cat $placeholder_output >> $output_name
                        fi
                    ;;
                esac
            else
                echo "$line" >> $output_name
            fi
        done < ../lib/page.html


    fi
}
main "$@"