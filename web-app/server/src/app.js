'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const morgan = require('morgan');
const util = require('util');
const path = require('path');
const fs = require('fs');
const axios = require('axios');
const {spawn} = require('child_process');
var http = require("http");
const CircularJSON = require('circular-json');
let axios_call = require('./axios_stuff.js');


const app = express();
app.use(morgan('combined'));
app.use(bodyParser.json());
app.use(cors());


var user = {
  name: "",
  email: "",
  phNo: "",
  username: "",
  password: "",
  consentId: "",
  linkReferenceNumber_Savings1:  "",
  linkReferenceNumber_Savings2:  "",
  linkReferenceNumber_RD: "",
  linkReferenceNumber_FD: ""
};




//Requesting user for consent of his financial data
app.get('/requestConsent', async (req, res) => {

let res1 = await axios_call.requestConsent()
//console.log(res1)
const str = CircularJSON.stringify(res1);
let sta = JSON.parse(str).status

res.send(sta)

/*
setTimeout(() => { 
  let msg = "";
  if (sta == "OK")
    msg = "success";
  else
    msg = "error";
  }, 3000);



res.send({"msg":msg});
*/
});


//To register user
app.post('/registerUser', async (req, res) => {
  console.log('req.body: ');
  console.log(req.body);
  user.name = req.body.name;
  user.email = req.body.email;
  user.phNo = req.body.phNo;
  user.username = req.body.username;
  user.password = req.body.password;
  
  console.log(user);
  
  res.send({"msg": "Successfully Registered "});

    });



//To login user
app.post('/loginUser', async (req, res) => {
  console.log('req.body: ');
  console.log(req.body);
  let msg;
  if (user.username == req.body.username || user.email == req.body.username){
    console.log("Inside if:1");
    if (user.password == req.body.password)
      {console.log("Inside if:2");
      msg = "Success"}
    else{
    console.log("Inside else:1");
      msg ="Incorrect Password";}
    }
  else{
  console.log("inside else:2");
    msg = "User not registered";}
  
  console.log(user)
  
  res.send({"msg": msg});

});



//Verify if user has accepted the consent permission
app.get('/verifyConsent', async (req, res) => {



  let res1 = await axios_call.verifyConsent()
  console.log(res1)
  const str = CircularJSON.stringify(res1);
  let sta = JSON.parse(str).data[0].status
  user.consentId = JSON.parse(str).data[1].consentID
  user.linkReferenceNumber_Savings1 = JSON.parse(str).data[1].accounts[0].linkReferenceNumber
  //If the user has more than one savings account
  //user.linkReferenceNumber_Savings2 = JSON.parse(str).data[0].accounts[3].linkReferenceNumber
  user.linkReferenceNumber_FD = JSON.parse(str).data[1].accounts[1].linkReferenceNumber
  user.linkReferenceNumber_RD = JSON.parse(str).data[1].accounts[2].linkReferenceNumber
  res.send(sta)
  console.log(user)

});




// app.get('/trying', async (req, res) => {

//   var dataToSend;
//   // spawn new child process to call the python script
//   const python = spawn('python', ['sh.py']);
//   // collect data from script
//   python.stdout.on('data', function (data) {
//    console.log('Pipe data from python script ...');
//    dataToSend = data.toString();
//   });
//   // in close event we are sure that stream from child process is closed
//   python.on('close', (code) => {
//   console.log(`child process close all stdio with code ${code}`);
//   // send data to browser
//   //res.send(dataToSend)
//   });
//   res.send("Done")

// });



// //Get saving data into json file
// app.post('/getSavingData', async (req, res) => {

//   let res1 = await axios_call.getSavingData(user.consentId, user.linkReferenceNumber_Savings1)
//   console.log(res1)
//   res.send(res1);
// });




//Sending saving account data
app.get('/getBankDetails', async (req, res) => {

  let jsonData = require('./bankDetails.json');
  console.log('This is after the read call');
  res.send(jsonData)  

});




app.get('/getFdData', async (req, res) => {

  let jsonData = require('./fdDetails.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




app.get('/getRdData', async (req, res) => {

  let jsonData = require('./rdDetails.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




app.get('/getReminderDetails', async (req, res) => {

  let jsonData = require('./reminderDetails.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




//monthly E I Graph
app.get('/getEIData', async (req, res) => {

  let jsonData = require('./monthWiseEI.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




// Each month all expense values distributed into different categories
app.get('/getCategoryMonthWise', async (req, res) => {

  let jsonData = require('./categoryMonthWise.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




app.get('/getAllTransactions', async (req, res) => {

  let jsonData = require('./monthWiseTransactions.json');
  //console.log('This is after the read call');
  res.send(jsonData)  

});




//Each transaction with brand name and amount yearly
app.get('/getBrandWise', async (req, res) => {

  let jsonData = require('./brandWise.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});


//Each transaction with brand name and amount yearly (only top 7 + others)
app.get('/getBrandWiseOther', async (req, res) => {

  let jsonData = require('./brandWiseOther.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});



//Each transaction with brand name and amount monthly
app.get('/getBrandWiseMonth', async (req, res) => {

  let jsonData = require('./brandWiseMonth.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});


//Each most expensive brand purchase transaction each month
app.get('/getTopBrandMonth', async (req, res) => {

  let jsonData = require('./topBrandMonth.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});

//Favourite Brands
app.get('/getFavBrands', async (req, res) => {

  let jsonData = require('./favBrands.json');
  //console.log('This is after the read call');
  res.send(jsonData)         
});




//Loyal Brands
app.get('/getLoyalBrands', async (req, res) => {

  let jsonData = require('./loyalty.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});





//Recommended Brands
app.get('/getRecBrands', async (req, res) => {

  let jsonData = require('./rec.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});




//Get brand urls
app.get('/getBrandWiseUrl', async (req, res) => {

  let jsonData = require('./brandWiseUrl.json');
  //console.log('This is after the read call');
  res.send(jsonData)  
});




app.listen(process.env.PORT || 8080);
