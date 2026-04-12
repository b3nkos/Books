type User = {
    name: string;
    age?: number
}

function greetUser(user: User): string {
    return "Hello, " + user.name.toUpperCase();
}

function describeUser(user: User) {
    if (user.age) {
        console.log(`${user.name} is ${user.age} years old.`);
    } else {
        console.log(`${user.name}'s age is unknown.`);
    }
}

const user1 = { name: "Alice" };
const user2 = { username: "Bob" };

console.log(greetUser(user1));
console.log(greetUser(user2));

describeUser(user1);
describeUser(user2);

export {}