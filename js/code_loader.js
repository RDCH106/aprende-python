function getParameterByName(name, url) {
    if (!url) { url = window.location.href; }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) { return null; }
    if (!results[2]) { return ""; }
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function load(url)
{
    req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send(null);

    return req.responseText; 
}

function getCodeSource(){
    var source_code = getParameterByName('code_source');
    if(source_code != null){
        return load(source_code);
    }else{
        return null;
    }        
}