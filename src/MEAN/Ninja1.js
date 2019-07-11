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

var Ninja1 = new Ninja("Jo-Jo");
Ninja1.sayName();
Ninja1.showStats();
Ninja1.drinkSake();
Ninja1.showStats();

