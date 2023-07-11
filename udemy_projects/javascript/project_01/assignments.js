const country = "Mexico";
const continent = "North America";
let population = 128000000;

console.log(country)
console.log(continent)
console.log(population)

// let javascriptIsFun = true;
// console.log(javascriptIsFun);

// let x, y;
// x = y = 25-10-5

// //Challenge 1:
// let massMark = 78;
// const heightMark = 1.69;
// let massJohn = 92;
// const heightJohn = 1.95;

// const markBMI = massMark / (heightMark * heightMark);
// const johnBMI = massJohn / (heightJohn * heightJohn);

// const markHigherBMI = markBMI > johnBMI;

// console.log("Mark's BMI is " + markBMI);
// console.log("John's BMI is " + johnBMI);


// if(BMIMark > BMIJohn){
//     console.log(`Mark's BMI ${BMIMark} is higher than John's ${BMIJohn}`);
// } else {
//     console.log(`John's BMI ${BMIJohn} is higher than Mark's ${BMIMark}`);
// }


// // End BMI challenge



// const firstName = "Sam";
// const lastName = "Lundy";
// const job 
// c= "Network Engineer";
// const birthYear = 1989;
// const year = 2037;

// // //old way:
// // const sam = "I'm " + firstName + ", a " +  (year - birthYear) + " year old " + job + '!';
// // console.log(sam)
// // // template literal:
// const samNew = `I'm ${firstName}, a ${year - birthYear} year old ${job}!`;
// console.log(samNew);

// // Multi lines old:
// console.log('String with \n\
// multiple \n\
// lines');
// //multi lines with template literals
// console.log(`String
// multiple
// lines`);

//conditionals
// const age = 16;
// const isOldEnough = age >= 18;

// if(isOldEnough) {
//     console.log("Sarah can start driving 🚙");
// } else {
//     const yearsLeft = 18 - age;
//     console.log(`Sarah is too young. Wait another ${yearsLeft} years.`);
// }

// const birthYear = 2005;
// //variables need to be declared outside of if/else block
// let century;
// if(birthYear <= 2000) {
//     century = 20;
// } else {
//     century = 21;
// }
// console.log(century);

//type conversions
// const inputYear = '1991';
// console.log(Number(inputYear));
// console.log(String(23));

//type coercion
let n = '1' + 1;
n = n - 1;
console.log(n);

// 5 falsy values: 0, '', undefined, null, NaN
// console.log(Boolean(0));
// console.log(Boolean(undefined));
// console.log(Boolean('Sam'));
// console.log(Boolean({}));

const money = 0;
if(money) {
    console.log("Don't spend it all");
} else {
    console.log("You should get a job!");
}

// equality 
const age = 18;
if (age === 18) console.log("You are an adult (strict)");
if (age == 18) console.log("You are an adult (loose)");

const userAge = Number(prompt("What's your age?"));
console.log(userAge);
console.log(typeof userAge);

if (userAge === 23) {
    console.log("I wish I were 23 again...")
} else if (userAge === 7) {
    console.log("7 is also a great age")
}    else {
        console.log("Number is not 23 or 7")
}

if (userAge !== 23) console.log("Why not 23?");