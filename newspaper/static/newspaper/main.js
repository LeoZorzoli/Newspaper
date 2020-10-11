var x = window.matchMedia("(max-width: 1024px)")

function mostrar() {
    function querie(x){
        let sidebar = document.getElementById('sidebar')
        if (x.matches){
            sidebar.style.width = "100%";
        }
        else{
            sidebar.style.width = "280px";
            sidebar.classList.add('abierto')
        }
    }

    querie(x)
    x.addListener(querie)
}

function ocultar() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("contenido").style.marginLeft = "0";
    sidebar.classList.remove('abierto')
}

function querie(x){
    if (x.matches){
        document.getElementById("sidebar").style.width = "100%";
    }
}

window.addEventListener('click', function(e){   
    let sidebar = document.getElementById('sidebar')
    let abierto = sidebar.classList.contains('abierto')
    let adentro = sidebar.contains(e.target)
    let abrir = document.getElementById('contenido')
    let clickMenu = abrir.contains(e.target)
    
    if(abierto){
        if(adentro === true){
            return
        }if(adentro === false && clickMenu === false){
            ocultar()
            sidebar.classList.remove('abierto')
        }
    }
});