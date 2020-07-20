function buildTable() {
  /* data route */
var url = "/api/pals";
d3.json(url).then(function(data){
  console.log(data);
  var pet_data = data;
  var tbody = d3.select("tbody");
// YOUR CODE HERE!
  pet_data.forEach((pet_data) => {
  var row = tbody.append("tr");
  Object.entries(pet_data).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});
});
}
buildTable();
function buildPlot() {
/* api route */
var url = "api/pals-summary";
d3.json(url).then(function(data){
  console.log(data);
  var x = data.map(d => d.Pet_Type);
  var y = data.map(d => d.count_pets);
  console.log("x:" + x);
  console.log("y:" + y);
  var trace = [{
      'x':x,
      'y':y,
      'type':'bar'
  }];
  var layout={
      margin: {t:30,
      b : 100}
  };
  Plotly.plot("plot",trace,layout);
}
)
}
buildPlot();