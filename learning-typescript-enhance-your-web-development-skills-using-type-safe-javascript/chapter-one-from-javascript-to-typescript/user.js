"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function greetUser(user) {
    return "Hello, " + user.name.toUpperCase();
}
function describeUser(user) {
    if (user.age) {
        console.log("".concat(user.name, " is ").concat(user.age, " years old."));
    }
    else {
        console.log("".concat(user.name, "'s age is unknown."));
    }
}
var user1 = { name: "Alice" };
var user2 = { username: "Bob" };
console.log(greetUser(user1));
console.log(greetUser(user2));
describeUser(user1);
describeUser(user2);
