// Sample data for demonstration
const appointments = [
    { id: 1, date: '2024-03-25', time: '10:00 AM', description: 'Meeting with client' },
    { id: 2, date: '2024-03-26', time: '2:00 PM', description: 'Review project progress' }
];

// Function to render appointments list
function renderAppointments() {
    const appointmentsList = document.getElementById('appointmentsList');
    appointmentsList.innerHTML = '';
    appointments.forEach(appointment => {
        const li = document.createElement('li');
        li.textContent = `${appointment.date}, ${appointment.time}: ${appointment.description}`;
        appointmentsList.appendChild(li);
    });
}

// Function to handle adding new appointments
function addAppointment() {
    const date = prompt('Enter date (YYYY-MM-DD):');
    const time = prompt('Enter time:');
    const description = prompt('Enter description:');
    const id = appointments.length + 1;
    appointments.push({ id, date, time, description });
    renderAppointments();
}

// Event listener for add appointment button
document.getElementById('addAppointmentBtn').addEventListener('click', addAppointment);

// Function to toggle sidebar visibility
// Function to toggle sidebar visibility
function toggleSidebar() {
    console.log("Toggling sidebar"); // Check if this message appears in the console
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed');
}
// Event listener for hamburger button
document.getElementById('hamburger').addEventListener('click', function(event) {
    toggleSidebar();
    event.stopPropagation(); // Prevent click event from bubbling up
});

// Close sidebar when clicking outside of it
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar.contains(event.target) && !event.target.matches('#hamburger')) {
        sidebar.classList.add('collapsed');
    }
});

// Initial rendering of appointments
renderAppointments();
