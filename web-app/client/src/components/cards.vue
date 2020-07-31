<template>
    <div>

            <div class="card">
          <div class="back" >
         <p>Cards</p>
      <div @click="scroll" class="bb">
            <p>BACK</p>
          </div>
      </div>
      <div class="list">
        <ul class="a">
          <li>
            <div class="child">
              <div class="highlight"></div>
              <div class="text">
                <div class="item1">
                  <p class="p1">SBI ELITE</p>
                </div>
                <div class="item2">
                   <p class="p2">6522 4670 1006 6695</p>
                </div>
                <div class="item3">
                   <p class="p3">11/24</p>
                </div>
                
               
               
              </div>
            </div>
          </li>
          <li>
            <div class="child">
              <div class="highlight"></div>
              <div class="text">
                <div class="item1">
                  <p class="p1">AXIS PRIVILEGE</p>
                </div>
                <div class="item2">
                   <p class="p2">6080 3204 2738 3157</p>
                </div>
                <div class="item3">
                  <p class="p3">08/22</p>
                </div>
                
               
                
              </div>
            </div>
          </li>
          <li>
            <div class="child">
              <div class="highlight"></div>
              <div class="text">
                <div class="item1">
                  <p class="p1">AMEX PLATINUM</p>
                </div>
                <div class="item2">
                   <p class="p2">4280 9421 1001 0010</p>
                </div>
                <div class="item3">
                     <p class="p3">01/23</p>
                </div>
                
               
             
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
        name:"cards",
        methods: {
      scroll() {
         console.log("scroll called")
      const element = document.getElementById('buttons');
      element.scrollIntoView({ behavior: 'smooth' });
    },
        },
    }
</script>

<style lang="scss" scoped>

.card {
 height: 357px;
  width: 888px;
  background-color: #202020;
//   margin: 0 , auto;
  // overflow-x: hidden; /* Hide horizontal scrollbar */
  // overflow-y: scroll; /* Add vertical scrollbar */
  // overflow: scroll;
  margin-left: 8px;
  overflow: auto;
  margin-right:0px; 
   margin-top: 146px;
  
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin: 0;
  margin-bottom: 30px;
  padding-bottom: 0;
}

.list {
                          //this is border
  ul {
      padding:0 ;
      padding-left: 50px;
      
    list-style: none;
    li {
      padding-bottom: 10px;
    }
  }
}


.child {
  width: 784px;
  height: 56px;
  background-color: #181818;
  position: relative;
}


.highlight {
  position: absolute;
  height: 56px;
  width: 14px;
  background-color: #edc530;
}
.text {
  // border: dotted red;                      //this is border
  height: 56px;
  width: 766px;
  margin-left: 14px;
  display: flex;
  justify-content: space-around;
}
.p1 {
  padding-top:9px;
  padding-left: 0;
  margin: 0;
  font-family: "Poppins", sans-serif;
  font-size: 22px;
  font-weight: 600;
}

.p2 {
  
  padding: 0;
  padding-top:9px;
  margin: 0;
  font-family: "Titillium Web", sans-serif;
  font-size: 22px;
}

.p3 {
  padding: 0;
  padding-top:9px;
  margin: 0;
  font-family: "Titillium Web", sans-serif;
  font-size: 22px;
}


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


.item1{
  //border: solid blue;
  width: 190px;
}
.item2{
 // border: solid blue;
}
.item3{
  // border: solid blue;
}


.bb{
 
  cursor: pointer;
  width: 78px;
  height: 18px;
  margin-top: 10px;
  background-color: #edc530;
  margin-right: 10px;


p{
  
    display: block;
    margin: -3px;
    margin-bottom: 1px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;

}
}

.back{
  display: flex;
  justify-content: space-between
}

</style>