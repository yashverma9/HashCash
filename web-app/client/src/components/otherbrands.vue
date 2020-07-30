<template>
  <div>


    <div v-show="show" class="popup" :class="data.class" >
      <button @click="show = !show, blurcontroll = !blurcontroll, email = flase " name="close">x</button>
      <!-- <h1>{{data.Coupon_id}}</h1> -->
      <div class="coffer">
          <h1>{{data.Offer}}</h1>
      </div>

      <div @click="email = true " class="sa">
        <p>Grab Offer</p>
      </div>
      <div v-show="email" class="email">
         <p>Check Your Email !</p>
      </div>
     
    
    </div>



    <div class="parent" :class="{blur:blurcontroll}">
      <p class="P">Brands You May Like <span style="font-size:20px; padding-left:10px; font-weight:100;"  >Based on deep analysis of your interests </span></p>
      <div class="display">
        <ul>
          <li>
            <div  @click="p1" id="1" class="child ">
               <img  src="../assets/Logos/inc5.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
          
            <li>
            <div @click="p1" id="2" class="child">
               <img  src="../assets/Logos/skechers.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="3" class="child">
               <img  src="../assets/Logos/relianceDigital.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="4" class="child">
               <img  src="../assets/Logos/fitbit.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="5" class="child">
               <img  src="../assets/Logos/polarBear.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="6" class="child">
               <img  src="../assets/Logos/mac.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="7" class="child">
               <img  src="../assets/Logos/crossword.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="8" class="child">
               <img  src="../assets/Logos/planb.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
            <li>
            <div @click="p1" id="9" class="child">
               <img  src="../assets/Logos/hotstar.jpg"  class="img" />
              <div class="offer">
                <p class="off">Reveal</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "otherbrands",
  data() {
    return {
      show: false,
      blurcontroll: false,
      email:false,
       data:[],
    }
  },
  methods: {
      p1(e) {
      var targetId = e.currentTarget.id;
      console.log(targetId); // returns 'foo'

      console.log("pressed");
      if (targetId == 1) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"₹ 399 off on Footwear worth ₹ 1299",class:"sh" }
      }

      if (targetId == 2) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"Extra 10% of on your first purchase", class:"sh"}
      }

      if (targetId == 3) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"Free earphones worth ₹ 399 on your first purchase", class:"sh"}
      }

      if (targetId == 4) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"Free pair of Stylish Straps with any Fitness Band", class:"sh"}
      }

      if (targetId == 5) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"Free Scoop of Ice-Cream of any flavour of your choice", class:"sh"}
      }
         if (targetId == 6) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"20% off on any Shade of Lipsticks", class:"sh"}
      }
         if (targetId == 7) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Offer:"30% off on all Best Seller Books", class:"sh"}
      }
         if (targetId == 8) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"50% off on Chicken Wings", class:"sh"}
      }
         if (targetId == 9) {
        this.show = true;
        this.blurcontroll = true;
        this.data = { Offer:"25% off on Yearly Subscription", class:"sh"}
      }

    
    }
  },
};
</script>

<style lang="scss" scoped>
.parent {
  width: 1426px;
  height: 705.2px;
  background-color: #202020;
  margin: 0, auto;
  margin-left: 17px;
  position: relative;
}

.display {
  position: absolute;
  width: 1238px;
  height: 537px;
  //border: solid blue;
  overflow-y: auto;
  overflow-x: hidden;

  top: 11.5%;
  left: 6%;

  ul {
    list-style: none;
    -webkit-columns: 3;
    -moz-columns: 3;
    columns: 3;
    padding-left: 0;
    padding: 0;
    margin-top: 0;

    li {
      padding: 5px;
      //   list-style-position: inside;
      //   -webkit-column-break-inside: avoid;
      //   page-break-inside: avoid;
      break-inside: avoid;
    }
  }
}

.child {
  margin-top: 10px;
  // border: solid blue;
  border-radius: 4%;
  width: 383px;
  height: 237px;
  position: relative;
  background-color: #5c5c5c;
  cursor: pointer;
}

.offer {
  width: 100%;
  height: 65px;
  border-radius: 10px 10px 10px 10px;
  background-color: #000000;
  position: absolute;
  bottom: 0;
  border:#F6752A
}

.off {
  text-align: center;
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  font-size: 25px;
  margin-bottom: 0;
  margin-top: 14px;
  //margin-top: 14px;
}

.P {
  // font-family: "Poppins", sans-serif;
  // color: white;
  // font-weight: 500;
  padding: -0.5em;
  // font-size: 27px;
  margin: 0;



  font-family: "Poppins", sans-serif;
    color: white;
  //  font-weight: bold;
    font-size: 45px;
}

.img{
  //  margin-left:18px; 
  //  margin-top: 10px;
    height:78%; 
    width:100%;
    border-radius: 10px;
}

.coffer{
  margin: 0 auto; 
  margin-top:20px; 

  h1{
    color: white;
    text-align: center;
  }
  border: solid #edc530;  
  width: 80%;
  
}


.sa {
  cursor: pointer;
  width: 116px;
  height: 30px;
  position: relative;
  top: 9%;
  left: 38%;
  background-color: #edc530;

  // border: dotted red;               //this is border

  p {
    margin: -3.5px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;
    font-size: 19px;
  }
}

.email{
 transition-property: height;
  transition-duration: 3s;
  position: relative;
  top: 9%;
  left: 35%;
  p{
    color: white;
    font-family: "Poppins", sans-serif;

  }
}



.popup {
  width: 449px;
  height: 449px;
  margin: 0 auto;
  //border: solid palevioletred;
  position: absolute;
  z-index: 1;
  left: 37%;
  top: 231%;
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

.blur {
  filter: blur(10px);
}


.sh{
  height: 349px;
}

.grow:hover
{
        -webkit-transform: scale(1.3);
        -ms-transform: scale(1.3);
        transform: scale(1.3);
}
</style>