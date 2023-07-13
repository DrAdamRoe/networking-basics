const net = require("net");

var client = net.connect({ host:"localhost", port: 3000 }, () => 
    client.write("GET / HTTP/1.1\nHost: localhost:3000\nUser-Agent:local-client\nAccept: */*")
);

client.on("data", (chunk) => {
  console.log("Received chunk: ");
  console.log(chunk.toString());
  client.end();
});
