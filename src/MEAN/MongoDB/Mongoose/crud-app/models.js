const mongoose = require("mongoose");

mongoose.Promise = require("bluebird");
mongoose.connect('mongodb://localhost/dojo_db',{ useNewUrlParser: true });

var DojoSchema = new mongoose.Schema({ 
    location: String,
    capacity: Number,
})

mongoose.model('Dojo', DojoSchema);


