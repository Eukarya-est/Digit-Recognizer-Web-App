const canvas = document.getElementById("canvas"),
clearCanvas = document.querySelector(".clear_canvas"),
inputCanvas = document.querySelector(".input_drawing")
ctx = canvas.getContext("2d");
ctx2 = img_preview.getContext("2d");

// Gloabal variables with default value
let isDrawing = false, brushWidth = 15, bruchColor = '#fff';
let mouselbtn = false;
const bars = document.querySelectorAll(".progress");

function setCanvasBackground() {
    //setting whole canvas background to white, so the downloaded imag background will be white
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx2.fillStyle = '#000';
    ctx2.fillRect(0, 0, img_preview.width, img_preview.height);
}

window.addEventListener("load", () => {
    // setting cavas width/height
    // offsetwidth/height returns viewable width/height of an element
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    setCanvasBackground();
});

const startDraw = () => {
    isDrawing = true;
    ctx.beginPath(); // creating new path to draw
    ctx.lineWidth = brushWidth; // passing brush Size as line width
    ctx.strokeStyle = bruchColor;
}

const drawing = (e) => {
    if(!isDrawing) return; // if isDrawing is false return from here
    ctx.lineTo(e.offsetX, e.offsetY); //creating line according to the mouse pointer
    ctx.stroke(); // drawing·filling line with color
}

// Clear
clearCanvas.addEventListener("click", () => {
    mouselbtn = false;
    ctx.clearRect(0, 0, canvas.width, canvas.height); // clearing whole canvas
    ctx2.clearRect(0, 0, img_preview.width, img_preview.height); // clearing img_preview
    setCanvasBackground();
    document.getElementById('prediction').innerHTML = "Predicition : ";  
    // document.getElementById('confidence').innerHTML = "Confidence : ";
    
    for (var i = 0; i < 10; i++){
        document.getElementById('stat'+i).innerHTML = "0%";
    }
    bars.forEach(item =>{
        item.style.width = 0
    })
});

// model prediciton
let model;
(async function(){  
    console.log("model loading...");  
    model = await tf.loadLayersModel("https://pdg2619.github.io/digit_recog_web/models/model.json")
    console.log("model loaded..");
})();

inputCanvas.addEventListener("click",async function(){  
    let canvas_img = document.getElementById("canvas"); //load canvas img
    // create processing img object
    let img_pre = document.getElementById("img_preview");
    let ctx = img_pre.getContext("2d");
    ctx.drawImage(canvas_img, 4, 4, 20, 20);

    // prediction
    let resize_img = tf.browser.fromPixels(canvas_img).resizeNearestNeighbor([28, 28]).mean(2).expandDims(2).expandDims().toFloat();  //preprocessimg;
    let predictions = await model.predict(resize_img).data();  
    let results = Array.from(predictions);
    displayLabel(results);
});


//output
function displayLabel(pre_data) {
    var data = []; 
    for (var i = 0; i < pre_data.length; i++){
        data.push(Math.round(pre_data[i] * 100) / 100 );
    }
    
    var max = data[0];    
    var maxIndex = 0; 
    var sumIndex = arrSum(data);
    for (var j = 1; j < data.length; j++) {        
      if (data[j] > max) {            
        maxIndex = j;            
        max = data[j];        
      }
    }
    
    let stat = new Array();
    for (var k = 0; k < data.length; k++){
        stat.push(Math.round((Math.round(data[k] * 100) / sumIndex) * 100) / 100);
        document.getElementById('stat'+k).innerHTML = stat[k] + "%";
        document.getElementsByClassName('progress')[k].setAttribute('id', stat[k]);
    }

    bars.forEach(item =>{
        let value = item.id;
        let contador = 0;
        let interval = setInterval(function(){
            item.style.width = contador + "%"
            if (contador == value){
                clearInterval(interval);
            }
            contador++;
        },8);
    })
    
    for (var l = 0; l < data.length; l++){
        document.getElementsByClassName('progress')[l].setAttribute('id', 'bar'+l);
    }

document.getElementById('prediction').innerHTML = "Predicition : "+maxIndex;  
// document.getElementById('confidence').innerHTML = "Confidence : "+(max*100).toFixed(2) + "%";
}

function arrSum(arr) {
    return arr.reduce((a, b) => (Math.round(a * 100) / 100) + (Math.round(b * 100) / 100), 0);
} 


canvas.addEventListener("mousedown",startDraw);
canvas.addEventListener("mousemove",drawing);
canvas.addEventListener("mouseup", () => isDrawing = false);