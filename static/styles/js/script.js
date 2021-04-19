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