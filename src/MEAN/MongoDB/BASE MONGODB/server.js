const app       = require("./app");
      http      = require("http");
      server    = http.createServer(app);
      
mongoose.connect('mongodb://localhost/dojo_db',{ useNewUrlParser: true });

server.listen(1337, () => {
  console.log("Server is listening on port 1337")
});