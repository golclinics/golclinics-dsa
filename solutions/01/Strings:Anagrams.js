// Complete the makeAnagram function below.
function makeAnagram(a, b) {
    let en=0;a=a.split('');b=b.split('');
    for(let i=0;i<a.length;i++){
      let x = b.indexOf(a[i]);
       if(x!==-1){
         en++;
         b.splice(x,1);
       }
    }
    return a.length - en + b.length;
}
