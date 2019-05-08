// https://stackoverflow.com/a/901144/9739532
function getParameterByName(name, url) {
    if (!url) { url = window.location.href; }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) { return null; }
    if (!results[2]) { return ""; }
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

// https://stackoverflow.com/a/17901198/9739532
function load(url)
{
    req = new XMLHttpRequest();
    req.open("GET", url, true);
    // https://developer.mozilla.org/es/docs/Web/API/XMLHttpRequest/Synchronous_and_Asynchronous_Requests
    req.onload = function (e) {
        if (req.readyState === 4) {
            if (req.status === 200) {
                //alert(req.responseText);
                window.ace.edit("editor").setValue(req.responseText, 1);  // https://stackoverflow.com/a/18629202
            } else {
                alert("Code Source: " + url + "\n\n" + req.statusText);
            }
        }
    };
    req.send(null);
}

function getCodeSource(){
    var source_code = getParameterByName('code_source');
    if(source_code != null){
        load(source_code);    
    }       
}