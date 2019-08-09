const mongoose = require("mongoose");

mongoose.Promise = require("bluebird");
mongoose.connect("mongodb://localhost/quoting_dojo" , { useNewUrlParser: true })

const QuoteSchema =  new mongoose.Schema({
  author: String,
  quote: String,
  created_at: {type: Date, default: Date.now}
})
mongoose.model("Quote", QuoteSchema);
const Quote = mongoose.model("Quote");

module.exports = Quote;