<template>
    <div>


          <div class="acc">
           <div class="back" >
         <p>Reminders</p>
      <div @click="scroll" class="bb">
            <p>BACK</p>
          </div>
      </div>
          <div class="list">
              <ul >
                  <li v-for = "(pmr,index) in pmrs" :key="index">
                      <div class="child">
                          <div :class="pmr.color"  class="highlight">
                            <!-- <div class="highlight1"></div> -->
                        <div class="table">
                            <table>
                              <tr>
                                 <th class="head">{{pmr.category.slice(0,5)}}</th>
                                <td class="text bf">{{pmr.short_brand}}</td> 
                                <!-- <td class="text bf">7.75%</td> -->
                          
                              </tr>
                              <tr>
                                <th class="head sf">DUE DATE</th>
                              
                                
                                <td class="text">{{pmr.next_date}}</td>
                                <!-- <td class="text">05/07/20</td> -->
                              </tr>
                              <tr>
                                <th class="head sf">AMT</th>
                                <!-- <td class="text">10000</td> -->
                                <td class="text">{{pmr.amount}}</td>
                              </tr>
                            </table>
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
import axios from "axios";
    export default {
        name:"paymentreminder",
        async mounted (){
             let res = await axios.get('http://localhost:8080/getReminderDetails');
             
             this.pmrs=res.data;
            // console.log("pmr data")
            // console.log(this.pmrs)
            // console.log("date")
            /* eslint-disable */
            var d = new Date();
            let date = d.getDate();
            let month =d.getMonth();
            let year =d.getFullYear();
            
            // console.log(date)
            // console.log(month)
            // console.log(year)

            for(var i=0;i<this.pmrs.length;i++)
            {
              // console.log("for loop")
              // console.log(this.pmrs[i].date)
              if(this.pmrs[i].date>date)
              {  
              }
                 if(this.pmrs[i].date<date)
              {
              //this.pmrs[i].date=
              }
               if(this.pmrs[i].category=="Insurance")
              {
              //this.pmrs[i].date=
              this.pmrs[i].category="INS"
              }

              if(this.pmrs[i].category=="Credit Card")
              {
              //this.pmrs[i].date=
              this.pmrs[i].category="CC"
              }
            }
            
          

            
        },
        data() {
            return {
              pmrs : [],
              
              es:" ",
            }
        },
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

.acc {
  background-color: #202020;
  height: 710px;
  width: 1467px;
//   margin: 200px auto;
margin: 0 auto; 
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  //padding: 0.1em;
  margin-top: 0;
}
.list {
  margin: 0 auto;
  margin-top: 0px;
  // border: solid blue;                    //this is border
  height: 660px;
  width: 1467px;
  width: 92%;
  // overflow: auto;
  // overflow-x: hidden;
  margin-left: 103px;
}

.child {
  width: 322px;
  height: 152px;
  background-color: #181818;
  position: relative;
}

ul {
  list-style: none;
  -webkit-columns: 3;
  -moz-columns: 3;
  columns: 3;
  padding-left: 0;
  margin-top: 0;

  li {
    padding: 10px;
    padding-top: 0;
    list-style-position: inside;
    -webkit-column-break-inside: avoid;
    page-break-inside: avoid;
    break-inside: avoid;
  }
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


  //this is table

  .table{
    // border: solid blue;
    width: 100%;
    height: 100%;
    position: relative;
    // top: -120px;
    bottom: 130px;
    right: -10px;
  }
  
  
  table {
      border-collapse: collapse;
      margin-left: 25px;
      
    width: 80%;
    height: 100%;
    // margin: 0 auto;
  }
  
  table, th, td {
      // border: 1px solid white;
    color: white;
  }
  .head{
    color: #EDC530;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-size: 25px;
  }

  th{
    width: 94px;
  }
  td{
    text-align: left;
  }
  
  .sf{
    font-size: 15px;
  }
  
  .bf{
    font-size: 22px;
  }
  .text{
    font-family: "Titillium Web", sans-serif;
  }

  .highlight{
      position: absolute;
      width: 100%;
      height: 11px;
     // background-color: #B6142C ;
      bottom: 0;
  }
  .Red{
     background-color: #B6142C ;
  }

  .Green{
     background-color: #016838 ;
  }

    .Yellow{
     background-color: #EDC530 ;
  }
  .highlight1{
    position: absolute;
    width: 100%;
    height: 11px;
    background-color: blue ;
    bottom: 0;
}
th, td{
padding: 5px;
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