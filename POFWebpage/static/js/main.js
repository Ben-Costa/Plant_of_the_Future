console.log('Hello World');
//console.warn('This is a warning');
//console.error('This is a warning');

//var, let, consts 
//var- globally scoped- do not use 
//let and consts- let- can reassign 
//const- constant variable
//use consts unless you will change the value of the variable
//can change values in array

//data types- primative- directly assigned to memeory
//string, number, boolean, null, undefined

const name = 'Ben';
const age = 30;
const isCool = true;
const rating = 4.5; //no float data type is just a number 
const x = null;
let y; //undefined 

console.log(typeof name);

//strings 
//concatination- template strings
const hello = `My name is ${name} and I am ${age}`;

console.log(hello);

//string properties 
const s = "Hello World";
//s.length
//s.toUpperCase
//s.substring(start, end index)- stops before end index
//s.split('')- will split into array by whats in the sting provided

//arrays- variables that hold multiple values

//consts numbers= new Array();
const fruits = ['apples', 'oranges','pears', 10]; //can add any values and any amount 

fruits[3]='grapes';

//cannot do fruits[]=[] as is reassigning

console.log(fruits[1]);

//fruits.push
//fruits.pop
//Array.isArray('value')- checks if value is in array
//array.indexOf('Value')

//object literals- key value pairs

const person ={
    firstname: 'John',
    lastname: 'Doe',
    age: 30,
    //embedded object
    address: {
        street: '5000 stret',
        city: 'Boston'
    }
}

console.log(person);
console.log(person.lastname);

//destructuring 
const {firstname, lastname, address: {city}} = person;

console.log(city);
console.log(firstname);

//can add properties to object via doing 
person.email = 'email@gmail.com';

//json
const todos = [
    {
        id: 1,
        text: 'take out trach',
        iscompleted: true
    },
    {
        id: 2,
        text: 'take out stuff',
        iscompleted: true
    },
    {
        id: 1,
        text: 'take out hoas',
        iscompleted: false
    }
];

const todoJSON = JSON.stringify(todos);
console.log(todoJSON);

//loops 
//for
for(let i =0; i < 10; i++){
    console.log(i);
}

//while
let i = 0;
while(i<10){
    console.log(i);
    i++;
}

//loop through array

for(let todo of todos){
    console.log(todo);
    console.log(todo.id);

}

//forEach, amp, filter
//forEach- pass function and pass in variable will do thing to each item
todos.forEach(function(todo){
    console.log(todo.text);
});

//map- returns array afer dong
const todoText = todos.map(function(todo){
    return todo.text;
});
console.log(todoText);

//filter returns objects that meet a criteria
const todoComleted = todos.filter(function(todo){
    return todo.iscompleted == true;
}).map(function(todo){
    return todo.text;
})

console.log(todoComleted);

//conditionals 

const condition = 10;

if(condition == '10'){ //double == means that string 10 and int 10 are the same 
    console.log('x is 10');
}

if(condition === '10'){  
    console.log('x is 10');
}
else if(condition === 10){
    console.log('x is int 10');
}
else{
    console.log('x is none');
}

//&& and ||, >=

//short hand if- assing variables based on conditon

const varx = 10;
const color = x > 10 ? 'red' : 'blue';
// ? = if, : = else 
console.log(color);

//switches 

switch(color){
    case 'red':
        console.log('color is red');
        break;
    case 'blue':
        console.log('color is blue');
        break;
    default:
        console.log('color is neither');
        break;
}

//functions 
function addNums(num1 = 1, num2 = 1){ //can set default values via var = value
    console.log(num1 + num2);
}

addNums(4,7);

//arrow function- to slim down functions- use for foreach functions to make smaller

const addNums2 = (num12 = 1, num21 = 1) => num12 + num21;

//Object oriented programming 

//object 

function people(firstn, lastn, dob){
    this.firstn = firstn;
    this.lastn = lastn;
    this.dob = new Date(dob); //date object 
    this.getBirthYear = function() {
        return this.dob.getFullYear();
    }
    this.getFullName = function() {
        return `${this.firstn} ${this.lastn}`;
    }
}

//prototypes

//initiate object

const person1 = new people('John', 'Smith', '4-1-1111');

console.log(person1.getBirthYear());
console.log(person1.getFullName());


//prototypes- makes so not all objects need to have the function- build outside of object 
function ppl(firstn, lastn, dob){
    this.firstn = firstn;
    this.lastn = lastn;
    this.dob = new Date(dob); //date object 
}

ppl.prototype.getBirthYear = function(){
    return this.dob.getFullYear();
}

ppl.prototype.getFullName = function(){
    return `${this.firstn} ${this.lastn}`;
}

const ppl1 = new ppl('John', 'Smith', '4-1-1111');


console.log(ppl1.getBirthYear());

//classes- same as objects but looks different 

class ppl2 {
    constructor(firstn, lastn, dob){
        this.firstn = firstn;
        this.lastn = lastn;
        this.dob = new Date(dob); //date object
    }

    getBirthYears(){
        return this.dob.getFullYear();
    }
}

const ppl22 = new ppl2('John', 'Smith', '4-1-1111');


console.log(ppl22.getBirthYears());


//The DOM- document file tree
//window object- parent of the webpage 
//window.alert(1)

//selecting html electments 

//single element selectors- 
//document- use to select things 
const form = document.getElementById('my-form');
console.log(form);

//query selector- can select anything, not just id based, but only select the first one  
const form2 = document.querySelector('h1');
console.log(form2);

//multiple element selection- selects all of them 
const form3 = document.querySelectorAll('.item');
//the above gives a node list- run array functions on it 
//use query selector 

const form4 = document.getElementsByTagName('li');
//above gives html selector 

//move through the dom 
const items = document.querySelectorAll('.item');

items.forEach((item) => console.log(item));


//chaning things in the dom- user interface 
const ul = document.querySelector('.items');

//remove elements 
//ul.remove 

//remove last item in list 
//ul.lastElementChild.remove();

//edit content 
//ul.firstElementChild.textContent = 'Hello';

//grab second 
ul.children[1].innerText = 'Brad';

//change html- use to add html dynamically 
ul.lastElementChild.innerHTML = '<h1>Hello<h1>';

//change btn element to list
const btn = document.querySelector('.btn');
btn.style.background = 'red';

//Events 
//say what event you want to listen for and then say what want to do 
//use (e) for even
//event types to go into the 'click'
//mouseover- changes on hover
//mouseout- trigger when mouse leaves 

btn.addEventListener('click', (e) => {
    e.preventDefault(); //stops form 
    //console.log(e.target.id); //gives event object id name- what was clicked on
    document.querySelector('#my-form').style.background = '#ccc';
    document.querySelector('body').classList.add('bg-dark');
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Bye<h1>';

});

//when submit on a form will submit to file- click on form must stop the form 

//event object

//when click want to change background on click 


const myForm = document.querySelector('#my-form');
const myForm = document.querySelector('#my-form');
const myForm = document.querySelector('#my-form');
const myForm = document.querySelector('#my-form');
const myForm = document.querySelector('#my-form');
const myForm = document.querySelector('#my-form');
