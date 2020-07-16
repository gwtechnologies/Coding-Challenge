// api url
const url = "https://pjx02kldej.execute-api.eu-west-1.amazonaws.com/default/get_river_level";
fetch(url).then((resp) => resp.json())
.then(function(data) {

    /// INSERT CODE HERE
    var date = data["date_time"]
    var level = data["river_level"]
 
    // current level is displayed with time formatted
    document.getElementById("currentLevel").innerHTML = "<h1 ><em> Current Level: </em>" + level + "m <em>at</em> " + date + "</h1>"
    // if levels are rising or falling
    if (RISING){
        document.getElementById("changeInLevel").innerHTML = "<img style='display:inline' src='img/down.png' height='50px' width='50px'><p style='display:inline; padding:1px;'> Falling </p>"
    }else{
        document.getElementById("changeInLevel").innerHTML = "<img style='display:inline' src='img/up.png' height='50px' width='50px'><p style='display:inline; padding:1px;'> Rising </p>"
    };

    // the set limits for each class
    const topLevel = 0.65;
    const intLevel = 0.62;
    const novLevel = 0.6;
    
    
    // if level higher than each crew limit
    if (true){
        document.getElementById("topCrews").innerHTML += "<button style='display:inline;' type='button' class='btn btn-danger'>Not Suitable</button>"
    }else{
        document.getElementById("topCrews").innerHTML += "<button type='button' class='btn btn-success'>Suitable</button>"
    }

    if (true){
        document.getElementById("intCrews").innerHTML += "<button style='display:inline;' type='button' class='btn btn-danger'>Not Suitable</button>"
    }else{
        document.getElementById("intCrews").innerHTML += "<button type='button' class='btn btn-success'>Suitable</button>"
    }

    if (true){
        document.getElementById("novCrews").innerHTML += "<button style='display:inline;' type='button' class='btn btn-danger'>Not Suitable</button>"
    }else{
        document.getElementById("novCrews").innerHTML += "<button type='button' class='btn btn-success'>Suitable</button>"
    }

}).catch(function(error){
    console.log(error)
})

