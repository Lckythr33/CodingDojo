var express = require("express");

var app = express();
var user;

// this is the line that tells our server to use the "/static" folder for static content
app.use(express.static(__dirname + "/static"));
// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);
// require body-parser
var bodyParser = require('body-parser');
// use it!
app.use(bodyParser.urlencoded({extended: true}));


app.get('/', function(request,response){
    response.render("form");
})

app.post('/survey', function (req, res){
    user = {name : req.body.name ,
            location : req.body.location, 
            language: req.body.language, 
            comment: req.body.comment}
    res.redirect('/results') 
});


// route to process new user form data:
app.get('/results', function (req, res){
    res.render('display', {user:user})
});


app.listen(1234, function(){
    console.log("listening on 1234")
})