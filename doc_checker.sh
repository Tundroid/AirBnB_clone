#!/usr/bin/env bash
#list contents of a directory ignoring characters
#before and including the first hyphen

list="console models.base_model"
for file in $list;
do
	python3 -c "print(__import__('$file').__doc__)"
done