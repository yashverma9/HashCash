<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <router-link to="/Login">Login</router-link>
      <router-link to="/">Register</router-link>
    </div> -->
      <header  class="header" id="h">


        <nav class="flex">
  
           <a  @click="d" href="http://localhost:8081/Dashboard" class="headerlinks logo" style="color:#edc530;  text-decoration:none;"><h1 >HashCash</h1></a>
  
  
          <div class="headerlinks hide-for-mobile flex">
            <router-link to="/">Home</router-link>
            <router-link to="/Login">Login</router-link>
            <router-link to="/Register">Register</router-link>
            <!-- <a >Home</a>
            <a >PFMS</a>
            <a >Refresh</a>
           -->
          </div>
        </nav>
      </header>

    <router-view/>
  </div>
</template>


<script>
  export default {
    name:"App.vue",
    methods: {
      d() {
        this.$router.push('Dashboard')
       this.$router.go('Dashboard')
      }
    },
    
  }
</script>


<style >
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');

#h{
  position: sticky;

}
html,body{
  

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  /* // background: #f1f1f1; */
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
}
body {
  margin: 0;
  padding: 0;
  background-color: #181818;
  font-family: "Poppins", sans-serif;
  /* font-family: 'Roboto Condensed'; */
}
#app{
font-family: "Poppins", sans-serif;
/* font-family: 'Roboto Condensed'; */
}
.flex {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;

}


.header {
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 2;
}

nav {
  padding: 5px;
  margin-top: 0em;
  background-color: #202020;
  padding-right: 1em;
  padding-left: 1em;
}
.header{
  
}

.headerlinks a {
  font-family: "Poppins", sans-serif;
  text-decoration: none;
  color: #edc530;
}

.headerlinks a:not(:last-child) {
  margin-right: 1.2em;
}

.logo {
  text-decoration: none;
}

.logo h1 {
  margin: 0;
  font-family: "Poppins", sans-serif;
  font-size: 1.5em;
}

.container {
  background-color: #202020;
  height: 560px;
  width: 380px;
  margin: 0 auto;
  margin-top: 9.9em;
  margin-bottom: 1em;
  border-radius: 7px;
  position: relative;
}

.divheader {
  height: 120px;
  width: 120px;
  border-radius: 50%;
  border: solid white;
  position: absolute;
  top: -60px;
  left: 130px;
  right: 130px;
}

.hcimg {
  height: 120px;
  width: 120px;
  display: block;
  border-radius: 50%;
}

#formm {
  margin: 0;
  padding: 0;
  position: absolute;
  top: 110px;
  left: 25px;
  right: 25px;
  width: 330px;
}

#formm form label {
  font-family: "Poppins", sans-serif;
  color: white;
}

#formm form input[type="text"] {
  height: 49px;
  width: 330px;
  border: solid #EDC530;
  background-color: #C4C4C4;
}

#formm form ul {
  list-style: none;
  padding: 0;
}

#submit {
  height: 54px;
  width: 170px;
  background-color: #EDC530;
  margin: 0 auto;
  border: none;
  font-family: "Poppins", sans-serif;
  color: #131417;
  font-weight: bold;
  font-size: 24px;
}

.label {
  height: 49px;
  width: 330px;
}

.submitt {
  height: 54px;
  width: 170px;
  margin: 0 auto;
}

.msg {
  position: absolute;
  top: 412px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 95%;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  margin: 0 auto;
  left: 5px;
  right: 6.5px;
}

label[for=radio] {
  color: white;
  font-family: "Poppins", sans-serif;
  margin-left: 0.3em;
  font-size: 0.8rem;
}

input[type="radio"] {
  border: solid #EDC530;
  background-color: #C4C4C4;
}

.a {
  text-decoration: none;
  color: #6A6A6A;
}

.a p {
  margin: 0;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  font-size: 0.8rem;
}

.or {
  position: absolute;
  top: 470px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 95%;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  margin: 0 auto;
  left: 6.5px;
  right: 6.5px;
}

.or h5 {
  margin: 0;
  color: white;
  font-family: "Poppins", sans-serif;
  font-size: 0.6em;
}

.Signup {
  position: absolute;
  top: 510px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 95%;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  margin: 0 auto;
  left: 6.5px;
  right: 6.5px;
}

.aa {
  text-decoration: none;
  color: #EDC530;
}

.aa p {
  margin: 0;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  font-size: 0.8rem;
}
/*# sourceMappingURL=LoginRegister.css.map */



/* width */
::-webkit-scrollbar {
    width: 10px;
  }
  
  /* Track */
  ::-webkit-scrollbar-track {
    
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




.navimg{
  margin-top: 5em; 
  color: white; 
   padding-left: 0px;
  /* //border: solid blue;  */
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
width: 37px;
  height: 40px;
  padding-left:3px; 
}


.sidenav {
  height: 100%;
  width: 46.8px;
  position: fixed;
  z-index: 1;
  /* // top: 40px; */
  left: 0;
  background-color: #202020;
  overflow-x: hidden;
    overflow-y: hidden;
  /* // padding-top: 20px; */
  top: 0;
   cursor: pointer;
}
</style>
