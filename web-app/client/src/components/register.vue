<template>
    <div>
        <div  v-show="three" class="overlay">
            <div v-on:click="final">
                <h1 style="text-align: center;  margin: 0 auto;">message</h1>
                <button style="margin-left:12em;"> ok.</button>
            </div>
            
        </div>
  <form @submit="fs" enctype=multipart/form-data>
     <div v-show="one" class="container">
        <div class="divheader">
         <img  class="hcimg"  src="../assets/logo.png" alt="">
        </div>
        <div  class="nformm" id="formm">
         
                <ul>
                    <li>
                        <label for="fname" class="label" >Name:</label><br>
                        <input type="text"   v-model="name"   id="fname" name="username" class="inputfield" ><br><br>
                    </li>
                    <li>
                        <label for="fname" class="label">Email:</label><br>
                        <input type="text"    v-model="email"   id="fname" name="password" class="inputfield"><br><br>
                    </li>
                    <li>
                        <label for="fname" class="label">PhNo:</label><br>
                        <input type="text"    v-model="phno"   id="fname" name="password" class="inputfield"><br><br>
                    </li>
                 
                </ul>

                <div class="navbuttons">
                    
                    <div class="buttons">
                     <p>1</p>
                            <div class="text">
                                <h5>Profile Info</h5>
                            </div>
                    </div>

                    <div class="buttons" style=" opacity: 0.5;">
                        <p style="margin-left: 10px;">2</p>
                        <div class="text">
                            <h5 style="margin-left: 5px;">Login Info</h5>
                        </div>

                    </div>



                </div>
                <div v-on:click="c " class="submitt">
                 
                   <!-- <a href="#">  <p>←</p></a> -->
                    <!-- <input  id="submit" type="submit" value="Next" name="patient" class="signup"> -->
                    <button   id="submit" class="btn">Next</button>
                </div>
               
            
        </div>


   
    </div>


     <div v-show="two" class="container">
        <div class="divheader">
         <img  class="hcimg"  src="../assets/logo.png" alt="">
        </div>
        <div  class="nformm" id="formm">
            <!-- <form @submit="fs" enctype=multipart/form-data> -->
                <ul>
                    <li>
                        <label for="fname" class="label" >User Name:</label><br>
                        <input type="text"   v-model="username"   id="fname" name="username" class="inputfield" ><br><br>
                    </li>
                    <li>
                        <label for="fname" class="label">Password:</label><br>
                        <input type="text"    v-model="password"   id="fname" name="password" class="inputfield"><br><br>
                    </li>
                    <li>
                        <label for="fname" class="label">Confirm Password:</label><br>
                        <input type="text"    v-model="cpassword"   id="fname" name="password" class="inputfield"><br><br>
                    </li>
                 
                </ul>

                <div class="navbuttons">
                    
                    <div class="buttons" style=" opacity: 0.5;">
                     <p>1</p>
                            <div class="text">
                                <h5>Profile Info</h5>
                            </div>
                    </div>

                    <div class="buttons" >
                        <p style="margin-left: 10px;">2</p>
                        <div class="text">
                            <h5 style="margin-left: 5px;">Login Info</h5>
                        </div>

                    </div>



                </div>
                <div class="submitt">
                    <div v-on:click="d">
                        <p style="cursor: pointer;">←</p>
                    </div>
                       <input  id="submit" type="submit" value="Register" name="patient" class="signup">
                    <!-- <button   id="submit" class="btn">Register</button> -->
                </div>
               
            
        </div>



    </div>
  </form>


    </div>
</template>

<script>
import axios from "axios";
    export default {
        name: "register",
             data() {
            return {
               name:"",
               email:"",
               phno:"",
                username: '',
              password: '',
              cpassword:"",
              one:true,
              two:false,
              three:false,
              firstsubmit:0
            }
        },
         methods: {
            async fs(e) {
                 e.preventDefault();
            // console.log("submit pressed")
            // console.log(this.name)
            // console.log(this.password)
            this.firstsubmit=this.firstsubmit+1;
            if(this.firstsubmit==2)
            {

                
          let params = {
            name: this.name,
            email: this.email,
            phNo: this.phno,
            username: this.username,
            password: this.password
          }
/* eslint-disable */
          let res = await axios.post('http://localhost:8080/registerUser',params);
          // console.log(res.data)
          
                // console.log("inside if")
                this.one=false;
                this.two=false;
                this.three=true;

                
            }
            
                
            },
              c(){
            // console.log("clicked")
            this.one=false;
            this.two=true;

        },
        d()
        {
            this.two=false;
            this.one=true;

        },
        async final(){
            // console.log("ok!")
            let res = await axios.get('http://localhost:8080/requestConsent');
            // console.log(res.data)
        }
        },
      
    }
</script>

<style lang="scss" scoped>
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
  top: 135px;
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
  border: solid #edc530;
  background-color: #c4c4c4;
}

#formm form ul {
  list-style: none;
  padding: 0;
}

#submit {
  height: 54px;
  width: 170px;
  background-color: #edc530;
  margin: 0 auto;
  border: none;
  font-family: "Poppins", sans-serif;
  color: #131417;
  font-weight: bold;
  font-size: 24px;
}

.submitt {
  width: 100%;
  margin: 0 auto;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  position: absolute;
}

.submitt p {
  padding: 0;
  margin: 0;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  color: #edc530;
  position: relative;
  font-size: 2rem;
}

.navbuttons {
  margin: 0;
  padding: 0;
  position: absolute;
  top: -70px;
  height: 54px;
  width: 85%;
  right: 23px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
}

.buttons {
  height: 29px;
  width: 29px;
  border-radius: 50%;
  position: relative;
  background-color: #edc530;
  color: #181818;
}

.buttons p {
  margin-top: 2px;
  margin-left: 12px;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
}

.text {
  width: 100px;
  position: absolute;
  bottom: -50px;
  right: -52px;
}

.text h5 {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 100;
}

.btn{
    /* font-size: 100%;
    font-family: inherit;

    border: 0;
    padding: 0; */
    background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
	cursor: pointer;
	outline: inherit;
   
}

input[type="text"] {
  height: 49px;
  width: 330px;
  border: solid #edc530;
  background-color: #c4c4c4;
}

.nformm {
  margin: 0;
  padding: 0;
  position: absolute;
  top: 135px;
  left: 25px;
  right: 25px;
  width: 330px;
}

label {
  font-family: "Poppins", sans-serif;
  color: white;
}

ul {
      list-style: none;
      padding: 0;
    }

    .overlay{
        //background-color: #edc530;
    //     width: 500px;
    //     height: 500px;
    //      margin: 0 auto;
    // border-radius: 25px;
    background-color: #202020;


    height: 560px;
  width: 380px;
  margin: 0 auto;
  margin-top: 9.9em;
  margin-bottom: 1em;
  border-radius: 7px;

    }
</style>