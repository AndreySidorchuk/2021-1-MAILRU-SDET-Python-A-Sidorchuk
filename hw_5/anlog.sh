#!/usr/bin/env bash
if [ $# -eq 0 ]; then
  echo "No arguments: filename required"
  exit
fi
file_log=($1)
count_req_all=$(cat $file_log |grep ' - - '| wc -l)
echo -e "\nCount of requests:$count_req_all\n" >> report

count_req_of_type=$(cat $file_log | cut -f6 -d" "| cut -c2-|grep -e "^[[:upper:]]"| sort |uniq  -c)
echo -e "Request of type:\n$count_req_of_type\n" >> report 

top_5_req_4xx=$(  cat $file | awk '{print $1, $7, $9, $10}' | grep -w "4[0-2][0-9]" | uniq | sort -k10 -nr | head -5)
echo -e "Top 5 req with error 4xx:\n$top_5_req_4xx\n" >> report

top_5_req_5xx=$(awk '($9 ~ /^5/)' $file_log | awk '{print $1,$7,$9,$10}' | sort | uniq -c | sort -r -k3 |tr -s " "| cut -f3,4 -d" "|head -5)
echo -e "Top 5 req with errors 5xx:\n$top_5_req_5xx\n" >> report
