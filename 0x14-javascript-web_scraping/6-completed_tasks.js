#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const jsonFile = JSON.parse(body);
    const taskComplete = {};
    for (const i in jsonFile) {
      const data = jsonFile[i];
      if (data.completed === true) {
        const id = data.userId;
        if (id in taskComplete) {
          taskComplete[id]++;
        } else {
          taskComplete[id] = 1;
        }
      }
    }
    console.log(taskComplete);
  }
});
