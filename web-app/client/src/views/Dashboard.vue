<template>
  <div>
    <!-- <h1>this is dashboard</h1> -->

    <div class="sidenav">
      <div  class="navimg">
        <ul>
          
        <li @click="dashboard">
          <img class="navimgg" src="./SideNav/Dashboard logo white.svg" alt="">
          <p > Dashboard</p>
        </li>
        <li >
          <div @click="brands" style="cursor:pointer; z-index:1;">
              <img class="navimgg" src="./SideNav/brands logo edited.svg" alt="">
          <p > Brands</p>
          </div>
       
        </li>
        <li @click="lifestyle">
           <img class="navimgg" src="./SideNav/lifestle logo.svg" alt="">
          <p > Lifestyle</p>
        </li>
        <li @click="profile">
           <img class="navimgg" src="./SideNav/profile logo.svg" alt="">
          <p > Profile</p>
        </li>
      </ul>
      </div>
      
    </div>
    <!-- <div class="graphcontainer">
        <div class="g"></div>
        <div class="g"></div>
        <div class="g"></div>
    </div>-->
    <div class="grid-container">
        <div class="grid-item item-0" :class="{blur:blurcontroll}">
      
      </div>
      <div class="grid-item item-2" :class="{blur:blurcontroll}">
        <accounts />
      </div>
      <div class="grid-item item-3" :class="{blur:blurcontroll}">
        <!-- <insights /> -->
         <cards />
      </div>
         <div class="grid-item item-5" :class="{blur:blurcontroll}">
        <paymentreminder v-on:bc="emitf" />
      </div>
      <div class="grid-item item-1" :class="{blur:blurcontroll}">
        <graphs />
      </div>
      

   
      <!-- <div class="grid-item item-6" :class="{blur:blurcontroll}">
        <cards />
      </div> -->
      <div class="grid-item item-4">
        <investments />
      </div>
      <div class="grid-item item-7" :class="{blur:blurcontroll}">
        <insurance />
      </div>
      <div class="grid-item item-8" :class="{blur:blurcontroll}">
        <loans />
      </div>
    </div>
  </div>
</template>

<script>
import accounts from "../components/accounts.vue";
import cards from "../components/cards.vue";
import investments from "../components/investments.vue";
import paymentreminder from "../components/paymentreminder.vue";
// import taxgst from "../components/taxgst.vue";
import graphs from "../components/graphs.vue";
import insurance from "../components/insurance.vue";
import loans from "../components/loans.vue";
// import insights from "../components/insights.vue";
export default {
  name: "Dashboard",
  components: {
    accounts,
   cards,
    investments,
    paymentreminder,
    // taxgst,
    graphs,
    insurance,
    loans,
    // insights,
  },
  data() {
    return {
      blurcontroll: false
    };
  },
  methods: {
    emitf() {
      console.log("emitted worked");
    },
    dashboard()
    {
      this.$router.push('Dashboard')
       this.$router.go('Dashboard')
    },
     brands()
    {
      this.$router.push('Brands')
      this.$router.go('Brands')
    
    },
    lifestyle()
    {
      this.$router.push('Lifestyle')
      this.$router.go('Lifestyle')
      
    },
     profile()
    {
      this.$router.push('Profile')
       this.$router.go('Profile')
    }
  }
};
</script>

<style lang="scss" scoped>
.sidenav {
  height: 100%;
  width: 46.8px;
  position: fixed;
  z-index: 1;
  // top: 40px;
  left: 0;
  background-color: #202020;
  overflow-x: hidden;
  overflow-y: hidden;
  // padding-top: 20px;
  top: 0;
   cursor: pointer;
}

.test {
  height: 500px;
  width: 50px;
 // border: solid blue;
  margin-left: 46.8px;
}

.mgl {
  margin-left: 46.8px;
}

.flex {
  display: flex;
}

.header {
  position: fixed;
  width: 100%;
  top: 0;
}

.grid-container {
  border: solid red; //this is border
  margin-left: 48.6px;
  // margin-top: 48.6px;
  width: 1467px;
  // margin-top: 48.6px;
  display: grid;
  grid-template-columns: 558px 175.5px;
  grid-template-rows: 710px 710px 710px 710px 710px 710px;
  grid-row-gap: 20px;
  width: 1467px;
}

.item-0 {
  border: dotted hotpink;       //this is border
  grid-column: span 3;
}

.item-1 {
  border: dotted green;       //this is border
  grid-column: span 3;
}
.item-2 {
   border: dotted chartreuse;      //this is border
  grid-column: span 1;
  height: 710px;
}
.item-3 {
  border: dotted yellow;        //this is border
  grid-column-start: 2;
  grid-column-end: 4;
  height: 710px;
}
.item-4 {
   border: dotted silver;         //this is border
  grid-column: span 3;
  height: 710px;
}

.item-5 {
  border: dotted red; //this is border
  grid-column: span 3;
  height: 710px;
}
.item-6 {
  border: dotted orange; //this is border
  grid-column-start: 3;
  grid-column-end: 4;
  height: 710px;
}
.item-7 {
  border: dotted silver;
  grid-column: span 2;
  height: 710px;
}
.item-8 {
  border: dotted silver;
  grid-column-start: 3;
  grid-column-end: 4;
  height: 710px;
}

// .graphcontainer{
//   display: flex;
// }

// .g{
//   width: 460.3px;
//   height: 348.2px;
//   background-color: whitesmoke;
//   border: solid black;
// }

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

.blur {
  filter: blur(10px);
}

.navimg{
  margin-top: 5em; 
  color: white; 
   padding-left: 0px;
  //border: solid blue; 
  ul{
    margin: 0;
    padding: 0; 
    list-style: none;
    li{
      padding-bottom:100px; 
    } 
  }
  
  p{
    color: white;
    padding: 0;
    margin: 0;
    font-size: 8px;
    text-align: center;
  }

  
}

.navimgg{
width: 30px;
  height: 40px;
  padding-left:8px; 
}
</style>