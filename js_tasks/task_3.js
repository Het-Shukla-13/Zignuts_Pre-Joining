class Shape{
    constructor(name){
        this.name = name;
    }
    calculateArea(){
        alert("The area of the " + this.name + " is not defined.");
        return NaN;
    }
}

class Circle extends Shape{
    constructor(radius){
        super("Circle");
        this.radius=radius;
    }
    
    calculateArea(){
        return Math.PI*Math.pow(this.radius, 2);
    }
}

class Triangle extends Shape{
    constructor(base, height){
        super("Triangle");
        this.base=base;
        this.height=height;
    }
    
    calculateArea(){
        return 0.5*this.base*this.height;
    }
}

let circle=new Circle(14);
let triangle=new Triangle(20, 2);
console.log("Area of the circle is: " + circle.calculateArea() + " square units.");
console.log("Area of the triangle is: " + triangle.calculateArea() + " square units.");