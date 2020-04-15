stress_file=$1
count=0

while true
do
	mysql -u root pdi < $stress_file
	count=$((count+1))
	echo -n "Count = " 
	echo $count
done
