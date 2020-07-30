<template>
  <div>
    <div class="acc">
      <p>Insurance</p>
        <div class="abs">
              <div class="fd">
        <div class="highlight">
          <p>POLICIES</p>
        </div>
        <!-- <div class="sa">
          <p>SHOW ALL</p>
        </div> -->
        <div class="list">
          <ul    class="a">
            <li @click="showpopup">
              <div class="child">
                <div class="table">
                  <table>
                    <tr>
                      <th class="head">NAME</th>
                      <td class="text bf">Max Life </td>
                      <td class="text">ADMAX1235926212</td> 
                      <!-- <td class="text bf">2</td> -->
                    </tr>
                    <tr>
                      <!-- <th class="head sf">POLICY NO</th>
                      <td class="text    ">ADMAX1235926212</td> -->
                      <!-- <td class="text bf">2</td> -->
                    </tr>
                    <tr>
                      <th class="head sf">OPD CLD</th>

                      <td class="text">11 February, 2020</td>
                      <td class="text">10 February, 2021</td>
                    </tr>
                    <tr>
                      <th class="head sf">PREMIUM</th>
                      <td class="text">₹ 3,567</td>
                 
                    </tr>
                          <tr>
                      <th class="head sf">INSURED AMT</th>
                      <td class="text">₹ 500,000</td>
                 
                    </tr>
                    <!-- <tr>
                      <th class="head sf"></th>
                      <td class="text">₹5</td>
                 
                    </tr> -->
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
                      <td class="text bf">IndiaFirst </td>
                      <td class="text    ">NEW34432019234</td> 
                      <!-- <td class="text bf">2</td> -->
                    </tr>
                    <tr>
                      <!-- <th class="head sf">POLICY NO</th>
                      <td class="text    ">ADMAX1235926212</td> -->
                      <!-- <td class="text bf">2</td> -->
                    </tr>
                    <tr>
                      <th class="head sf">OPD CLD</th>

                      <td class="text">1 May, 2018</td>
                      <td class="text">30 April, 2021</td>
                    </tr>
                    <tr>
                      <th class="head sf">PREMIUM</th>
                      <td class="text">₹ 5,201</td>
                 
                    </tr>
                          <tr>
                      <th class="head sf">INSURED AMT</th>
                      <td class="text">₹ 1000,000</td>
                 
                    </tr>
                    <!-- <tr>
                      <th class="head sf"></th>
                      <td class="text">₹5</td>
                 
                    </tr> -->
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
  name: "insurance",
  data() {
      return {
        
        
      }
    },
    methods: {
      showpopup() {
        
      }
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
    font-weight: 700;.list {
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
    //border: 1px solid white;
  color: white;
}
th {
    padding-right: 15px;
    width: 100px;
}

td {
   text-align: left;
    width: 122px;
}

th,td{
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

.abs{
    position: absolute;
    top: 64px;
    left: 111px;
}
</style>