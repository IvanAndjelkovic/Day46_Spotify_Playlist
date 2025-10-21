#!/bin/sh
echo "What food do you choose: "
read FOOD

if [ "$FOOD" = "Apple" ];then
    echo "Eat yougurt with your Apple."
elif [ "$FOOD" = "Milk" ];then
    echo "Eat cereal with your Milk."
else
    echo "Eat your $FOOD by itself."

fi