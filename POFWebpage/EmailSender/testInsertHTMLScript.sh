#! /usr/bin/bash

read -p "Enter file that contains the formatted email: " HTMLFILE

while true
    do 
        if [ -f "$HTMLFILE" ]
        then
            break
        else
            read -p "Enter file that contains the formatted email: " HTMLFILE
fi
done

sed -i '/</d' EmailListSender.py
sed -i -e '/    msg.add_alternative("""/r '"$HTMLFILE"'' EmailListSender.py

python EmailListSender.py