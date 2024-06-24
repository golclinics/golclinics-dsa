/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    s=s.split('')
    let stk = [];
  
    for(i=0,l=s.length;i<l;i++){
        let l2 = stk.length;
        if(s[i]==='(' || s[i]==='{' || s[i]==='[' )
            stk.push(s[i])
      
        if(s[i]===')')
            if(stk[l2-1]==='(')
                stk.pop()
            else
                return false;
        if(s[i]==='}')
            if(stk[l2-1]==='{')
                stk.pop()
            else
                return false;
        if(s[i]===']')
            if(stk[l2-1]==='[')
                stk.pop()
            else
                return false;
  }
    
    return stk.length===0?true:false;   
};
