// this is the amusing output of chatgpt that I'll leave here for posterity's sake

const os = require('os');
const dns = require('dns');

function getLocalIP() {
  return new Promise((resolve) => {
    const interfaces = os.networkInterfaces();
    const addresses = [];

    Object.keys(interfaces).forEach((ifname) => {
      interfaces[ifname].forEach((iface) => {
        if (iface.family === 'IPv4' && !iface.internal) {
          addresses.push(iface.address);
        }
      });
    });

    if (addresses.length > 0) {
      resolve(addresses[0]);
    } else {
      // Fallback to resolve localhost
      dns.lookup(os.hostname(), (err, address) => {
        if (err) {
          resolve('127.0.0.1');
        } else {
          resolve(address);
        }
      });
    }
  });
}

(async () => {
  const localIP = await getLocalIP();
  console.log(localIP);
})();