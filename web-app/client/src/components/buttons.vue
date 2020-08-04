<template>
  <div>
      <div class="p">
           <p></p>
      </div>

      
    <div class="flex flex1">
      <div @click="scroll" class="child">
        <div class="img">
          <!-- <img src="./buttonlogos/accounts.png"  /> -->
           <img class="imgg" src="./buttonlogos/cards.png"  />
        </div>
        <div style="top:-8px;" class="t">
          <p>Accounts & Cards</p>
        </div>
      </div>
      <!-- <div @click="scroll1" class="child">
        <div class="img">
          <img class="imgg" src="./buttonlogos/cards.png"  />
        </div>
        <div class="t">
          <p>Cards</p>
        </div>
      </div> -->

      <div @click="scroll3" class="child">
        <div class="img">
         <img class="imgg" src="./buttonlogos/reminders.png"  />
        </div>
        <div class="t">
          <p>Reminders</p>
        </div>
      </div>

            <div @click="scroll4" class="child">
        <div class="img">
          <img class="imgg" src="./buttonlogos/trends.png"  />
        </div>
        <div style="top:-7px;" class="t">
          <p>Transactions & Trends</p>
        </div>
      </div>
    </div>
    <div class="flex flex2">


      <!-- <div @click="scroll5" class="child">
        <div class="img">
      <img class="imgg" src="./buttonlogos/trends.png"  />
        </div>
        <div class="t">
          <p>Trends</p>
        </div>
      </div> -->

      <div @click="scroll6" class="child">
        <div class="img">
       <img class="imgg" src="./buttonlogos/investments.png"  />
        </div>
        <div class="t">
          <p>Investments</p>
        </div>
      </div>
       <div @click="scroll7" id="ins" class="child">
        <div class="img">
        <img style="height:71px; width:66px; margin-left:16px  " class="imgg" src="./buttonlogos/insurance.png"  />
        </div>
        <div style="top:-9px;" class="t">
          <p>Insurance
            &Mortgage</p>
        </div>
      </div>
    </div>
    <div class="flex flex3">
     
<!-- 
        <div @click="scroll7" class="child">
        <div class="img">
      <img   style="height:71px; width:66px; margin-left:18px" class="imgg" src="./buttonlogos/mortage.png"  />
        </div>
        <div class="t">
          <p>Mortage</p>
        </div>
      </div> -->
    </div>

    <div class="insights">
             <div  class="childd">
                <div class="list">
                    <ul>
                        <li style="padding-top:10px;" class="headerr">
                            Income
                        </li>

                        <li class="value">
                            ₹ 153123
                        </li>

                         <li class="percent red">
                            &#11015; 1%
                        </li>
                    </ul>
                </div>
            </div>


              <div  class="childd">
                    <div class="list">
                    <ul>
                        <li style="padding-top:10px;" class="headerr">
                            Expense
                        </li>

                        <li class="value">
                            ₹ 127550
                        </li>

                         <li class="percent ">
                           &#11015; 40%
                        </li>
                    </ul>
                </div>
            </div>


             <div class="childd">
                    <div class="list">
                    <ul>
                        <li style="padding-top:10px;" class="headerr">
                            Avg Daily Spends
                        </li>

                        <li  style="font-family: Titillium Web, sans-serif;" class="value">
                            ₹ 4114
                        </li>

                         <li class="percent">
                            &#11015; 40%
                        </li>
                    </ul>
                </div>
            </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "buttons",
  methods: {
     scroll() {
         console.log("scroll called")
      const element = document.getElementById('accounts');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll1() {
         console.log("scroll called")
      const element = document.getElementById('cards');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll2() {
         console.log("scroll called")
      const element = document.getElementById('accounts');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll3() {
         console.log("scroll called")
      const element = document.getElementById('paymentreminder');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll4() {
         console.log("scroll called")
      const element = document.getElementById('graphs');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll5() {
         console.log("scroll called")
      const element = document.getElementById('graphs');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll6() {
         console.log("scroll called")
      const element = document.getElementById('investments');
      element.scrollIntoView({ behavior: 'smooth' });
    },
    scroll7() {
         console.log("scroll called")
      const element = document.getElementById('insurance');
      element.scrollIntoView({ behavior: 'smooth' });
    }
  },
};
</script>

<style lang="scss" scoped>
.flex {
 // border: solid blue;
  width: 77%;
  height: 102px;
  margin-top: 84px;
  margin-bottom: 80px;
  margin-left: 20px;
  display: flex;
  justify-content: space-between;
}
.flex1{
    margin-top: 80px;
}

.flex2{
  display: flex;
  justify-content: flex-start;
}
.flex3{
    display: flex;
    justify-content: flex-start;
}
#ins{
    margin-left:27px; 
}
.child {
  //border: dotted darkmagenta;
  width: 349px;
  height: 102px;
  position: relative;
  background-color: #202020;
  cursor: pointer;
}
.img {
  width: 102px;
  height: 102px;
  background-color: #edc530;
}

.imgg {
  width: 75px;
  height: 64px;
 // border-radius: 50%;
  margin-left: 12px;
  margin-top: 16px;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin: 0;
  font-size: 30px;
  text-align: left;
}

.t {
  position: absolute;
  top: 12px;
  left: 123px;
   //border: solid orangered;
  width: 190.05px;
  height: 74.800px;
}

.insights{
    position: absolute;
    width: 20%;
    height: 100%;
    //border: solid yellow;
    top: 0px;
    right: 0px;
}

.childd{
    width: 240px;
    height: 188px;
    background-color: #202020;
//     -webkit-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
// -moz-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
// box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
box-shadow: 0px 1px 6px 0px #000000;
margin:0 auto; 
margin-top:27px; 
margin-bottom:38px; 
}

.list{
            //border: dotted green;
          ul{
              
                  list-style: none;
                  li{
                     // color: white;
                      font-family: "Titillium Web", sans-serif;
                      padding: 0px;
                      margin: 0;
                      padding-top:0; 
                      padding-bottom:12px;
                  }
              }
}


.headerr{
    font-size:25px; 
    color: #EDC530;
    //font-weight:bold; 
}

.value{
    font-size:35px; 
    color: white;
     font-family: "Titillium Web", sans-serif;
}

.percent{
    font-size:25px; 
    color: #07ad60;
}
.red{
    color: #B22222;
}

.heading{
    margin:0;
}


.p{
    width: 77%;
    p{
        margin: 0;
        padding: 0;
        text-align: center;
    }
}
</style>