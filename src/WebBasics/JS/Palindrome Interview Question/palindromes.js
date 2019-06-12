function isPalindrome(str){
    var half = Math.floor(str.length/2);
    for(var i =0; i < half; i++){
        if(str[i]!==str[str.length-i-1]){
            return false;
        }
    }
    return true;
}

  function longestPalindrome(s) {
    var max_len = 0,
      max = '';
    for (var i = 0; i < s.length; i++) {
        var substring = s.substr(i, s.length);
        if (substring.length <= max_len) break; //Stop Loop for smaller strings
            for (var j = substring.length; j >= 0; j--) {
                var pal_sub = substring.substr(0, j);
                if (pal_sub.length <= max_len) break; // Stop loop for smaller strings
                    if (isPalindrome(pal_sub)) {
                        max_len = pal_sub.length;
                        max = pal_sub;
        }
      }
    }
    return max;
  }

 test = longestPalindrome("i love dydad and aracecars");
 console.log(test)