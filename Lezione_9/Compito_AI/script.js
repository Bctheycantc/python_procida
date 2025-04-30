const form = document.getElementById('form-registrazione');
const messaggio = document.getElementById('messaggio');

if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault(); // evita il refresh della pagina

    const nome = document.getElementById('nome');
    const cognome = document.getElementById('cognome');
    const dataNascita = document.getElementById('dataNascita');
    const email = document.getElementById('email');
    const corso = document.getElementById('corso');

    // Validazione più affidabile
    if (
      nome.value.trim() === "" ||
      cognome.value.trim() === "" ||
      dataNascita.value === "" ||
      email.value.trim() === "" ||
      corso.selectedIndex === 0 // verifica che non sia ancora la prima voce "-- Seleziona un corso --"
    ) {
      messaggio.textContent = "Compila tutti i campi!";
      messaggio.style.color = "red";
      return;
    }

    const studente = {
      nome: nome.value.trim(),
      cognome: cognome.value.trim(),
      dataNascita: dataNascita.value,
      email: email.value.trim(),
      corso: corso.value
    };

    // Recupera o inizializza l'array degli studenti
    const studenti = JSON.parse(localStorage.getItem('studenti')) || [];
    studenti.push(studente);
    localStorage.setItem('studenti', JSON.stringify(studenti));

    messaggio.textContent = "Registrazione completata!";
    messaggio.style.color = "green";
    
    setTimeout(() => {
      messaggio.textContent = "";
    }, 3000);
    
    form.reset(); // svuota il form
  });
}
  
    // Pagina HOME
    const listaStudenti = document.getElementById('lista-studenti');

    if (listaStudenti) {
      const studenti = JSON.parse(localStorage.getItem('studenti')) || [];
    
      studenti.forEach((studente, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
          ${studente.nome} ${studente.cognome} - ${studente.email} (${studente.corso})
          <span class="delete" data-index="${index}">&times;</span>
        `;
        listaStudenti.appendChild(li);
      });
    
      // Gestione click su X per eliminare
      document.querySelectorAll('.delete').forEach(btn => {
        btn.addEventListener('click', e => {
          const index = e.target.getAttribute('data-index');
          studenti.splice(index, 1);
          localStorage.setItem('studenti', JSON.stringify(studenti));
          location.reload(); // ricarica la lista
        });
      });
    }
    

      function mostraStudenti() {
        const listaStudenti = document.getElementById('lista-studenti');
        if (!listaStudenti) return; // evita errori se non siamo nella pagina giusta
      
        listaStudenti.innerHTML = ''; // svuota prima
      
        const studenti = JSON.parse(localStorage.getItem('studenti')) || [];
      
        studenti.forEach((studente, index) => {
          const li = document.createElement('li');
          li.innerHTML = `
          <strong>${studente.nome} ${studente.cognome}</strong><br>
          Email: ${studente.email}<br>
          Data di nascita: ${studente.dataNascita}<br>
          Corso: ${studente.corso}
          <span class="delete" data-index="${index}" style="margin-left:10px; color:red; cursor:pointer;">✖</span>
        `;
        
      
          // Aggiungi bottone di rimozione
          const btnRimuovi = document.createElement('span');
          btnRimuovi.textContent = ' ✖';
          btnRimuovi.style.cursor = 'pointer';
          btnRimuovi.style.color = 'red';
          btnRimuovi.style.marginLeft = '10px';
      
          btnRimuovi.addEventListener('click', () => {
            studenti.splice(index, 1);
            localStorage.setItem('studenti', JSON.stringify(studenti));
            mostraStudenti(); // ricarica la lista
          });
      
          li.appendChild(btnRimuovi);
          listaStudenti.appendChild(li);
        });
      }
      
      document.addEventListener('DOMContentLoaded', () => {
        const listaStudenti = document.getElementById('lista-studenti');
        if (listaStudenti) mostraStudenti();
      });
      
      