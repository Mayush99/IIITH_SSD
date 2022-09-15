function dragstartHandler(evt){
    evt.dataTransfer.setData("DragElement", evt.target.id);
}

function dragoverHandler(evt){
    evt.preventDefault();
}

function dropHandler(evt){
    evt.preventDefault();
    var elementId = evt.dataTransfer.getData("DragElement");
    evt.target.appendChild(document.getElementById(elementId));
}

function validate(){
    var mname = document.getElementById("mname");
    var tl = document.getElementById("tl");
    var gemail = document.getElementById("gemail");
    var usr = document.getElementById("usr");
    var pswd = document.getElementById("pswd");
    var cnf = document.getElementById("cnf");
    if(pswd==cnf) alert("Name:"+ mname +"\n" +"Email:"+ gemail +"\n"+"Username:"+ usr +"\n"+"Team Lead: "+tl +"\n"+ "Team members: ");
    else alert("From details invalid");
}