const express   = require("express");
      app       = express();
      appConfig = require("./main-config");


appConfig.init(app, express);

app.get("/", (req, res) => {
  res.render("index");
})


module.exports = app;