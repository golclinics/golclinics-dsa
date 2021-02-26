function evaluate(S){
    let stuff = S.split(' '),res=Number(stuff[0]),operator='';
    for(i=0;i<stuff.length;i++){
      if(isNaN(stuff[i])){
         if(stuff[i]==='+')
         res += Number(stuff[i+1]);
        if(stuff[i]==='-')
         res -= Number(stuff[i+1]);
      }
    }
    return res;
 }
 console.log(evaluate("1 + 1 - 1 + 10"));