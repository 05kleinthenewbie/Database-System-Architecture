const API_URL = "http://127.0.0.1:5000/notes";

async function fetchNotes() {
    const response = await fetch(API_URL);
    const notes = await response.json();
    const noteList = document.getElementById("note-list");
    noteList.innerHTML = "";
    notes.forEach(note => {
        const li = document.createElement("li");
        li.textContent = `${note.title}: ${note.content}`;
        noteList.appendChild(li);
    });
}

async function addNote() {
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content })
    });

    if (response.ok) {
        fetchNotes();
    } else {
        alert("Failed to add note");
    }
}

window.onload = fetchNotes;
