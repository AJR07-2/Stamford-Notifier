let firebaseConfig = {
    apiKey: "AIzaSyDbj7Rz5vPAONiVUVa3OsS_0uiNoc4fcbI",
    authDomain: "stamford-notifier.firebaseapp.com",
    projectId: "stamford-notifier",
    storageBucket: "stamford-notifier.appspot.com",
    messagingSenderId: "778420216028",
    appId: "1:778420216028:web:81e349e2984bd8a2d19419",
    measurementId: "G-FJDDZ2EBSM"
  };
firebase.initializeApp(firebaseConfig);
let email;
function setup() {
    nameV = document.getElementById('email').value;
}

document.getElementById('save').onclick = function () {
    setup();
    console.log("Lol")
    firebase.database().ref('users/' + email).set({
        user_Email: email
    });
}