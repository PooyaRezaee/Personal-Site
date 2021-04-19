const labels = [
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '9',
  '10',
  '11',
  '12'
];

const data = {
  labels: labels,
  datasets: [{
    label: 'Visit from Site',
    backgroundColor: 'rgb(60, 0, 109)',
    borderColor: 'rgb(216, 27, 96)',
    data: [10, 230, 451, 526, 242,202,100,500,200,200,200],
  }]
};


const config = {
  type: 'line',
  data,
  options:{
    responsive:true,
    title:{
      display:false,
    }
  }
};

var myChart = new Chart(
  document.getElementById('myChart'),
  config
);