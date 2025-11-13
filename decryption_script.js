var CryptoJS = require('crypto-js.js');

var secret_key = "<secret_key_revealed_at_client_side>";
var username = "<encrypted_username_in_request";
var password = "<encrypted_password_in_request";

console.log('Decrypting the username and password');


	function decrypt_credentials(username,password){
		
		var login_credentials = ();
		
		var key = secret_key;
		var iv = iv;
		
		var decrypted_username = CryptoJS.AES.decrypt(username,key,
			
			{
				
				iv:iv;
				
			});
			
		console.log(decrypted_username.toString(CryptoJS.enc.Utf8));
		
		var decrypted_password = CryptoJS.AES.decrypt(password,key,
			
			{
				
				iv:iv;
				
			});
			
		console.log(decrypted_password.toString(CryptoJS.enc.Utf8));
		
		
		logincredentials.username = decrypted_username;
		logincredentials.password = decrypted_password;
		
		return logincredentials;
		
		
	}
	
	
console.log(decrypt_credentials(username,password));

