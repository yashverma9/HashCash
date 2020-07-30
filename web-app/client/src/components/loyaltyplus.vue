<template>
  <div>
    <div v-show="show" class="popup" :class="data.class" >
      <button @click="show = !show, blurcontroll = !blurcontroll, email = false " name="close">x</button>
      <!-- <h1>{{data.Coupon_id}}</h1> -->
      <div class="coffer">
          <h1>{{data.Offer}}</h1>
      </div>

      <div @click="email = true" class="sa">
        <p>Grab Offer</p>
      </div>
      <div v-show="email" class="email">
         <p>Check Your Email !</p>
      </div>
     
    
    </div>



    <div class="parent" :class="{blur:blurcontroll}">
      <div class="yellow">
        <div class="position">
          <p>LOYALTY PLUS</p>
        </div>
      </div>

      <div class="display">
        <div class="dis">
          <div @click="p1" id="1"  class="child">
            <img src="../assets/Logos/pvr.jpg" class="img" />
            <div class="offer">
              <p>Reveal</p>
            </div>
          </div>

          <div @click="p1" id="2" class="child">
            <img src="../assets/Logos/kfc.png" class="img" id="kfc" />
            <div class="offer">
              <p>Reveal</p>
            </div>
          </div>
          <div @click="p1" id="3" class="child">
            <img src="../assets/Logos/bBlunt.jpg" class="img" />
            <div class="offer">
              <p>Reveal</p>
            </div>
          </div>
          <div @click="p1" id="4" class="child">
            <img style=" background-color: black;" src="../assets/Logos/hm_t.png" class="img" />
            <div class="offer">
              <p>Reveal</p>
            </div>
          </div>
          <div @click="p1" id="5" class="child">
            <img src="../assets/Logos/adidas.jpg" class="img" />
            <div class="offer">
              <p>Reveal</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "loyaltyplus",
  data() {
    return {
      show: false,
      blurcontroll: false,
      email:false,
      data:[],
    };
  },
  methods: {
    p1(e) {
      var targetId = e.currentTarget.id;
      console.log(targetId); // returns 'foo'

      console.log("pressed");
      if (targetId == 1) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Coupon_id:"PVRC2392", Offer:"Free ticket & Large Popcorn + Pepsi combo for your next movie"}
      }

      if (targetId == 2) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Coupon_id:"PVRC2392", Offer:"Free 10pc Fiery Chicken Bucket",class:"sh"}
      }

      if (targetId == 3) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Coupon_id:"PVRC2392", Offer:"Free Manicure + Pedicure on bill above ₹ 499",class:"sh"}
      }

      if (targetId == 4) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Coupon_id:"PVRC2392", Offer:"Free Gift Card with ₹ 899 balance",class:"sh"}
      }

      if (targetId == 5) {
        this.show = true;
        this.blurcontroll = true;
        this.data = {Coupon_id:"PVRC2392", Offer:"Free T-shirt on your next purchase",class:"sh"}
      }

    
    }
  }
};
</script>

<style lang="scss" scoped>
.parent {
  width: 1426px;
  height: 427.62px;
  background-color: #202020;
  margin: 0 auto;
  margin-top: 20px;
  position: relative;
}

.yellow {
  width: 64px;
  height: 100%;
  background-color: #edc530;
  position: absolute;
  p {
    font-family: "Poppins", sans-serif;
    font-size: 36px;
    font-weight: 500;
    display: block;
    margin: 0;
    margin-right: 10px;
    margin-left: 10px;
    writing-mode: vertical-rl;
    -webkit-transform: rotate(-180deg);
  }
}

.position {
  position: relative;
  top: 87px;
  right: 7px;
}

.display {
  width: 1307px;
  height: 329px;
  //border: dotted blueviolet;
  position: absolute;
  top: 11%;
  left: 6%;
}

.dis {
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}

.child {
  margin-top: 10px;
  // border: solid blue;
  border-radius: 4%;
  width: 241px;
  height: 303px;
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
}

.offer {
  p {
    text-align: center;
    font-family: "Poppins", sans-serif;
    color: #edc530;
    font-weight: 500;
    font-size: 25px;
    margin-top: 14px;
  }
}

.img {
  margin-left: 8px;
  margin-top: 10px;
  height: 185px;
  width: 227px;
}

#kfc {
  margin: 0;
  width: 300px;
  height: 190px;
  margin-left: -30px;
  margin-top: 8px;
}

.popup {
  width: 449px;
  height: 449px;
  margin: 0 auto;
  //border: solid palevioletred;
  position: absolute;
  z-index: 1;
  left: 37%;
  top: 132%;
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
  position: relative;
  top: 9%;
  left: 35%;
  p{
    color: white;
    font-family: "Poppins", sans-serif;

  }
}

.sh{
  height: 349px;
}
</style>