echo "usage: bash main-loop.sh count-start length height"
c=$1
l=$2
h=$3
while true
do
  python2 main.py $c-$l-$h $l $h
  c=$((c+1))
done
