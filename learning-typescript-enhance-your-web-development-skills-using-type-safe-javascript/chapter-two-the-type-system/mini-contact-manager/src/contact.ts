export type Contact = {
    name: string;
    email: string;
    phone?: string;
    isActive: boolean;
};

export function displayContact(contact: Contact) {
    console.log(`📇 ${contact.name} (${contact.email})`);
    if (contact.phone) {
        console.log(`    Phone: ${contact.phone}`);
    }

    console.log(`    Active: ${contact.isActive}`);
}