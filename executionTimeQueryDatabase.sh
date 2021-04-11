#!/bin/sh
py query_db.py $(cat uniqueKeys.txt)
read -p "Press enter to continue"