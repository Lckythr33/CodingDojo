const mongoose = require('mongoose');
const Passenger = mongoose.model('Passenger')
const Ride = mongoose.model('Ride')


module.exports = {

    allRides: (req,res) => {
            //retrive all rides and res with err or rides

        Ride.find({}, (err,rides) => {
            if(err){
                res.json(err);
            }
            else{
                res.json(rides);
            }


        })
    },

    singleRide: (req,res) =>{
        Ride.findOne({_id:req.params.id}, (err,ride) =>{
            if(err){
                res.json(err);
            }
            else{
                res.json(ride);
            }

        })

    },

    addRide: (req,res) => {
        Ride.create(req.body, (err,ride) =>{
            if(err){
                res.json(err);
            }
            else{
                res.json(ride);
            }
        })

    },

    editRide: (req,res) => {
        Ride.update({_id: req.params.id}, req.body, (err,data)=> {
            if(err){
                res.json(err);
            }
            else{
                res.json(data);
            }
        })

    },

    removeRide: (req,res) => {
        Ride.remove({_id: req.params.id}, (err,data)=> {
            if(err){
                res.json(err);
            }
            else{
                res.json(data);
            }
        })

    },

    addPassenger:(req,res) =>{
        // create passenger, then push to array

        Passenger.create(req.body, (err,passenger) => {
            if(err){
                console.log("Rider validations TRIGGERED!")
                res.json(err);
            }
            else{
                Ride.update({_id: req.params.id} , {$push: {riders: passenger}}, (err,data)=>{
                    if(err){
                        console.log("Couldnt update ride");
                        res.json(err);
                    }
                    else{
                        res.json(data);
                    }

            })

        }


    })

},

    removePassenger: (req,res) => {
        Ride.update({_id: req.params.id}, {$pull: {riders: {_id: req.params.p_id}}}, (err,data)=>{
        if(err){
            res.json(err);
        }
        else{
            res.json(data);
        }
        
    })

}

}