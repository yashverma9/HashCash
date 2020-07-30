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

    <div class="container">
      <div class="divvheader">
        <img class="hcimg" style="height:105px; width:'105px" src="../assets/user.svg" alt />
      </div>

      <table>
        <tr>
          <th>Name</th>
          <td>Shreya Sinha</td>
        </tr>
        <tr>
          <th>Dob</th>
          <td>1947-08-15</td>
        </tr>
        <tr>
          <th>Mobile</th>
          <td>9716841208</td>
        </tr>

            <tr>
          <th>Address</th>
          <td>8/1190, 5th Cross, 3rd Main, 7th Block, Jayanagar, Bangalore - 560011</td>
        </tr>
            <tr>
          <th>Email</th>
          <td>shreya9@gmail.com</td>
        </tr>
            <tr>
          <th>Pan</th>
          <td>AIMPN5746M</td>
        </tr>
            


      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",

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

.container {
  width: 712.83px;
  height: 525.98px;
  background-color: #202020;
  // margin:0 , auto;
  margin-top: 137px;
  position: relative;
  // left: 0%;
  // margin-left: -50px;
  // top: 50%;
  //margin-top: -50px;
}

.divvheader {
  height: 120px;
  width: 120px;
  border-radius: 50%;
  //border: solid white;
  background-color: #202020;
  position: absolute;
  top: -60px;
  left: 275px;
  right: 130px;

  --webkit-box-shadow: 0px 1px 6px 0px #000000;
  box-shadow: 0px 1px 6px 0px #000000;
}

table {
  border-collapse: collapse;
  position: absolute;
  left: 15%;
  //margin-left: -50px;
  top: 16%;
  //margin-top: -50px;
}

table,
th,
td {
  //border: 1px solid white;
  text-align: left;
}


 th{
    color: #edc530;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 22px;
  padding: 8px;
  }

   td{
    color: white;
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 18px;
   padding: 8px;
   padding-left:50px; 
   //width: 10px;
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