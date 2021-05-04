#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const result of data.results) {
      for (const character of result.characters) {
        if (character.includes(18)) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
