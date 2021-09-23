// Complete the rotLeft function below.
function rotLeft(a, d) {
    let i=1,a2,a3;
 while(i<=d){
   a3 = a.slice(d)
   a2 = a.slice(0,d);
   i++;
 }
 return [...a3,...a2];

}