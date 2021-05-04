#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    console.group(err);
  } else {
    console.log(data);
  }
});
