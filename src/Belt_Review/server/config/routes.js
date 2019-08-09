const rideController = require('./../controllers/rides');


module.exports = (app) => {

 app.get('/api/rides', rideController.allRides );
 app.get('/api/rides/:id', rideController.singleRide );
 app.post('/api/rides', rideController.addRide );
 app.put('/api/rides/:id', rideController.editRide );
 app.delete('/api/rides/:id', rideController.removeRide );


 app.post('/api/rides/:id/passenger', rideController.addPassenger);
 app.delete('/api/rides/:id/passenger/:p_id', rideController.removePassenger);

//39:12
}
