const net = require("net");

var client = net.connect({ host:"localhost", port: 3000 }, () => 
    client.write("Hello, this is the client")
);

client.on("data", (chunk) => {
  console.log("Received chunk: ");
  console.log(chunk.toString());
  client.end();
});
