<template>
  <div>
    
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


      <div  class="grid-container">
        <div class="grid-item item-1">
           <topspends/>
          
        </div>
        <div  class="grid-item item-2"> <p class="brands">Brand Trends <span style="font-size:10px; padding-left:2px;"  >All Time </span></p><brandgraph/></div>
        <div  class="grid-item item-3"><spends/></div>
         <div   class="grid-item item-4"><favbrands/></div>
         
         <div  class="grid-item item-5"> <p class="p">Rewards for you <span style="font-size:20px; padding-left:10px; font-weight:100;"  >Exclusively brought to you from the brands you &#10084;</span></p><loyaltyplus/></div>
         <div  class="grid-item item-6"><otherbrands/></div>


      </div>


  </div>
</template>

<script>
import topspends from '../components/topspends.vue'
import spends from '../components/spends.vue'
import favbrands from '../components/favbrands.vue'
import brandgraph from '../components/brandgraph.vue'
import loyaltyplus from '../components/loyaltyplus.vue'
import otherbrands from '../components/otherbrands.vue'
export default {
  namme: "Brands",
  components: {
            topspends,
            spends,
            favbrands,
            brandgraph,
            loyaltyplus,
            otherbrands,
        },

        methods: {
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
        },
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
}


  .grid-container{

   // border: solid red;
    margin-left: 48.6px;
    
    width: 1467px;
    height: auto;
    // margin-top: 48.6px;
    display: grid;
    grid-template-columns: 380.5px 705px 380.5px;
     grid-template-rows: 496px 214px 630px 710px;
     row-gap: 30px;
   // grid-row-gap:20px;
  }

.grid-item{

    //border: dotted blue;
}

.item-1{
   // border: dotted green;       //this is border
    grid-column: span 1;
    grid-row: span 2;
  }

  .item-2{
    // border: dotted chartreuse;      //this is border
    grid-column-start: 2;
    grid-column-end:3 ;
  }

  .item-3{
    // border: dotted yellow;        //this is border
    grid-column-start: 3;
    grid-column-end:4 ;
  
    grid-row: span 2;
  }

  .item-4{
  //  border: dotted yellow;        //this is border
 
   grid-column-start: 2;
   grid-column-end:3 ;
   
   grid-row-start: 2;
   grid-row-end: 3;
 }

 .item-5{
     // border: dotted olivedrab;        //this is border
   
     grid-column-start: 1;
     grid-column-end:4;
     
     grid-row-start: 3;
     grid-row-end: 4;
   }

   .item-6{
    //border: dotted olivedrab;        //this is border
 
   grid-column-start: 1;
   grid-column-end:4;
    
   grid-row-start: 4;
   grid-row-end: 5;
 }

 .p{
    font-family: "Poppins", sans-serif;
    color: white;
    
    font-size: 45px;
    margin: 0;
    margin-left:17.273px;
    margin-top: 40px 
    
  } 
  .brands{
    font-family: "Poppins", sans-serif;
    color: white;
    font-weight: 500;
    //font-size: 15px;
    margin: 0;
    margin-left:27.5px;
    margin-top: 10px;
   // margin-top: 40px 
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
</style>