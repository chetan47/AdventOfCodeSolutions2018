#!/bin/bash

let "a = `cat input.txt | xargs`"
echo $a
