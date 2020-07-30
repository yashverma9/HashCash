<template>
  <div>
    <div class="pc">
      <p>Your Favourite Brands</p>
      <div class="fbrands">
        <div class="ffbrands">
          <img style="height:135px; width:135px;" src="../assets/Logos/iPlanet.jpg" alt />
        </div>
        <div class="ffbrands">
          <img style="height:100%; width:100%; " src="../assets/Logos/amull.jpeg" alt />
           <!-- <img style="height:135px; width:135px;" src="../assets/Logos/bluo.jpg" alt /> -->
        </div>
        <div class="ffbrands">
          <img style="height:135px; width:135px;" src="../assets/Logos/gillys.jpg" alt />
        </div>
        <div style="background-color:black" class="ffbrands">
          <img style="height:106px; width:128px; margin-top:14px; margin-left:2px" src="../assets/Logos/hm_t.png" alt />
          <!-- <img style="height:135px; width:135px;" src="../assets/Logos/bluo.jpg" alt /> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "favbrands"
};
</script>

<style lang="scss" scoped>
.pc {
  width: 700.2px;
  height: 209.2px;
  //border: solid blue;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin: 0;
  margin-left: 53.7px;
}

.fbrands {
  width: 584px;
  height: 135px;
  //border: dotted red;
  // margin-left: 25px;
  margin: 0 auto;
  display: flex;
  justify-content: space-evenly;
}

.ffbrands {
  width: 135px;
  height: 135px;
 background-color: #202020;
}
</style>