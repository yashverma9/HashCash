<template>
  <div>
    <div style="margin-top:5px;" class="flex">
      <div v-show="g1" class="g1">
        <div class="headerr">
          <div class="flexx">
            <p>
              Spending Trends
              <span style="font-size:10px; padding-left:2px;">last 6 months</span>
            </p>

            <!-- <div class="info">
              <img
                style="width: 16px;
                  height: 20px;
                  border-radius: 50px;"
                src="./Logos/ibutton.jpg"
                alt
              />

            

              <span class="extra-info">Your Monthly Spends</span>
            </div>-->

            <div @click="st1" style="width:130px;" class="sa">
              <p>TRANSACTIONS</p>
            </div>
          </div>
          <hr />
        </div>
        <canvas width="400px" height="240px" id="myChart"></canvas>
        <!-- <div><h1>mess</h1></div> -->
      </div>

      <div v-show="false" class="t1">
        <div class="header1">
          <p>
            Transactions
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg1" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li v-for="(jul, index) in july" :key="index">
              <div class="child">
                <div class="logo">
                  <img :src="test2(jul.brand)" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>{{ jul.brand }}</li>
                    <li>{{ jul.date }}</li>
                    <!-- <li>{{ jul.url }}</li> -->
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{ jul.ammount }}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <div v-show="g2" class="g2">
        <div class="headerr">
          <div class="flexx">
            <p>
              Category Trends
              <span style="font-size:10px; padding-left:2px;">This month</span>
            </p>
            <div @click="st2" class="sa">
              <p>LIST ALL</p>
            </div>
          </div>
          <hr />
        </div>
        <canvas height="180px" id="myChart1"></canvas>
      </div>

      <div v-show="t2" id="t2" class="t1">
        <div class="header1">
          <p>
            Categories
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg2" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/bills.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Bills</li>

                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Bills}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/cashwithdrawal.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Cash Withdrawal</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Cash Withdrawal"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <!-- <li>
              <div class="child">
                <div class="logo"></div>
                <div class="table">
                  <ul>
                    <li>
                      Courier
                    </li>
                    <li>
                     {{julyy.Month}}
                    </li>
                  </ul>
                </div>
                <div class="amt">
                  <h4> <span>₹ {{julyy.Courier}}</span></h4>
                </div>
              </div>
            </li>-->

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/creditcard.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Credit Card</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Credit Card"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/entertainment.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Entertainment</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Entertainment}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/food_drinks.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Foods and Drinks</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Foods and Drinks"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/fuel.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Fuel</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Fuel}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/groceries.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Groceries</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Groceries}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/health.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Health</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Health}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/insurance.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Insurance</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Insurance}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/investment.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Investment</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Investment}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/emi.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Loan (EMI)</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Loan (EMI)"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/other.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Other</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Other}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/personalcare.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Personal Care</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Personal Care"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/rent.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Rent</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Rent}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/shopping.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Shopping</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Shopping}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <!-- <li>
              <div class="child">
                <div class="logo"></div>
                <div class="table">
                  <ul>
                    <li>Total_Expense</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Total_Expense}}</span>
                  </h4>
                </div>
              </div>
            </li>-->

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/transfer.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Transfer</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Transfer}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/travel.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Travel</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Travel}}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <div v-show="g3" class="g3">
        <div class="headerr">
          <div class="flexx">
            <p>
              Brand Trends
              <span style="font-size:10px; padding-left:2px;">This month</span>
            </p>
            <div @click="st3" class="sa">
              <p>LIST ALL</p>
            </div>
          </div>
          <hr />
        </div>
        <canvas width="400px" height="240px" id="myChart2"></canvas>
      </div>

      <div v-show="t3" class="t1">
        <div class="header1">
          <p>
            Brands
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg3" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li v-for="(data,index) in julyyy" :key="index">
              <div class="child">
                <div class="logo">
                  <img :src="test1(data.brand)" class="img" />
                </div>
                <div
                  class="table"
                  style="width: auto;height: auto;position: absolute;left: 22%;top: 29%;"
                >
                  <ul>
                    <li>{{data.brand}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{data.amount}}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="flex">
     

      <div v-show="true" class="t1">
        <div class="header1">
          <p>
            Transactions
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg1" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li v-for="(jul, index) in july" :key="index">
              <div class="child">
                <div class="logo">
                  <img :src="test2(jul.brand)" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>{{ jul.brand }}</li>
                    <li>{{ jul.date }}</li>
                    <!-- <li>{{ jul.url }}</li> -->
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{ jul.ammount }}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

     

      <div v-show="true" id="t2" class="t1">
        <div class="header1">
          <p>
            Categories
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg2" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/bills.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Bills</li>

                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Bills}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/cashwithdrawal.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Cash Withdrawal</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Cash Withdrawal"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <!-- <li>
              <div class="child">
                <div class="logo"></div>
                <div class="table">
                  <ul>
                    <li>
                      Courier
                    </li>
                    <li>
                     {{julyy.Month}}
                    </li>
                  </ul>
                </div>
                <div class="amt">
                  <h4> <span>₹ {{julyy.Courier}}</span></h4>
                </div>
              </div>
            </li>-->

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/creditcard.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Credit Card</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Credit Card"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/entertainment.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Entertainment</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Entertainment}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/food_drinks.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Foods and Drinks</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Foods and Drinks"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/fuel.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Fuel</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Fuel}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/groceries.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Groceries</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Groceries}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/health.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Health</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Health}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/insurance.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Insurance</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Insurance}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/investment.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Investment</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Investment}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/emi.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Loan (EMI)</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Loan (EMI)"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/other.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Other</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Other}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/personalcare.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Personal Care</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy["Personal Care"]}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/rent.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Rent</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Rent}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/shopping.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Shopping</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Shopping}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <!-- <li>
              <div class="child">
                <div class="logo"></div>
                <div class="table">
                  <ul>
                    <li>Total_Expense</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Total_Expense}}</span>
                  </h4>
                </div>
              </div>
            </li>-->

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/transfer.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Transfer</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Transfer}}</span>
                  </h4>
                </div>
              </div>
            </li>

            <li>
              <div class="child">
                <div class="logo">
                  <img src="./clogos/travel.png" class="img" />
                </div>
                <div class="table">
                  <ul>
                    <li>Travel</li>
                    <li>{{julyy.Month}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{julyy.Travel}}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

   
      <div v-show="true" class="t1">
        <div class="header1">
          <p>
            Brands
            <span style="font-size:10px; padding-left:2px;">This month</span>
          </p>

          <div @click="sg3" class="bb">
            <p>TRENDS</p>
          </div>
        </div>
        <div class="scroll">
          <ul>
            <li v-for="(data,index) in julyyy" :key="index">
              <div class="child">
                <div class="logo">
                  <img :src="test1(data.brand)" class="img" />
                </div>
                <div
                  class="table"
                  style="width: auto;height: auto;position: absolute;left: 22%;top: 29%;"
                >
                  <ul>
                    <li>{{data.brand}}</li>
                  </ul>
                </div>
                <div class="amt">
                  <h4>
                    <span>₹ {{data.amount}}</span>
                  </h4>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

/* eslint-disable */
var month = [];
var income = [];
var expenditure = [];
var april = [];
var may = [];
var june = [];
var brand = [];
var amt = [];
export default {
  name: "graphs",

  async mounted() {
    let url = await axios.get("http://localhost:8080/getBrandWiseUrl");
    this.url = url.data;

    let data2 = await axios.get("http://localhost:8080/getBrandWiseMonth");
    this.allbd = data2.data;
    this.julyyy = this.allbd;

    for (var i = 0; i < this.julyyy.length; i++) {
      for (var j = 0; j < this.url.length; j++) {
        if (this.julyyy[i].brand == this.url[j].brand) {
          this.julyyy[i].url = this.url[j].url;
        }
      }
    }
    console.log(this.julyyy);

    let data1 = await axios.get("http://localhost:8080/getCategoryMonthWise");
    this.allcd = data1.data;
    this.julyy = this.allcd[6];
    for (var x = 0; x <= this.allcd.length; x++) {
      // console.log(this.allcd[x].Month)
      // if(this.allcd[x].Month=="July")
      // {
      //   console.log("inside if")
      //      // this.julyy=this.allcd[x]
      //      console.log(this.allcd[x])
      //     //console.log(this.allcd[x])
      // }
    }
    // console.log("julyy");
    // console.log(this.julyy);
    // console.log("julyy");

    let data = await axios.get("http://localhost:8080/getAllTransactions");
    this.alltd = data.data;
    for (var i = this.alltd.length - 1; i > 0; i--) {
      if (
        (this.alltd[i].month == "July" ||
          this.alltd[i].month == "June" ||
          this.alltd[i].month == "May" ||
          this.alltd[i].month == "April" ||
          this.alltd[i].month == "March" ||
          this.alltd[i].month == "February" ||
          this.alltd[i].month == "January") &&
        this.alltd[i].type == "DEBIT"
      ) {
        let x = {
          brand: this.alltd[i].brand,
          date: this.alltd[i].valueDate,
          ammount: this.alltd[i].amount
        };
        this.july.push(x);
      }
    }

    for (var i = 0; i < this.july.length; i++) {
      for (var j = 0; j < this.url.length; j++) {
        if (this.july[i].brand == this.url[j].brand) {
          this.july[i].url = this.url[j].url;
        }
      }
    }
    // console.log(this.july)
    // console.log(this.alltd)
    let res = await axios.get("http://localhost:8080/getEIData");
    this.label = res.data;
    for (var i = 1; i <= 6; i++) {
      month.push(this.label[i].Month);
      income.push(this.label[i].Total_Income);
      expenditure.push(this.label[i].Total_Expense);
    }

    let res1 = await axios.get("http://localhost:8080/getCategoryMonthWise");
    for (var i = 0; i < res1.data.length; i++) {
      this.label2[i] = res1.data[i];
    }

    // console.log(this.label2);
    for (var i = 3; i <= 6; i++) {
      if (i == 3) {
        april.push(this.label2[i].Bills);
        april.push(this.label2[i]["Cash Withdrawal"]);
        april.push(this.label2[i].Courier);
        april.push(this.label2[i]["Credit Card"]);
        april.push(this.label2[i].Entertainment);
        april.push(this.label2[i]["Foods and Drinks"]);
        april.push(this.label2[i].Fuel);
        april.push(this.label2[i].Groceries);
        april.push(this.label2[i].Health);
        april.push(this.label2[i].Insurance);
        april.push(this.label2[i].Investment);
        april.push(this.label2[i]["Loan (EMI)"]);
        april.push(this.label2[i].Other);
        april.push(this.label2[i]["Personal Care"]);
        april.push(this.label2[i].Rent);
        april.push(this.label2[i].Shopping);
        april.push(this.label2[i].Transfer);
        april.push(this.label2[i].Travel);
      }
      if (i == 4) {
        may.push(this.label2[i].Bills);
        may.push(this.label2[i]["Cash Withdrawal"]);
        may.push(this.label2[i].Courier);
        may.push(this.label2[i]["Credit Card"]);
        may.push(this.label2[i].Entertainment);
        may.push(this.label2[i]["Foods and Drinks"]);
        may.push(this.label2[i].Fuel);
        may.push(this.label2[i].Groceries);
        may.push(this.label2[i].Health);
        may.push(this.label2[i].Insurance);
        may.push(this.label2[i].Investment);
        may.push(this.label2[i]["Loan (EMI)"]);
        may.push(this.label2[i].Other);
        may.push(this.label2[i]["Personal Care"]);
        may.push(this.label2[i].Rent);
        may.push(this.label2[i].Shopping);
        may.push(this.label2[i].Transfer);
        may.push(this.label2[i].Travel);
      }
      if (i == 6) {
        june.push(this.label2[i].Bills);
        june.push(this.label2[i]["Cash Withdrawal"]);
        june.push(this.label2[i].Courier);
        june.push(this.label2[i]["Credit Card"]);
        june.push(this.label2[i].Entertainment);
        june.push(this.label2[i]["Foods and Drinks"]);
        june.push(this.label2[i].Fuel);
        june.push(this.label2[i].Groceries);
        june.push(this.label2[i].Health);
        june.push(this.label2[i].Insurance);
        june.push(this.label2[i].Investment);
        june.push(this.label2[i]["Loan (EMI)"]);
        june.push(this.label2[i].Other);
        june.push(this.label2[i]["Personal Care"]);
        june.push(this.label2[i].Rent);
        june.push(this.label2[i].Shopping);
        june.push(this.label2[i].Transfer);
        june.push(this.label2[i].Travel);
      }
    }

    let res2 = await axios.get("http://localhost:8080/getBrandWiseMonth");
    this.label3 = res2.data;
    for (var i = 0; i < 7; i++) {
      brand.push(this.label3[i].brand);
      amt.push(this.label3[i].amount);
    }
    // console.log(april[14]);
    var x = random_rgba();
    //console.log(x);
    g1();
    g2();
    g3();
  },

  data() {
    return {
      test: "1",
      g1: true,
      t1: false,
      g2: true,
      t2: false,
      g3: true,
      t3: false,
      label: [],
      label2: [{}],
      label3: [],
      alltd: [{}],
      allcd: [{}],
      allbd: [{}],
      july: [],
      julyy: [],
      julyyy: [],
      url: [],
      test: "./Logos/ccd.jpg"
    };
  },
  computed: {
    // userWithIcon (q) {
    //   //     for (var i = 0; i < this.julyyy.length; i++) {
    //   //   for (var j = 0; j < this.url.length; j++) {
    //   //     if (y == this.url[j].brand) {
    //   //      var x = this.url[j].url;
    //   //     }
    //   //   }
    //   // }
    //   // return require(`${x}`)
    //   return require(`${this.url[0].url}`)
    //   console.log(q)
    //   // return require(`${y}`)
    // }
  },
  methods: {
    st1() {
      this.g1 = false;
      this.t1 = true;
    },
    sg1() {
      this.g1 = true;
      this.t1 = false;
    },
    sg2() {
      this.g2 = true;
      this.t2 = false;
    },
    st2() {
      this.g2 = false;
      this.t2 = true;
    },
    sg3() {
      this.g3 = true;
      this.t3 = false;
    },
    st3() {
      this.g3 = false;
      this.t3 = true;
    },
    test1(w) {
      for (var j = 0; j < this.url.length; j++) {
        if (w == this.url[j].brand) {
          var x = this.url[j].url;
          return require(`${x}`);
        }

        //  console.log(x)
      }

      // return require(`${x}`)

      // return require('./Logos/jio.jpg')
    },

    test2(w) {
      for (var j = 0; j < this.url.length; j++) {
        if (w == this.url[j].brand) {
          var x = this.url[j].url;
          return require(`${x}`);
        }

        //  console.log(x)
      }

      // return require(`${x}`)

      // return require('./Logos/jio.jpg')
    }
  }
};

/* eslint-disable */
function g1() {
  var ctx = document.getElementById("myChart").getContext("2d");
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: "bar",

    // The data for our dataset
    data: {
      labels: month,
      datasets: [
        {
          // hoverBackgroundColor:"#FFFFFF",
          label: "Income",
          backgroundColor: "#427a5b",
          borderColor: "rgb(0, 182, 97)",
          fill: false,

          borderWidth: "1",
          barThickness: "1",
          data: income
        },
        {
          // hoverBackgroundColor:"#FFFFFF",
          label: " Spendings",
          fontColor: "#FFFFFF",
          fill: false,
          backgroundColor: "#B22222",
          borderColor: "#B22222",

          borderWidth: "1",
          barThickness: "1",
          data: expenditure
        }
      ]
    },

    // Configuration options go here
    options: {
      legend: {
        display: true,
        labels: {
          fontColor: "#FFFFFF"
        }
      },
      scales: {
        gridLines: {
          gridLinescolor: "rgb(0, 182, 97)"
        },

        yAxes: [
          {
            ticks: {
              fontColor: "#FFFFFF",
              // Include a dollar sign in the ticks
              callback: function(value, index, values) {
                fontColor: "#EDC530";
                return "₹" + value;
              }
            },

            gridLines: {
              display: true
              //   color:'rgb(0, 0, 0)'
            }
          }
        ],
        xAxes: [
          {
            ticks: {
              fontColor: "#FFFFFF"
              // Include a dollar sign in the ticks
            },
            gridLines: {
              display: true
              //   color:'rgb(0, 0, 0)'
            }
          }
        ]
      }
    }
  });
}

function g2() {
  var ctx = document.getElementById("myChart1").getContext("2d");
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: "pie",

    // The data for our dataset
    data: {
      labels: [
        "Bills",
        "Cash Withdrawal",
        "Courier",
        "Credit Card",
        "Entertainment",
        "Foods and Drinks",
        "Fuel",
        "Groceries",
        "Health",
        "Insurance",
        "Investment",
        "Loan (EMI)",
        "Other",
        "Personal Care",
        "Rent",
        "Shopping",
        "Transfer",
        "Travel"
      ],
      datasets: [
        {
          label: "June",
          backgroundColor: [
            "#758AA2",
            "#fa8572",
            "#fa8572",
            "#b24968",
            "#6c3779",
            "#47535E",
            "#f58231",
            "rgb(200,228,171)",
            "rgb(248,241,163)",
            "#84577c",
            "rgb(18,135,165)",
            "#f9bf8f",
            "rgb(62,50,25)",
            "rgb(165, 108, 193)",
            "rgb(231, 124, 124)",
            "#b4cd93",
            "rgb(199,150,208)",
            "rgb(60,48,83)"

            // "#2D4A6B",
            // "#FA6047",
            // "#fa8572",
            // "#E1114F",
            // "#7F3C90",
            // "#23394E",
            // "#F58231",
            // "#9CE155",
            // "#E1D924",
            // "#1e2a78",
            // "#17b978",
            // "#0971F8",
            // "#3E32FF",
            // "#A56CC1",
            // "#430d27" ,
            // "#ac3f21",
            // "#5BABCD",
            // "#3C3053"
          ],
          borderColor: "rgb(237, 197, 48,22)",
          data: june
        }
      ]
    },

    // Configuration options go here
    options: {
      legend: {
        display: false,
        labels: {
          fontColor: "#FFFFFF"
        }
      }
    }
  });
}

function g3() {
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
            "#e67a7a",
            "#aa7070",
            "#74698c",
            "#f8a978",
            "#616C6F",
            "#b24968",
            "#fecea8"
          ],
          borderColor: "rgb(237, 197, 48,22)",
          data: amt
        }
      ]
    },

    // Configuration options go here
    options: {
      legend: {
        display: false,
        labels: {
          fontColor: "#FFFFFF"
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

function LightenDarkenColor(col, amt) {
  var num = parseInt(col, 16);
  var r = (num >> 16) + amt;
  var b = ((num >> 8) & 0x00ff) + amt;
  var g = (num & 0x0000ff) + amt;
  var newColor = g | (b << 8) | (r << 16);
  return newColor.toString(16);
}
/* eslint-enable */
/* eslint-enable */
</script>

<style lang="scss" scoped>
.flex {
  margin: 0 auto;
  border: solid blue;
  width: 1461px;
  height: auto;
  display: flex;
  justify-content: space-around;
  margin-bottom:10px;
  margin-left:0px; 
}

.g1 {
  width: 460.3px;
  height: 327px;
  //border: solid greenyellow;
  margin-top: 8px;
  // background-color:#202020;
  cursor: pointer;
}

.g2 {
  width: 460.3px;
  height: 327px;
  // border: solid greenyellow;
  margin-top: 8px;
  // background-color:#202020;
}

.g3 {
  width: 460.3px;
  height: 327px;
  // border: solid greenyellow;
  margin-top: 8px;
}

.headerr {
  // border: dotted purple;
  width: 100%;
  height: 40px;
}

p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0.5em;
  margin: 0;
  padding: 0;
}

.sa {
  cursor: pointer;
  width: 108px;
  height: 18px;
  margin-top: 4px;
  background-color: #edc530;

  // border: dotted red;               //this is border

  p {
    margin: -3.5px;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
    color: #181818;
    font-weight: 700;
  }
}

.flexx {
  display: flex;
  justify-content: space-between;
}

// ------------------------------------ TABLES ------------------------------------------------------------

.t1 {
  margin-top: 8px;
  width: 460.297px;
  height: 327px;
  //border: solid blue;
  // margin: 4em auto;
  background-color: #202020;
}

.t1 .scroll {
  width: 460.3px;
  height: 288px;
  overflow: auto;
  overflow-x: hidden;
}

.t1 .header1 {
  width: 460.3px;
  height: 38.99px;
  background-color: #202020;
  -webkit-box-shadow: 0px 1px 6px 0px #000000;
  box-shadow: 0px 1px 6px 0px #000000;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}

.t1 .header1 p {
  font-family: "Poppins", sans-serif;
  color: white;
  font-weight: 500;
  padding: 0;
  margin: 0;
  margin-top: 6px;
  margin-left: 10px;
}

.t1 .header1 .bb {
  cursor: pointer;
  width: 108px;
  height: 18px;
  margin-top: 10px;
  background-color: #edc530;
  margin-right: 10px;
}

.t1 .header1 .bb p {
  display: block;
  margin: -3px;
  margin-bottom: 1px;
  padding: 0;
  font-family: "Poppins", sans-serif;
  text-align: center;
  color: #181818;
  font-weight: 700;
}

.t1 ul {
  overflow: auto;
  overflow-x: hidden;
  list-style: none;
  padding-left: 0;
  padding: 0;
  margin-top: 5px;
}

.t1 ul li {
  padding: 5px;
}

.t1 ul li .child {
  width: 100%;
  height: 93px;
  background-color: #181818;
  position: relative;
}

.t1 ul li .child .logo {
  width: 55px;
  height: 55px;
  //background-color: #8e43e7;
  border-radius: 100%;
  position: absolute;
  top: 18%;
  left: 2%;
}

.t1 ul li .child .table {
  width: auto;
  height: auto;
  position: absolute;
  left: 22%;
  top: 16%;
}

.t1 ul li .child .table ul {
  list-style: none;
}

.t1 ul li .child .table ul li {
  color: white;
  font-family: "Titillium Web", sans-serif;
  padding: 0px;
  margin: 0;
}

.t1 ul li .child .amt {
  width: auto;
  height: 30px;
  background-color: #222020;
  border-radius: 7px;
  padding: 0 10px;
  position: absolute;
  left: 74%;
  top: 32%;
}

.t1 ul li .child .amt h4 {
  margin: 3px;
  padding: 0;
  text-align: center;
  font-family: "Poppins", sans-serif;
  color: white;
  font-size: 15px;
}

.t1 ul li .child .amt h4 span {
  color: white;
  font-family: "Titillium Web", sans-serif;
}

#t2 .table {
  width: auto;
  height: auto;
  position: absolute;
  left: 22%;
  top: 18%;
}

#t2 .table ul {
  list-style: none;
}

#t2 .table ul li {
  color: white;
  font-family: "Titillium Web", sans-serif;
  padding: 0px;
  margin: 0;
}

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

.img {
  width: 55px;
  height: 55px;
  border-radius: 50%;
}

// * {
//   transition: all .2s ease;
// }

.info {
  //border: solid #EDC530;
  // margin-right:247px;
  font-size: 15px;
  padding-left: 5px;
  width: 40px;
  height: 20px;
  border-radius: 50px;
  display: flex;

  p {
    color: white;
    text-align: center;
    // padding-right: 10px;
    // padding-top: 4px;
  }
}

.extra-info {
  display: none;
  // line-height: 30px;
  // font-size: 12px;
  // position: absolute;
  // top: 0;
  // left: 50px;
  color: white;
  z-index: 1;
  padding-left: 10px;
}

.info:hover {
  background-color: #202020;
  //padding: 0 0 0 5px;
  width: auto;
  text-align: left !important;
  p {
    display: none;
  }
}
.info:hover .extra-info {
  display: block;
}
.circle {
  cursor: pointer;
  width: 4px;
  height: 4px;
  //margin-top: 4px;
  background-color: #edc530;
}
</style>
