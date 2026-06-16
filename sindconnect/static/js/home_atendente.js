function atualizarDataHora() {
    const data = new Date();

    const opcoesData = {
        day: "2-digit",
        month: "long",
        year: "numeric"
    };

    const opcoesHora = {
        weekday: "long",
        hour: "2-digit",
        minute: "2-digit"
    };

    document.getElementById("dataAtual").innerText =
        data.toLocaleDateString("pt-BR", opcoesData);

    document.getElementById("horaAtual").innerText =
        data.toLocaleDateString("pt-BR", opcoesHora);
}

function toggleSidebar() {
    const sidebar = document.querySelector(".sidebar");
    sidebar.classList.toggle("show");
}

atualizarDataHora();
setInterval(atualizarDataHora, 60000);