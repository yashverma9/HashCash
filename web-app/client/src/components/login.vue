<template>
    <div class="login">
        <h1>this is inside inside login</h1>
         <div class="container">
        <div class="divheader">
         <img  class="hcimg"  src="../assets/logo.png" alt="">
        </div>
        <div   id="formm">
            <form  @submit="fs" enctype=multipart/form-data>
                <ul>
                    <li>
                        <label for="fname" class="label" >Username:</label><br>
                        <input type="text"   v-model="username"    name="username" class="inputfield" required><br><br>
                    </li>
                    <li>
                        <label for="fname" class="label">Password:</label><br>
                        <input type="password"    v-model="password"    name="password" class="inputfield"><br><br>
                    </li>
                  
                  
                   
                    
                </ul>
                <div class="submitt">
                    <input  id="submit" type="submit" value="Login" name="patient" class="signup">
                </div>
               
            </form>
        </div>
        <div class="msg" >
                <div>
                    <input type="radio" id="male" name="gender" value="male">
                    <label for="radio">Remember Me</label>
            
                </div>
               <div >
                <a class="a" href=""><p>Forgot your password?</p></a>
               </div>
              
           
        </div>

        <div class="or">
            
            <h5>OR</h5>
        </div>

        <div class="Signup">
            
            <!-- <a class="aa" href=""><p>Signup with us Now !</p></a> -->
            <p  @click="route" class="aa">    <button  class="btn"> Signup with us Now ! </button> </p>
        </div>
    </div>
    </div>
</template>

<script>
import axios from "axios";
    export default {
        name: "login",
        data() {
            return {
                username: '',
              password: '',
            }
        },
        methods: {
            async fs(e) {
                 e.preventDefault();
            // console.log("submit pressed")
            // console.log(this.username)
            // console.log(this.password)
              let params = {
    
            username: this.username,
            password: this.password
          }

          let res = await axios.post('http://localhost:8080/loginUser',params);
          // console.log(res.data)
            let res1 = await axios.get('http://localhost:8080/verifyConsent');
          // console.log(res1.data)
          if(res.data.msg=="Success" && res1.data=="ACTIVE" )
               this.$router.push('Dashboard') 
                 this.$router.go('Dashboard')
            
                
            },
            route (){
              this.$router.push('Register') 
           
            }
        },
    }
</script>

<style  scoped>
.login{
    /* border: solid blue; */
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
#formm form input[type="password"] {
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
  cursor: pointer;
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
  top: 430px;
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
  cursor: pointer;
}

.aa {
  text-decoration: none;
  color: #EDC530;
  margin: 0;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  font-size: 0.8rem;
}

.aa p {
  margin: 0;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  font-size: 0.8rem;
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
/*# sourceMappingURL=LoginRegister.css.map */
</style>