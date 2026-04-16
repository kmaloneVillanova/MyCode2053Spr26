//alert("hello!");
//console.log("hello!");

var x=10;
console.log(x);

function print3Ways() {
    console.log("hello");
    alert("hello!");
    document.write("hello!");
}

var x='hello';
console.log(x);

function plainOldFunction() {
    console.log("this is a plain function");
    function nestedFunction() {
        console.log("this is a nested function");
    }
    nestedFunction();
}

var funExpression = function(){
    console.log("this is a funct exp");
}

function callback() {
    console.log("this is the call back function")
}

function firstFunction(cb) {
    cb();
}
function soManyFunctions() {
    plainOldFunction();
    firstFunction(callback);   
    funExpression();
    firstFunction(funExpression);

}

var dogObj={
    name: 'boomer',
    type: 'labradoodle',
    age: 10,
    tricks: ['roll over', 'paw', 'sit'],
    speak: function(){console.log('woof')}
}
console.log("My dog"+dogObj.name+' is '+dogObj.age+"years old"+
    'and can do lots of tricks like '+dogObj.tricks[1]
);
