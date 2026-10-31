contacts = [
    {"Name": "David Mutua", "Phone": "0767890123", "Skill": "plumbing", "City": "Nakuru"},
    {"Name": "Mercy Akinyi", "Phone": "0778901234", "Skill": "graphic design", "City": "Eldoret"},
    {"Name": "Kevin Kiprono", "Phone": "0789012345", "Skill": "electrical", "City": "Nakuru"},
    {"Name": "Faith Wanjiku", "Phone": "0790123456", "Skill": "catering", "City": "Naivasha"},
    {"Name": "John Ouma", "Phone": "0701234567", "Skill": "carpentry", "City": "Kisii"},
]

# Add a New Contact
contacts.append({"Name": "Moses Mwangi", "Phone": "0712345678", "Skill": "Mechanic", "City": "Nairobi"})

# Display All Contacts
print("=== CONTACT BOOK ===")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['Name']}")    
    print(f"   Phone: {contact['Phone']}")
    print(f"   Skill: {contact['Skill']}")
    print(f"   City: {contact['City']}")

# Search by Name
search_name = "Mike Dawa"
found_contact = False

for contact in contacts:
    if contact["Name"] == search_name:
        found_contact = True
        print("\nContact found:")
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Skill: {contact['Skill']}")
        print(f"City: {contact['City']}")
        break

if not found_contact:
    print("\nNo contact found with the name:", search_name)

#Search by City
print("\n==== NAKURU CONTACTS ====")

for contact in contacts:
    if contact["City"] == "Nakuru":
        print(f"  {contact['Name']} | {contact['Phone']}")

# Summary
print(f"\nTotal Contacts: {len(contacts)}")