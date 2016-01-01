grep 'ContentPlaceHolder1_hdnAuthCode' auth.html |grep -P -o 'value="\w+'|sed 's/value=\"//'
