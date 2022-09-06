document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Make the button on compose working
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  // Add this to not display the email details
  document.querySelector('#email-detail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

}

// Third part: read the email and its details
function open_email(id){
  // You’ll likely want to make a GET request to /emails/<email_id> to request the email.
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    // Print email
    //console.log(email);
    
    // show email detail and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-detail-view').style.display = 'block';
  
    // If we use createElement, it will amount divs every time we go back

    // display email details
    document.querySelector('#email-detail-view').innerHTML = `
      <ul class="list-group">
        <li class="list-group-item"><b>From:</b> <span>${email['sender']}</span></li>
        <li class="list-group-item"><b>To: </b><span>${email['recipients']}</span></li>
        <li class="list-group-item"><b>Subject:</b> <span>${email['subject']}</span</li>
        <li class="list-group-item"><b>Time:</b> <span>${email['timestamp']}</span></li>
        <li class="list-group-item"><br/>${email['body']}</li>
      </ul>
    `;

    // Once the email has been clicked on, you should mark the email as read. 
    if (!email['read']) {
      fetch('/emails/' + email['id'], {
        method: 'PUT',
        body: JSON.stringify({ read : true })
      })
    }

    // Allow users to reply to an email.
    const reply = document.createElement('button');
    reply.className = "btn btn-primary m-2";
    reply.innerHTML = "Reply";
    reply.addEventListener('click', function() {
      compose_email();

      // populate fields with information from email
      document.querySelector('#compose-recipients').value = email['sender'];
      let subject = email['subject'];
      //console.log(subject.split(" ", 1)[0]);
      if (subject.split(" ", 1)[0] != "Re:") {
        subject = "Re: " + subject;
      }
      document.querySelector('#compose-subject').value = subject;

      let body = `
        On ${email['timestamp']}, ${email['sender']} wrote: ${email['body']}
      `;
      document.querySelector('#compose-body').value = body;

    });

    document.querySelector('#email-detail-view').appendChild(reply);

    //  Allow users to archive and unarchive emails that they have received.
    archiveButton = document.createElement('button');
    archiveButton.className = "btn btn-secondary m-1";
    archiveButton.innerHTML = !email['archived'] ? 'Archive' : 'Unarchive';
    archiveButton.addEventListener('click', function() {
      fetch('/emails/' + email['id'], {
        method: 'PUT',
        body: JSON.stringify({ archived : !email['archived'] })
      })
      .then(response => load_mailbox('inbox'))
    });
    document.querySelector('#email-detail-view').appendChild(archiveButton);
  })
  // Catch any errors and log them to the console
  .catch(error => {
    console.log('Error:', error);
  });
}

// Second part: Fixing load_mailbox function
function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  // Add this to not display the email details
  document.querySelector('#email-detail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // You’ll likely want to make a GET request to /emails/<mailbox> to request the emails for a particular mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Loop through all the emails in that mailbox
      emails.forEach(email => {

        // Create new div
        let new_email_div = document.createElement('div');

        // Check if it is read or not
        new_email_div.className = email['read'] ? "email-box-not-read" : "email-box-read"
        
        // Add sender, subject and timestamp in div
        new_email_div.innerHTML = `
          <span class="sender-email"> <strong>${email['sender']}</strong> </span>
          <span class="subject-email"> ${email['subject']} </span>
          <span class="timestamp-email"> ${email['timestamp']} </span>
        `

        // Logic of opening the details of the email
        new_email_div.addEventListener('click', () => open_email(email['id']));

        // Add new email in the following ones
        document.querySelector('#emails-view').appendChild(new_email_div);
      });

  })
  // Catch any errors and log them to the console
  .catch(error => {
    console.log('Error:', error);
  });

}

// First part: Send Email
function send_email(event){
  //Modifies the default beheavor so it doesn't reload the page after submitting.
  event.preventDefault();

  // You’ll likely want to make a POST request to /emails, passing in values for recipients, subject, and body.
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
  })
  // Catch any errors and log them to the console
  .catch(error => {
    console.log('Error:', error);
  });

  // Once the email has been sent, load the user’s sent mailbox.
  load_mailbox('sent');
}
