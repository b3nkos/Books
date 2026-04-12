import type { Contact } from "./contact.js";

export function getRandomId(): number {
    return Math.floor(Math.random() * 1000);
}

export const appName = "Contact Manager";

export function getActiveContacts(contacts: Contact[]): Contact[] {
    return contacts.filter(contact => contact.isActive);
}