for i in `seq 1 14`; do 
       fn=`printf step_%04d $i`; 
       read sent; echo $sent; 
       rec -r 16000 -e signed-integer -b 16 -c 1 wav/$fn.wav 2>/dev/null; 
done < step-corpus-14.txt