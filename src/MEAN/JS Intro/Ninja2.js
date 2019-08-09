// Define the object constructor
function Ninja(name, health=100, speed=3 , strength=3) {
    this.name = name;
    this.health = health;
    var speed = speed;
    var strength = strength;



this.sayName = function() {
    console.log("My Ninja name is " + name);
    return "My Ninja name is " + name;
}

this.punch = function(otherNinja) {

    if(otherNinja instanceof Ninja){
    otherNinja.health -= 5;
    console.log(otherNinja.name + " was punched by " + this.name + " and lost 5 health! " + otherNinja.name + "- health: " + otherNinja.health )
    }
    else{
    console.log("You missed the ninja!")

    }
}
this.kick = function(otherNinja) {
    if(otherNinja instanceof Ninja){
    otherNinja.health -= 15;
    console.log(otherNinja.name + " was kicked by " + this.name + " and lost 15 health! " + otherNinja.name + "- health: " + otherNinja.health )
    }
    else{
    console.log("You missed the ninja!")
    }
}

this.showStats = function() { 
    console.log("|Name: " + name + " | Strength: " + strength + " | Speed: " + speed + " | Health: " + health+"|");
    return " | Name: " + name + " | Strength: " + strength + " | Speed: " + speed + " | Health: " + health+"|";
}

this.drinkSake = function() {
    console.log("Drinking Sake.")
    console.log("Very good drink..")
    health += 10;
    return health; 
}

};


var Jerry;
var blueNinja = new Ninja("Goemon");
var redNinja = new Ninja("Bill Gates");
redNinja.punch(blueNinja);
redNinja.kick(blueNinja);
redNinja.punch(Jerry);
redNinja.kick("Brick Wall");
redNinja.punch(42);

