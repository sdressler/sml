#!/bin/bash

result=`./sml.py $@`

if [[ "$result" == setvar* ]] then
	eval ${result/setvar /}
else 
	echo $result
fi

