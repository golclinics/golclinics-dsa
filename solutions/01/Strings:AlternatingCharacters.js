// Complete the alternatingCharacters function below.
function alternatingCharacters(s) {
    let curr=s[0],c=0;
    for(let i=1;i<s.length;i++){
        if(s[i]===curr){
            c++;
        }else{
            curr=s[i];
        }
    }
  return c;
}