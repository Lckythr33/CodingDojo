const app       = require("./app");
      http      = require("http");
      server    = http.createServer(app);
      
server.listen(1337, () => {
  console.log("Server is listening on port 1337")
});