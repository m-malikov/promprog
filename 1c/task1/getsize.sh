#! /bin/bash
IFS=$'\n'
total_size=0;

ls_output=$(ls -la $1 | sed '1d')

for line in $ls_output; do
  filename=$(echo "$line" | awk '{print $9}');
  absolute_name="$1/$filename";
  file_size=$(echo "$line" | awk '{print $5}');
  if [[ "$filename" != "."  && "$filename" != ".." ]]
  then 
    if [ -f "$absolute_name" ]
    then
      let total_size=total_size+file_size;
    elif [ -d "$absolute_name" ]
    then
      subfolder_size=$(./$0 "$absolute_name");
      let total_size=total_size+subfolder_size;
    fi
  fi
done

echo $total_size;
