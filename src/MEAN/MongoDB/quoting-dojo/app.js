const express   = require("express");
      app       = express();
      appConfig = require("./main-config");
      Quote     = require("./models");


appConfig.init(app, express);

app.get("/", (req, res) => {
  res.render("index");
})

app.post("/newquote", (req,res) => {
var quote = new Quote(req.body)
console.log(quote);
quote.save()
.then(console.log("Quote saved!"))
.catch(err => console.log(err));
res.redirect("/quotes");
})

app.get('/quotes', (req,res) => {
  Quote.find({}, null, {sort: {created_at: -1}}, (err, quotes) => {
    if (err) {
      console.log(err);
      res.redirect(500, err);
    } else {
      console.log(quotes);
      res.render("quotes", {quotes: quotes})
    }
  })

})


module.exports = app;