const mongoose = require('mongoose');


const PassengerSchema = mongoose.Schema({

    name: {type: String, required :[true, "Need 1 letter"], minlength: [1, 'Name must be 1 character or more']},
});

const RideSchema = mongoose.Schema({
    driver: {type: String, required :[true, "Yo, we need a wheelman!"], minlength: [1, 'Name must be 1 character or more']},
    capacity: {type: Number, required :[true, "Yo, how many henchman can we fit?"], min: [1, 'We need at least 1 guy, Johnny!'], max: [8, "Nothing fit 8, Johnny..."] },
    destination: {type: String, required :[true, "Yo, wheres the job?"], minlength: [2, 'Destination must be 2 characters']},
    riders: [PassengerSchema],
})

mongoose.model('Passenger', PassengerSchema)
mongoose.model('Ride', RideSchema)