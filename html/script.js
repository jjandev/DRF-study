const getData = () => {
// const tt = document.querySelector("#test")
const myData = fetch('http:127.0.0.1:8000/movies')
    .then((response) => (response.text()))
    .then((result) => {
        console.log(result);
        // tt.textContent = result;
    }
)
}

getData()
// console.log(typeof myData)
// console.dir(myData)
// for (const tmp of myData){
//     console.log(tmp)
// }
// console.log(data)
// const getData = () => {
//     fetch('http:127.0.0.1:8000/movies')
//     .then((response) => (response.text()))
//     .then((data) => {
//         console.log(data);
//         return data;
//     }
//     )
// }