var TIME_TO_CHECK = 10000;//10 seconds

function updateData(){
  getTopOverAll();
  getTopTime();
  getWarnings();
}

function getWarnings(){
  requestServer('/api/v1/warnings', function(result){
    addWarning('#result-warnings', result)
  })
}

function addWarning(destination, result){

  var total = 0;
  for(var key in result.result)
    total++

  $(destination).html('');

  if(total>0){
    reserveResult = result.result.reverse();
    for(var key in reserveResult){
      var warning = reserveResult[key];
      var html = "<div class=\"data-warn\"><span class=\"data-image\"></span><div class=\"warn-text\"><span>" + warning + "</span><ul><li>tag1</li><li>tag2</li><li>tag3</li></ul></div></div>"
      $(destination).append(html)
    }
  }else{
    var html = "<span class=\"no-data\">No data yet</span>"
    $(destination).append(html)
  }
}

function getTopTime(){
  getTop('10', '#result-time'); // 10 returns last 10 seconds stats
}

function getTopOverAll(){
  getTop('-1', '#result-overall'); // -1 returns overall stats
}

function getTop(time, destination){
  requestServer('/api/v1/stats/' + time, function(result){
    addTop(destination, result)
  })
}

function sort(object){
  var sortable = [];
  for (var key in object)
      sortable.push([key, object[key]])

  sortable.sort(function(a, b) {
      return b[1] - a[1];
  })

  return sortable;
}

function addTop(destination, result){

  var total = 0;
  for(var key in result.result)
    total++

  //clear data from screen
  $(destination).html('');

  var count = 0;
  if(total > 0){
    sortedResult = sort(result.result)
    for(var key in sortedResult){
      var hits = sortedResult[key][0];
      var section = sortedResult[key][1];
      var html = "<li><span class=\"top-number\">" + hits + "</span><span class=\"top-description\">" + section + "</span></li>"
      $(destination).append(html)
      count++;
      if(count >= 8)
        break;
    }
  }else{
    var html = "<li class=\"no-data\">No data yet</li>"
    $(destination).append(html)
  }
}

function requestServer(url, success){
  $.ajax({
    url: url,
    success: success
  });
}

function constructor(){
  setTimeout(function(){
    updateData();
    constructor();
  }, TIME_TO_CHECK);
}

updateData();
constructor();
