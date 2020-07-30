<template>
  <div>
    <div class="t1">
      <div class="header1">
        <p>All Brands <span style="font-size:10px; padding-left:2px;"  >All Time </span></p>
      </div>
      <div class="scroll">
        <ul>
          <li v-for="(spend, index) in spends" :key="index">
            <div class="child">
              <div class="logo">
                <img        :src="require(`${spend.url}`)"  class="img" >
              </div>
              <div class="table">
                <ul>
                  <li>{{ spend.brand }}</li>

                </ul>
              </div>
              <div class="amt">
                <h4>
                  <span>₹ {{ spend.amount }}</span>
                </h4>
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
  name: "spends",
  async mounted() {

    

    let url = await axios.get("http://localhost:8080/getBrandWiseUrl");
    this.url = url.data;

    let data = await axios.get("http://localhost:8080/getBrandWise");
    this.spends = data.data;
    // console.log(this.spends)

    for (var i = 0; i < this.spends.length; i++) {
      for (var j = 0; j < this.url.length; j++) {
        if (this.spends[i].brand == this.url[j].brand) {
          this.spends[i].url = this.url[j].url;
        }
      }
    }

    // console.log(this.spends)
  },
  data() {
    return {
      spends: [],
      url: [],
       test: "./Logos/ccd.jpg"
      
    };
  },
};
</script>

<style lang="scss" scoped>
.t1 {
  width: 360.5px;
  height: 704.531px;
  //border: solid blue;
  margin: 0 auto;
  background-color: #202020;
  .scroll {
    width: 360.5px;
    height: 663.26px;
    overflow: auto;
    overflow-x: hidden;
  }
  .header1 {
    width: 360.5px;
    height: 38.99px;
    background-color: #202020;
    box-shadow: 0px 1px 6px 0px #000000;
    display: flex;
    justify-content: space-between;
    p {
      font-family: "Poppins", sans-serif;
      color: white;
      font-weight: 500;
      padding: 0;
      margin: 0;
      margin-top: 6px;
      margin-left: 10px;
    }

    .bb {
      width: 108px;
      height: 18px;
      margin-top: 10px;
      background-color: #edc530;
      margin-right: 10px;

      // border: dotted red;               //this is border

      p {
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
  }

  ul {
    overflow: auto;
    overflow-x: hidden;
    list-style: none;

    padding-left: 0;
    padding: 0;
    margin-top: 5px;

    li {
      padding: 5px;

      .child {
        width: 100%;
        height: 93px;
        background-color: #181818;
        position: relative;

        //   border: dotted red;

        .logo {
          width: 55px;
          height: 55px;
          // border: solid white;
         // background-color: #8e43e7;
          border-radius: 100%;
          position: absolute;
          top: 18%;
          left: 2%;
          box-shadow: 0px 1px 6px 0px #000000;
        }
        .table {
          width: auto;
          height: auto;
          //  border: dotted red;
          position: absolute;
          left: 26%;
          top: 29%;
          ul {
            list-style: none;
            li {
              color: white;
              font-family: "Titillium Web", sans-serif;
              padding: 0px;
              margin: 0;
            }
          }
        }
        .amt {
          width: auto;
          height: 30px;
          background-color: #222020;
          border-radius: 7px;
          padding: 0 10px;
          position: absolute;
          left: 71%;
          top: 32%;

          h4 {
            margin: 3px;
            padding: 0;
            text-align: center;
            font-family: "Poppins", sans-serif;
            color: white;
            font-size: 15px;
            span {
              color: white;
              font-family: "Titillium Web", sans-serif;
            }
          }
        }
      }
    }
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

.btn {
  /* font-size: 100%;
    font-family: inherit;

    border: 0;
    padding: 0; */
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  margin: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}


.img{
  width: 55px;
  height: 55px;
  border-radius: 50%;
  border:solid   #000;
  border-width: 2px;
}
</style>
