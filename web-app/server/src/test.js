
async function test2 (){

    console.log("test2")

}



async function test1 (){

    await test2()
    console.log("test1")
}


test1()