function atualizarDataHora() {
    const agora = new Date();

    const dataFormatada = agora.toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "long",
        year: "numeric"
    });

    const horaFormatada = agora.toLocaleDateString("pt-BR", {
        weekday: "long",
        hour: "2-digit",
        minute: "2-digit"
    });

    document.getElementById("dataAtual").innerText = dataFormatada;
    document.getElementById("horaAtual").innerText = horaFormatada;
}

function toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("show");
}

atualizarDataHora();
setInterval(atualizarDataHora, 60000);