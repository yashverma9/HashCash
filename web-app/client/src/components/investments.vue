<template>
  <div>
  

    <div    class="investments" >
          <div class="back" >
         <p>Investments</p>
      <div @click="scroll" class="bb">
            <p>BACK</p>
          </div>
      </div>
      <div class="container">
        <div class="fd">
          <div class="highlight">
            <p>FIXED DEPOSITS</p>
          </div>
          <!-- <div class="sa">
            <p>SHOW ALL</p>
          </div> -->
          <div class="list">
            <ul v-for="(fd,index) in fds" :key="index" class="a">
              <li >
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">PNB</th>
                        <td class="text bf">{{fd.accountNo.slice(7,15)}}</td>
                        <td class="text bf">{{fd.interestRate}}% </td>
                      </tr>
                      <tr>
                        <th class="head sf">OPD CLD</th>

                        <td class="text">{{fd.openingDate}}</td>
                        <td class="text">{{fd.maturityDate}}</td>
                      </tr>
                      <tr>
                        <th class="head sf">PA MA</th>
                        <td class="text">₹{{es}}{{fd.principalAmount}}</td>
                        <td class="text">₹{{es}}{{fd.maturityAmount}}</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <div class="rd">
          <div class="highlight">
            <p>RECURRING DEPOSITS</p>
          </div>
          <!-- <div class="sa">
            <p>SHOW ALL</p>
          </div> -->
          <div class="list">
            <ul v-for="(rd,index) in rds" :key="index" class="a">
              <li >
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">PNB</th>
                        <td class="text bf">{{rd.accountNo.slice(7,15)}}</td>
                        <td class="text bf">{{rd.interestRate}}{{es}}%</td>
                      </tr>
                      <tr>
                        <th class="head sf">TENURE RA</th>

                        <td class="text">{{rd.tenureMonths}} months</td>
                        <td class="text">₹{{es}}{{rd.recurringAmount}}{{es}}/{{es}}month</td>
                      </tr>
                      <tr>
                        <th class="head sf">CA MA</th>
                        <td class="text">₹{{es}}{{rd.currentValue}}</td>
                        <td class="text">₹{{es}}{{rd.maturityAmount}}</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <div class="mf">
          <div class="highlight">
            <p>MUTUAL FUNDS</p>
          </div>
          <!-- <div class="sa">
            <p>SHOW ALL</p>
          </div> -->
          <div class="list">
            <ul  class="a">
              <li>
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">Name </th>
                        <!-- <td class="text bf">{{fd.accountNo.slice(7,15)}}</td>
                        <td class="text bf">{{fd.interestRate}}</td> -->
                        <td class="text bf">Motilal Oswal</td>
                         <td class="text bf">334212093</td>
                      </tr>
                      <tr>
                        <th class="head sf">START END</th>

                        <td class="text">1 April, 2020</td>
                        <td class="text">27 March, 2021</td>
                      </tr>
                      <tr>
                        <th class="head sf">COST FREQ</th>
                        <td class="text">₹ 5,000</td>
                        <td class="text">Monthly</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </li>

              <li >
                <div class="child">
                  <div class="table">
                    <table>
                      <tr>
                        <th class="head">Name </th>
                        <!-- <td class="text bf">{{fd.accountNo.slice(7,15)}}</td>
                        <td class="text bf">{{fd.interestRate}}</td> -->
                        <td class="text bf">Principal Fund</td>
                         <td class="text bf">9843120683</td>
                      </tr>
                      <tr>
                        <th class="head sf">START END</th>

                        <td class="text">31 March, 2019</td>
                        <td class="text">25 March, 2022</td>
                      </tr>
                      <tr>
                        <th class="head sf">COST FREQ</th>
                        <td class="text">₹ 9,000</td>
                        <td class="text">Monthly</td>
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
import axios from "axios";
export default {
  name: "investments",
  async mounted() {
    let res = await axios.get("http://localhost:8080/getFdData");
    //  console.log(res.data)
    this.fds = res.data;
    // console.log("fd data")
    // console.log(this.fds)

    let res1 = await axios.get("http://localhost:8080/getRdData");
    // console.log(res1.data)
    this.rds = res1.data;
    // console.log("rd data")
    // console.log(this.rds)
  },
  data() {
    return {
      fds: [],
      rds: [],
      es: " ",
      blurcontroll:false,
      popup:false,
    };
  },
  methods: {
    showpopup() {
      this.popup=true;
      this.blurcontroll=true;
       this.$emit('bc', 'true')
    },
    hidepopup(){
      this.popup=false;
      this.blurcontroll=false
    },
    scroll() {
         console.log("scroll called")
      const element = document.getElementById('buttons');
      element.scrollIntoView({ behavior: 'smooth' });
    },
  }
};
</script>

<style lang="scss" scoped>
.blur{
  filter: blur(10px);
}
.investments {
  //filter: blur(10px);
  //   border: solid blue;
  width: 1436px;
  height: 710px;
  //   margin-left: 46.8px;
  margin-left: 20px;
  background-color: #202020;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin: 0;
  margin-bottom: 30px;
}

.container {
  // border: dotted red;
  width: 1436px;
  height: 595px;
  display: flex;
  justify-content: space-evenly;
  margin: 0;
}
.fd {
  width: 449px;
  height: 595;
  background-color: #1d1d1d;
  position: relative;
}

.rd {
  width: 449px;
  height: 595;
  background-color: #1d1d1d;
  position: relative;
}

.mf {
  width: 449px;
  height: 595;
  background-color: #1d1d1d;
  position: relative;
}

.highlight {
  width: 449px;
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

.child {
  width: 390px;
  height: 153px;
  background-color: #181818;
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

// ul > :first-child {
//   margin-top: 80px;
// }

.list {
  // border: solid blue;
  // width: 449px;
  height: 492px;
  margin-top: 83px;
  overflow: auto;
  overflow-x: hidden;
}

.sa {
  width: 108px;
  height: 18px;

  background-color: #edc530;
  position: absolute;
  // border: dotted red;               //this is border
  bottom: 0;
  left: 170px;
  p {
    margin: -2px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;
  }
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

.table {
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
th{
  
}

td{
  // text-align: center;
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

.popup {
  width: 449px;
  height: 605px;
  margin: 0 auto;
  //border: solid palevioletred;
  position: absolute;
  z-index: 1;
  left: 37%;
  top: 117%;
  background-color: #181818;
  box-shadow: 0 5px 30px rgba(0, 0, 0, 6.3);
}

button {
  background: #edc530;
  border: 0;
  // border-radius: 4px;

  font-size: 18px;
  color: #181818;
  cursor: pointer;
  margin-left: 427px;

  &:focus {
    outline: none;
  }

  &:hover {
    background: lighten(#edc530, 10%);
  }
}

// .close{
// font-family: "Poppins", sans-serif;
//   font-weight: 500;
//   font-size: 25px;
//   }

.popuptable {
  table,
  th,
  td {
      //border: 1px solid white;
    //color: white;
  }
   th{
    text-align: left;
  }
  th,td{
    text-align: center;
  }
  th,td{
    width: 40%;
    
  }
  th{
    color: #edc530;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 25px;
  }
  td{
    text-align: center;
    font-family: "Titillium Web", sans-serif;
  }
  table{
    margin: 0;
  }
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