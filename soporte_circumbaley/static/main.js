function hola(){
var send=document.getElementById("send");
                        send.addEventListener("click",function(){
                            var content = encodeURIComponent(document.getElementById("content").value);
                            if (content.length > 0){
                                document.getElementById("content").value = '';
                                const url = "{% url 'messenger:add' thread.pk %}" + "?content="+content;
                                fetch(url,{'credentials':'include'}).then(response => response.json()).then(function(data){
                                if (data.created) {
                                var message = document.createElement('div');
                                message.classList.add('mine','mb-3');
                                message.innerHTML = '<small><i>Hace Unos Segundos</i></small><br>'+decodeURIComponent(content);
                                document.getElementById("thread").appendChild(message);
                                ScrollBottomInThread();
                                } else {
                                // Si algo ha ido mal podemos debugear en la consola del inspector
                                console.log("Algo ha fallado y el mensaje no se ha podido añadir.")
                                }})
                            }
                        })
}