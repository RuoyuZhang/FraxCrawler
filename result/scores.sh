for sample in `ls *.html`;do
    name=$(echo $sample|sed 's/\.html//')
    #Major osteoporotic
    ost=$(grep 'ContentPlaceHolder1_lbrs1' $sample|grep -o -P '>\w+\.?\w+<'|sed 's/[><]//g')
    #Hip fracture
    hip=$(grep 'ContentPlaceHolder1_lbrs2' $sample|grep -o -P '>\w+\.?\w+<'|sed 's/[><]//g')

    echo "$name, $ost, $hip" >> temp
done

echo '2.0132, N/A, N/A' >>temp
echo '4.1530, N/A, N/A' >>temp

sort -n -k1 temp >result
rm temp
