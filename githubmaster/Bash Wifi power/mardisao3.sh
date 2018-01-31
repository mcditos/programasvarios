#!/bin/bash

## print header lines


while IFS= read -r line; do

 
    [[ "$line" =~ Quality ]] && { 
     
        lvl=${line##*evel=}
        lvl=${lvl%% *}
    }
    [[ "$line" =~ Encrypt ]] && enc=${line##*key:}
    [[ "$line" =~ ESSID ]] && {
        essid=${line##*ID:}
        echo  "$essid"  # output after ESSID
        echo "$lvl"
    }

done
