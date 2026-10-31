const stkPush = {
  business_shortcode: "174379",
  phone_number: "254712345678",
  amount: 1500,
  account_ref: "JuaKaliOrder",
  description: "Sliding gate deposit",
  timestamp: new Date().toISOString()
};

// Serialize to send to backend
const payload = JSON.stringify(stkPush);
console.log("Serialized payload:");
console.log(payload);

// Pretty-print for readability
console.log("\nFormatted:");
console.log(JSON.stringify(stkPush, null, 2));

// Parse what the backend sends back
const response = JSON.parse('{"MerchantRequestID":"abc-123","ResponseCode":"0","CustomerMessage":"Success. Request accepted for processing"}');
console.log("\nBackend response:");
console.log("Code:", response.ResponseCode);
console.log("Message:", response.CustomerMessage);