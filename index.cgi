#!/bin/bash

SEC=`date +%S`
NUM=`expr $SEC % 7 + 1`

echo Content-type: text/html
echo
echo
cat << EOF
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<title>Stop SOAP!</title>
			<style type="text/css">
				body {
					background: #000000;
					color: #00ff00;
				}
				#banner {
					background: #ff0000;
					color: #fff;
					text-align: center;
					width: 100%;
					position: fixed;
					font-size: 80px;
					margin-top: 40%;
					font-weight: bold;
				}
			</style>
		</head>
		<body>
			<div id="banner">STOP SOAP</div>
			
EOF
echo "<pre>"
cat /home/josh/www/stopsoap/wsdl/$NUM | sed "s/</\&lt;/g" | sed "s/>/\&gt;/g"
echo "</pre></body></html>"
