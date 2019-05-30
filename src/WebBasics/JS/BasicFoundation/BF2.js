function reverseArr(arr) {
  var i = 0;
    for(var i=0;i<arr.length;i++){
        arr.splice(i, 0, arr.pop());
    }
  return arr;
}
var test = reverseArr([7,2,4,3]);
console.log(test);

//keep a pointer and a value