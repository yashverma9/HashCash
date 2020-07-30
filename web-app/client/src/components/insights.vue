<template>
  <div>
    <div class="card">
      <p>Summary This Month <span style="font-size:10px; padding-left:2px;"  >in comparison with last month </span></p> 

        <div class="container">

            <div class="child">
                <div class="list">
                    <ul>
                        <li class="headerr">
                            Income
                        </li>

                        <li class="value">
                            ₹ 153123
                        </li>

                         <li class="percent red">
                            &#11015; 1%
                        </li>
                    </ul>
                </div>
            </div>
            <div class="child">
                    <div class="list">
                    <ul>
                        <li class="headerr">
                            Expense
                        </li>

                        <li class="value">
                            ₹ 127550
                        </li>

                         <li class="percent ">
                           &#11015; 40%
                        </li>
                    </ul>
                </div>
            </div>
            <div class="child">
                    <div class="list">
                    <ul>
                        <li class="headerr">
                            Avg Daily Spends
                        </li>

                        <li  style="font-family: Titillium Web, sans-serif;" class="value">
                            ₹ 4114
                        </li>

                         <li class="percent">
                            &#11015; 40%
                        </li>
                    </ul>
                </div>
            </div>

        </div>





    </div>

  </div>
</template>

<script>
export default {
  name: "insights"
};
</script>

<style lang="scss" scoped>
.card {
  width: 888px;
  height: 357px;
  background-color: #202020;
  //   margin: 0 , auto;
  // overflow-x: hidden; /* Hide horizontal scrollbar */
  // overflow-y: scroll; /* Add vertical scrollbar */
  // overflow: scroll;
  margin-left: 8px;
  overflow: auto;
 // border: solid blue;
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


.container{
    width: 848px;
    //border: dotted blue;
    height: 240px;
    margin: 0;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
}

.child{
    width: 240px;
    height: 229px;
    background-color: #202020;
//     -webkit-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
// -moz-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
// box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
box-shadow: 0px 1px 6px 0px #000000;
}

.list{
          ul{
                  list-style: none;
                  li{
                     // color: white;
                      font-family: "Titillium Web", sans-serif;
                      padding: 0px;
                      margin: 0;
                      padding-bottom:12px;
                  }
              }
}


.headerr{
    font-size:25px; 
    color: #EDC530;
    //font-weight:bold; 
}

.value{
    font-size:35px; 
    color: white;
     font-family: "Titillium Web", sans-serif;
}

.percent{
    font-size:25px; 
    color: #07ad60;
}
.red{
    color: #B22222;
}

.list{
    margin-top:35px; 
}

// up arrow  &#11014;  down arrow &#11015;
</style>