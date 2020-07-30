<template>
    <div>

            <div class="card">
      <p>Cards</p>
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
    }
</script>

<style lang="scss" scoped>

.card {
 height: 710px;
  width: 704.58px;
  background-color: #202020;
//   margin: 0 , auto;
  // overflow-x: hidden; /* Hide horizontal scrollbar */
  // overflow-y: scroll; /* Add vertical scrollbar */
  // overflow: scroll;
  margin-left: 8px;
  overflow: auto;
  
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
      margin-top: 69px;
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
  width: 600px;
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
  width: 600px;
  margin-left: 14px;
  display: flex;
  justify-content: space-evenly;
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
</style>