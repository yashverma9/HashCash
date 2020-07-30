<template>
  <div>
    <div class="shadow">
       <canvas width="400px" height="240px" id="myChart2"></canvas>
    </div>
      
  </div>
</template>

<script>
import axios from "axios";
var brand = [];
var amt = [];
export default {
  name: "brandgraph",
  async mounted() {
   
    let res2 = await axios.get("http://localhost:8080/getBrandWiseOther");
    this.label3 = res2.data;
    // console.log("this is is")
    // console.log(this.label3)
    for (var i = 0; i <  7; i++) {
      brand.push(this.label3[i].brand);
      amt.push(this.label3[i].amount);
    }
    //console.log(april[14]);
    var x = random_rgba();
     console.log(x);
   
    g3();
  },
  data() {
    return {
     
      label3: [],


    };
  },
};
/* eslint-disable */
function g3() {
    // console.log(brand)
  var ctx = document.getElementById("myChart2").getContext("2d");
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: "doughnut",

    // The data for our dataset
    data: {
      labels: brand,
      datasets: [
        {
          label: "My First dataset",
          backgroundColor: [
            "rgb(0,0,0)",
            "rgb(33,63,147)",
            "rgb(2,21,77)",
           "rgb(247,138,54)",
           "rgb(2,124,231)",
            "rgb(202,88,48)",
            "rgb(204,7,30)",
            
           
          ],
          borderColor: "rgb(237, 197, 48,22)",
          data: amt
        }
      ]
    },

    // Configuration options go here
    options: {
      legend: {
        display: true,
        labels: {
          fontColor: "#FFFFFF",
            fontFamily:"Poppins"
        }
      }
    }
  });
}

function random_rgba() {
  var o = Math.round,
    r = Math.random,
    s = 255;
  return (
    "rgba(" +
    o(r() * s) +
    "," +
    o(r() * s) +
    "," +
    o(r() * s) +
    "," +
    r().toFixed(1) +
    ")"
  );
}
</script>

<style lang="scss" scoped>
#myChart2{
 // background-color: beige
// margin-top: 20px;
}

.shadow{
 // border: dotted blue;
 -webkit-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
-moz-box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
box-shadow: 1px 1px 12px 4px rgba(0,0,0,1);
height: 420px;
width: 650px;
margin: 0 auto;
margin-top:18px;
padding-top: 10px;
}
</style>