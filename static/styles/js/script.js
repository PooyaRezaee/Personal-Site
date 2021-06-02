// Values
function range(start, end) {
  return Array(end - start + 1).fill().map((_, idx) => start + idx)
}
var day_month = range(1, 30);
// Functions
function Blur(Bool) {
  if (Bool) {
      document.getElementById("blur_background").style.display = "block";
      document.getElementById("fade_background").style.display = "block";
  }
  else {
      document.getElementById("blur_background").style.display = "none";
      document.getElementById("fade_background").style.display = "none";
  }
}

function popup(status,id) {
  if (status == "open") {
      Blur(true);
      document.getElementById(id).style.display = "flex";
  }
  if (status == "close") {
      Blur(false);
      document.getElementById(id).style.display = "none";
  }
}

function ChangeFormSetting(status,id) {            
if (status == "open") {
      document.getElementById(id).style.display = "block";
      document.getElementById("settings").style.display = "none";
  }
  if (status == "close") {
      document.getElementById(id).style.display = "none";
      document.getElementById("settings").style.display = "block";
  }
}

const labels = day_month;
const data = {
  labels: labels,
  datasets: [{
    label: 'Visit last month',
    borderColor: 'rgb(54, 162, 235)',
    pointBorderColor: 'rgb(0,0,0)',
    pointBorderWidth: '5',
    data: last_month,
    fill:false,
  }]
};


const config = {
  type: 'line',
  data,
  options:{ 
    scales: {
      yAxes: [{
          ticks: {
              precision: 0
          }
      }]
    }
  }
};

var myChart = new Chart(
  document.getElementById('myChart'),
  config
); 