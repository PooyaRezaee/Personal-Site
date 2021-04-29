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

const labels = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
];
const data = {
  labels: labels,
  datasets: [{
    label: 'My First dataset',
    borderColor: 'rgb(54, 162, 235)',
    pointBorderColor: 'rgb(0,0,0)',
    pointBorderWidth: '5',
    data: [500 ,1000, 500, 200, 1000, 2000, 2500,2100,1700,1900,1500,1000],
    fill:false,
  }]
};


const config = {
  type: 'line',
  data,
  options:{
  }
};

var myChart = new Chart(
  document.getElementById('myChart'),
  config
);