<template>
  <div>
    <div class="acc">
      <p>Accounts</p>
      <div id="list">
        <ul v-for="(account, index) in accounts" :key="index">
          <li>
            <div class="child">
              <div class="header">
                <p>PNB</p>
              </div>

              <div class="info">
                <table>
                  <tr>
                    <td>{{ account.accountNo.slice(7, 15) }}</td>
                  </tr>

                  <tr>
                    <td>{{ account.typeAccount }}</td>
                  </tr>
                </table>
              </div>

              <div class="balance">
                <div class="b">
                       <div class="ball" style="margin: 0 , auto;">
                  <h4 style="text-align: centre;">
                    Bal <span> ₹{{ account.currentBalance }}</span>
                  </h4>
                </div>

                </div>
           
              </div>
            </div>
          </li>

          <li>
            <div class="child">
              <div class="header">
                <p>PAYPAL</p>
              </div>

              <div class="info">
                <table>
                  <tr>
                    <td>WALLET</td>
                  </tr>

                  <tr>
                    <td></td>
                  </tr>
                </table>
              </div>

              <div class="balance">
                <div class="b">
                     <div class="ball" style="margin: 0 , auto;">
                  <h4 style="text-align: centre;">Bal <span> ₹ 4561</span></h4>
                </div>
                </div>
             
              </div>
            </div>
          </li>

          <li>
            <div class="child">
              <div class="header">
                <p>PAYTM</p>
              </div>

              <div class="info">
                <table>
                  <tr>
                    <td>WALLET</td>
                  </tr>

                  <tr>
                    <td></td>
                  </tr>
                </table>
              </div>

              <div class="balance">
                <div class="b">
                        <div class="ball" style="margin: 0 , auto;">
                  <h4 style="text-align: centre;">Bal <span> ₹ 2101</span></h4>
                </div>
                </div>
          
              </div>
            </div>
          </li>

           <li>
            <div class="child">
              <div class="header">
                <p>AMZN</p>
              </div>

              <div class="info">
                <table>
                  <tr>
                    <td>WALLET</td>
                  </tr>

                  <tr>
                    <td></td>
                  </tr>
                </table>
              </div>

              <div class="balance">
                <div class="b">
                     <div class="ball" style="margin: 0 , auto;">
                  <h4 style="text-align: centre;">Bal <span> ₹ 2500</span></h4>
                </div>
                </div>
             
              </div>
            </div>
          </li>


        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "accounts",
  async mounted() {
    let res = await axios.get("http://localhost:8080/getBankDetails");
    //  console.log(res.data)
    this.accounts = res.data;
    // console.log("mounted")
    // console.log(this.accounts)
  },
  data() {
    return {
      accounts: [],
    };
  },
  methods: {
    name() {},
  },
};
</script>

<style lang="scss" scoped>
body {
  margin: 0;
  padding: 0;
  background-color: #181818;
}

.acc {
  background-color: #202020;
  height: 357px;
  width: 518px;
  margin: 0 auto;
  //   margin-bottom: 200px;
  //   margin: 200px auto;
}
.child {
  width: 200px;
  height: 110px;
  background-color: #181818;
  position: relative;
}

ul {
  list-style: none;
  -webkit-columns: 2;
  -moz-columns: 2;
  columns: 2;
  padding-left: 0;
  padding: 0;
  margin-top: 0;

  li {
    padding: 5px;
    list-style-position: inside;
    -webkit-column-break-inside: avoid;
    page-break-inside: avoid;
    break-inside: avoid;
  }
}
.a {
  padding: 0;
}

#list {
  // width: 100%;
  // height: 100%;
  width: 429px;
  height: 239px;
  margin: 0 auto;
  // border: solid blue;
 // overflow: auto;
  // overflow-x: hidden;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin-top: 0;
}

//Scroll bar

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  // background: #f1f1f1;
  background: #272727;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.header {
  // border: solid blue;
  height: 31px;
  width: 58px;
  position: absolute;
  top: 0;
  left: 10px;
  p {
    margin: 0;
    padding: 0;
    font-family: "Poppins", sans-serif;
    font-size: 28px;
    color: #edc530;
  }
}

.info {
  // border: solid red;
  width: 55px;
  height: 39px;
  position: absolute;
  top: 1px;
  right: 20px;
}

.balance {
  width: 100%;
  height: 26px;
  // border: solid green;
  position: absolute;
  bottom: 6px;
  left: 0px;
  right: 31px;

  h4 {
    margin: 0;
    padding: 0;
    font-family: "Poppins", sans-serif;
    color: white;
    font-size: 19px;
    span {
      // color:#EDC530;
      font-family: "Titillium Web", sans-serif;
    }
  }
}

table,
th,
td {
  //  border: 1px solid white;
  //  border-collapse: collapse;
  color: white;
  height: 100%;
  width: 100%;
  font-family: "Titillium Web", sans-serif;
  text-align: right;
}

.b{
  //border: dotted darkmagenta;
  display: flex;
  justify-content: center;
  
}
</style>
