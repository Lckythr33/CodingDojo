function makeArr(){
    var numArr=[];
    for(var i=1;i<=255;i++){
        numArr.push(i);
    }
    return numArr;
}   

function sumEvenArr(){
var sum=0;
    for(var i=1;i<=1000;i++){
     if(i % 2 === 0){
        sum += i;
      }
    }
    console.log(sum);
    return sum;
}

function sumOddArr(){
var sum=0;
    for(i=1;i<=5000;i+=2)
    {
      sum+=i;
    }
    return sum;
}

function sumArr(arr){
    var sum = 0;
    for(var i=0;i<arr.length;i++){
        sum = sum + arr[i];
        
    }
    return sum;
}   

function findMax(arr){
    var max = arr[0];
    for(var i=0;i<arr.length;i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
   return max;
}

function findAvg(arr){
    var sum=0;
    for(var i=0;i<arr.length;i++){
        sum += arr[i];
    }
    return sum/arr.length;
}


function makeOddArr(){
    var oddArr=[];
    for(var i=1;i<=255;i+=2){
        oddArr.push(i);
    }
    return oddArr;
}   

function greaterThanY(arr,y){
    var count = 0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>y){
            count++;
        }
    }
    return count;
}

function squareArr(arr){
    for(var i=0;i<arr.length;i++){
    arr[i] *= arr[i];    
    }
    return arr;
}

function removeNegs(arr){
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]=0;
        }
    }
    return arr;
}

function getMaxMinAvg(arr){
    var max=0;
    var min=0;
    var sum=0;
    var returnArr=[];
    if(arr[0]>arr[1]){
        max=arr[0];
        min=arr[1];
    }
    else{
        max=arr[1];
        min=arr[0];

    }
    for(var i=2;i<arr.length;i++){
        sum += arr[i];

        if(arr[i] > max){
            max =arr[i];
        }
        else if(arr[i] < min){
            min=arr[i];
        }
    }
    avg = sum/arr.length;
    returnArr = [min,max,avg];
    return returnArr;
}

function swap(arr) {
     var lastindex = arr.length-1;
     var firstval = arr[0];
      arr[0] = arr[lastindex];
      arr[lastindex] = firstval;
  
      return arr;
}

function dojoNegs(arr){
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]="Dojo";
        }
    }
    return arr;
}