const express   = require("express");
      app       = express();
      appConfig = require("./main-config");
      Mongoose  = require("./models");


app.use(bodyParser.urlencoded({
extended: true
}));
var Dojo = mongoose.model('Dojo') // use to query the DB

appConfig.init(app, express);

app.get("/", (req, res) => {
Dojo.find({}, function(err,dojos){
   if(err){
    console.log(err);
    }
    if(dojos){
        res.render("index", {allDojos : dojos});
        }
    })
})

app.post("/dojos", (req, res) => {
  Dojo.create(req.body, function(err,dojo){
    if(err) {
        console.log("Something failed:" + err)
    }
    if(dojo){
        console.log(dojo + " | Added Succesfully!")
    }
  })
  res.redirect('/')
})


module.exports = app;