import type { Contact } from "./contact.js";
import { displayContact } from "./contact.js";
import { getRandomId, appName } from "./utils.js";

// Explicit type annotation
let contactCount: number = 0;

// Inferred type
const isAppRunning = true;

// Create some contacts
const contact1: Contact = {
    name: "Alice",
    email: "alice@example.com",
    isActive: true
};

const contact2: Contact = {
    name: "Bob",
    email: "bob@example.com",
    phone: "555-1234",
    isActive: false
};

function addContact(contact: Contact): void {
    contactCount++;
    console.log(`Added contact #${getRandomId()}`);
    displayContact(contact);
}

// Run program
console.log(`🚀 Starting ${appName}...`);
addContact(contact1);
addContact(contact2);
console.log(`Total contacts: ${contactCount}`);