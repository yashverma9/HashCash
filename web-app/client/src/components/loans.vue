<template>
  <div>
    <div class="acc">
         <div class="back" >
         <p>Mortgage</p>
      <div @click="scroll" class="bb">
            <p>BACK</p>
          </div>
      </div>
      <div class="abs">
        <div class="fd">
          <div class="highlight">
            <p>LOANS</p>
          </div>
          <!-- <div class="sa">
          <p>SHOW ALL</p>
        </div> -->
          <div class="list">
            <ul class="a">
              <li @click="showpopup">
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">NAME</th>
                        <td class="text bf">PNB Personal Loan</td>
                        <td class="text    ">MSW12902746123</td>
                        <!-- <td class="text bf">2</td> -->
                      </tr>
                      <tr>
                        <!-- <th class="head sf">POLICY NO</th>
                      <td class="text    ">ADMAX1235926212</td> -->
                        <!-- <td class="text bf">2</td> -->
                      </tr>
                      <tr>
                        <th class="head sf">OPD TENURE</th>

                        <td class="text">24 December, 2019</td>
                        <td class="text">12 Years</td>
                      </tr>
                      <tr>
                        <th class="head sf">RATE EMI</th>

                        <td class="text">8.5%</td>
                        <td class="text">₹ 11,345</td>
                      </tr>
                      <tr>
                        <th class="head sf">AMT ISSUED</th>
                        <td class="text">₹ 1,500,000</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </li>

                <li @click="showpopup">
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">NAME</th>
                        <td class="text bf">IDBI Home Loan</td>
                        <td class="text    ">SBI2324095728821</td>
                        <!-- <td class="text bf">2</td> -->
                      </tr>
                      <tr>
                        <!-- <th class="head sf">POLICY NO</th>
                      <td class="text    ">ADMAX1235926212</td> -->
                        <!-- <td class="text bf">2</td> -->
                      </tr>
                      <tr>
                        <th class="head sf">OPD TENURE</th>

                        <td class="text">1 March, 2018</td>
                        <td class="text">20 Years</td>
                      </tr>
                      <tr>
                        <th class="head sf">RATE EMI</th>

                        <td class="text">10.5%</td>
                        <td class="text">₹ 14,583</td>
                      </tr>
                      <tr>
                        <th class="head sf">AMT ISSUED</th>
                        <td class="text">₹ 3,500,000</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </li>
          
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "loans",
  data() {
    return {};
  },
  methods: {
    showpopup() {},
    scroll() {
         console.log("scroll called")
      const element = document.getElementById('buttons');
      element.scrollIntoView({ behavior: 'smooth' });
    },
  },
};
</script>

<style lang="scss" scoped>
.acc {
  background-color: #202020;
  height: 710px;
  width: 704.58px;
  // margin: 200px auto;
  margin: 0, auto;
  margin-left: 12px;
  position: relative;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin-top: 0;
}

.fd {
  width: 519px;
  height: 595px;
  background-color: #1d1d1d;
  position: relative;
}

.highlight {
  width: 519px;
  height: 72px;
  background-color: #edc530;
  position: absolute;
  top: 0;

  p {
    font-family: "Poppins", sans-serif;
    text-align: center;
    font-size: 2rem;
    margin: 0;
    padding: 0;
    padding-top: 10px;
    color: #181818;
  }
}

.sa {
  width: 108px;
  height: 18px;

  background-color: #edc530;
  position: absolute;
  // border: dotted red;               //this is border
  bottom: 0;
  left: 39%;
  p {
    margin: -2px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;
    .list {
      // border: solid blue;
      // width: 449px;
      height: 492px;
      //margin-top: 83px;
      overflow: auto;
      overflow-x: hidden;
    }
  }
}

.list {
  // border: solid blue;
  // width: 449px;
  height: 492px;
  margin-top: 78px;
  overflow: auto;
  overflow-x: hidden;
  position: absolute;
  top: 0;
}

.child {
  width: 454px;
  height: 147px;
  background-color: #181818;
}

table {
  // border: solid blue;
  width: 100%;
  height: 100%;
}

table {
  border-collapse: collapse;
  margin-left: 15px;

  width: 100%;
  height: 100%;

  // margin: 0 auto;
}

table,
th,
td {
  //  border: 1px solid white;
  color: white;
}
th {
  padding-right: 15px;
}

td {
  text-align: left;
}

th,
td {
  padding: 3.5px;
  padding-right: 0px;
  padding-left: 0px;
}
.head {
  color: #edc530;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 25px;
}

.sf {
  font-size: 15px;
}

.bf {
  font-size: 22px;
}
.text {
  font-family: "Titillium Web", sans-serif;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
  //margin-top: 80px;
  // margin-left: 30px;

  margin-left: 27.1px;
  margin-right: 27.1px;
  li {
    margin-top: 0;
    padding-bottom: 20px;
  }
}

.abs {
  position: absolute;
  top: 64px;
  left: 111px;
}

.bb{
 
  cursor: pointer;
  width: 78px;
  height: 18px;
  margin-top: 10px;
  background-color: #edc530;
  margin-right: 10px;


p{
  
    display: block;
    margin: -3px;
    margin-bottom: 1px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;

}
}

.back{
  display: flex;
  justify-content: space-between
}

</style>
