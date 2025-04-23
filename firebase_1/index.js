const auth = firebase.auth();

function signUp(){
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById(signup-password).value;

    auth.createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            console.log("YAY IT WORKED", user);
            alert("YAY IT WORKED");
        })
        .catch((error) => {
            console.error("You couldn't do it...", error.message);
            alert("at least the code works", error.message)
        });
}