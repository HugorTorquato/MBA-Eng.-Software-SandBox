console.log("HUGO2")

let stocks =[]

let endpoint =  'http://localhost:4000/get'

buscarProdutosAPI()

async function buscarProdutosAPI() {
    let res = await fetch(endpoint)
    stocks = await res.json()
    console.log(stocks)
}