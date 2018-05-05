
const BASE_URL = "http://localhost:5000/api/"

$(document).ready(function () {
  loadContacts();

  $('#createContact').click(createContact);
});


function loadContacts() {
  $.ajax({
    url: BASE_URL + "contacts",
    type: "GET",
    success: function (response) {
      $.each(response.contacts, function (_, contact) {
        addContact(contact)
      });
    }
  });
}


function addContact(contact) {
  contactHtml = `<tr id=${contact.id}>'\
                  '<td><button class="sendMessage button button-clear">Send</button></td>'\
                  '<td>${contact.first_name}</td>'\
                  '<td>${contact.last_name}</td>'\
                  '<td>${contact.number}</td>'\
                  '<td><button class="removeContact button button-clear">Remove</button></td>'\
                </tr>`
  $('#contactList').append(contactHtml);
  const addedContact = $('#contactList').children().last()
  addedContact.on('click', '.removeContact', removeContact);
  addedContact.on('click', '.sendMessage', sendMessage);
}


function createContact() {
    const payload = {
      first_name: $("#firstNameField").val(),
      last_name: $("#lastNameField").val(),
      number: $("#phoneField").val()
    };

    $.ajax({
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(payload),
      method: "POST",
      url: BASE_URL + "contacts",
      success: function (response) {
        addContact(response.contact);
      },
      error: function (response) {
        alert(response.error);
      },
    });
}


function removeContact() {
  const contact_row = $(this).closest('tr');

  $.ajax({
    method: "DELETE",
    url: BASE_URL + `contacts/${contact_row.attr('id')}`,
    success: function (response) {
      contact_row.remove()
    },
    error: function (response) {}
  });
}


function sendMessage() {
  const contact_row = $(this).closest('tr');

  $.ajax({
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({
      message: $("#messageField").val()
    }),
    method: "POST",
    url: BASE_URL + `contacts/${contact_row.attr('id')}/sms`,
    success: function (response) {
      alert('Message Sent!');
    },
    error: function (response) {
      alert(response.error);
    },
  });
}
