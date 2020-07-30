const axios = require('axios');
var fs = require('fs');
const CircularJSON = require('circular-json')

//Trial axios post function
//Request user consent for financial data (after user registers or if user logins after long time for the first time)
exports.requestConsent = async function (){

let res = await axios({
    method: 'post',
    url: 'https://sandbox.moneyone.in/finpro_sandbox/v2/requestconsent',
    data: {
      "partyIdentifierType": "MOBILE",
      "partyIdentifierValue": "1999999999",
      "productID": "FISH102",
      "accountID": "123",
      "vua": "1999999999@onemoney"
    },
    headers: {'Content-Type': 'application/json',
    'client_id': 'fp_test_1e03828a99bc7bbdebb9790aee3dfa4bb4f2f7dc',
    'client_secret': '9bd38e434f851a30a254bb07ed42a7e9167cde70533f1ba2996b6917c281b29fcad3c4c5',
    'organisationId': 'a45528fa-c7d2-4d6a-ab20-dad31d145c45',
    'appIdentifier': 'www.hashcash.com' }
    })

  return res;
}



//This verifies if the consent is accepted (ACTIVE) and the consentId and linkreferencenumbers of each account is stored in the JS object 
exports.verifyConsent = async function (){
console.log("inside verifyConsent")

let res = await axios({
    method: 'post',
    url: 'https://sandbox.moneyone.in/finpro_sandbox/v2/getconsentslist',
    data: {
      "partyIdentifierType": "MOBILE",
      "partyIdentifierValue": "1999999999",
      "productID": "FISH102",
      "accountID": "123"
    },
    headers: {'Content-Type': 'application/json',
    'client_id': 'fp_test_1e03828a99bc7bbdebb9790aee3dfa4bb4f2f7dc',
    'client_secret': '9bd38e434f851a30a254bb07ed42a7e9167cde70533f1ba2996b6917c281b29fcad3c4c5',
    'organisationId': 'a45528fa-c7d2-4d6a-ab20-dad31d145c45',
    'appIdentifier': 'www.hashcash.com' }
    })

  //console.log(res.data);
  return res.data;
}





exports.getSavingData = async function (consentID, linkReferenceNumber){
  console.log("inside getSavingData")
  
  let res = await axios({
      method: 'post',
      url: 'https://sandbox.moneyone.in/finpro_sandbox/getfidata',
      data: {
        "linkReferenceNumber":linkReferenceNumber, //"11fabe78-0a59-4c71-8fdb-57e54779d236",
        "consentID":  consentID//"2dfe6008-c789-4e75-8ce9-8512f996139c"
      },
      headers: {'Content-Type': 'application/json',
      'client_id': 'fp_test_1e03828a99bc7bbdebb9790aee3dfa4bb4f2f7dc',
      'client_secret': '9bd38e434f851a30a254bb07ed42a7e9167cde70533f1ba2996b6917c281b29fcad3c4c5',
      'organisationId': 'a45528fa-c7d2-4d6a-ab20-dad31d145c45',
      'appIdentifier': 'www.hashcash.com' }
      })
    //console.log(res.data["balance"]);
    //const str = CircularJSON.stringify(res);
    //let data = JSON.parse(str)
    //fs.writeFile('saving_data.json', JSON.stringify(data), function (err) {
     // if (err) throw err;
      //console.log('Saved!');
    //});
    
    return ({"msg": "Success"})
  
  }






    
  
/*


async function makeRequest() {

  const config = {
      method: 'post',
      url: 'https://sandbox.moneyone.in/finpro_sandbox/v2/requestconsent',
      data: {
        "partyIdentifierType": "MOBILE",
        "partyIdentifierValue": "1999999999",
        "productID": "102",
        "accountID": "123",
        "vua": "1999999999@onemoney"
      },
      headers: { 
        'Content-Type': 'application/json',
        'client_id': 'fp_test_1e03828a99bc7bbdebb9790aee3dfa4bb4f2f7dc',
        'client_secret': '9bd38e434f851a30a254bb07ed42a7e9167cde70533f1ba2996b6917c281b29fcad3c4c5',
        'organisationId': 'a45528fa-c7d2-4d6a-ab20-dad31d145c45',
        'appIdentifier': 'www.hashcash.com'
      }
  }

  let res = await axios(config)

  console.log(res.request._header);
}

makeRequest();

*/
