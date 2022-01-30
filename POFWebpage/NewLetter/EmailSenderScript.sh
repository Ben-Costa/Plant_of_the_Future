#! /usr/bin/bash

read -p "Enter the HTML email file to be used: " HTMLFILE

while true
    do 
        if [ -f "$HTMLFILE" ]
        then
            break
        else
            read -p "Enter the HTML email file to be used: " HTMLFILE
        fi
done


sed -i '/</d' EmailListSender.py
#sed -i '/    """, subtype = 'html')/ a\\'  EmailListSender.py
sed -i -e '/    """, subtype =/i \\' EmailListSender.py
sed -i -e '/    msg.add_alternative("""/r '"$HTMLFILE"'' EmailListSender.py

python EmailListSender.py
