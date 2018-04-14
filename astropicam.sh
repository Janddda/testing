!#/bin/sh

cd /data/media/sda/
mkdir "$(date +"%d-%m-%Y")"
raspistill -o "$(date +"%d-%m-%Y")"/sky_%04d.jpg -t 500000000 -tl 0 -ss 9900000 -ISO 800 -$

