#!/bin/bash

# check_time_web.sh Check load time web for nagios. By Pablo Serrano
# This plugin check if website load is more that normal parameters. You can change variables how website, header, useragent, ect 
#  
#  
#  Version 1.0

website='google.es' # Put you web if you want track 
header='x-up-calling-line-id: NAGIOS' # Put your header as you want to use
useragent='Mozilla/5.0 (Linux; U; Android 2.1-update1; es-es; GT-I9000 Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 UP.Link/6.3.1.15.0' #put you user-agent as you want to use. 
timewar='2' # Time limit to warning 
timecri='3' # Time limit to critical  
enter=`curl -o /dev/null -s --header "$header"  --user-agent "$useragent" -w %{time_total} $website` # you can remove o add new options for connect on your web. See "man curl" for add more optinos

val=`echo $enter | awk 'BEGIN { FS = "," } ; { print $1 }' `

if [ $(echo "$val >= $timewar"|bc) -eq 0  ] ; then
        echo "OK - Load time $enter seconds" ; exit 0
else

         if [ $(echo "$val >= $timecri"|bc) -eq 0  ] ; then

                echo "Warning - There is a load problem " ; exit 1
        else
                echo "Critical - There is a load problem $enter seconds " ; exit 2
        fi
fi
