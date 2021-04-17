#!/bin/sh

folder=`ls celebrity_face`
for name in $folder ; 
do
    list_of_pic=`ls celebrity_face/${name}`
    counter=1
    for pic in $list_of_pic:
    do
        cp celebrity_face/$name/$pic face_data/${name}_${counter}.jpeg
        # echo ${name}_${counter}
        # echo celebrity_face/$name/$pic
        counter=$((counter+1))
    done
done
