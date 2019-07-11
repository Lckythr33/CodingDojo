var express = require("express");

var app = express();


// this is the line that tells our server to use the "/static" folder for static content
app.use(express.static(__dirname + "/static"));
// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


app.get('/', function(request,response){

    var cats  = [

            {
            name : 'Chungus' ,
            age : '1.5' ,
            sleeping : 'bathroom, perch' ,    
            },

            {name : 'Bungus' ,
            age : '2' ,
            sleeping : 'toilet, box' ,    
            },
            
            {name : 'Fungus' ,
            age : '7' ,
            sleeping : 'under the cabinet, coding dojo kitchen' ,    
            },

        ];
    response.render("cats", {cat : cats} );
})




app.listen(1234, function(){
    console.log("listening on 1234")
})