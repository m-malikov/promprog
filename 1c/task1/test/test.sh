#! /bin/bash

#git clone https://github.com/vuejs/vuex
computed_size=$(./../getsize.sh vuex)
actual_size=$(du -sb vuex | awk '{print $1}')
echo -e "Computed size:\t" $computed_size
echo -e "Actual size:\t" $actual_size
#rm -rf vuex
