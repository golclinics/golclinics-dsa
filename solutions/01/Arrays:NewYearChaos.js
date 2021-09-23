// Complete the minimumBribes function below.
function minimumBribes(q) {
    let min=0,swapped;
    do{
      let i=0;swapped=false;
      while(i<q.length){
      let temp,diff = q[i] - (i+1);
      if(diff > 2){
        console.log('Too chaotic');
        return;
      }
      if(q[i]>q[i+1]){
        temp=q[i+1];q[i+1]=q[i];q[i]=temp;
        swapped=true;min++
      }
      i++;
    }
  }while(swapped);

  console.log(min);
}
