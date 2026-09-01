import crypt

max_attempts = 3     
attempt = 0          
stored_pw_hash = 'aa0GPiClW35DQ'
entered_pw = 'aa0GPiClW35DQ'

entered_pw_hash = crypt.crypt(input('pass: '), stored_pw_hash)



try:

     while attempt < max_attempts:

        uname = input('Username: ')  
        entered_pw_hash = crypt.crypt(input('pass: '), stored_pw_hash)

        if uname == 'admin' and entered_pw_hash == stored_pw_hash:
            print('Welcome Admin')
            break
        else:
            attempt += 1
            if attempt == max_attempts:
                raise RuntimeError("\nYou've reached the maximum number of attempts allowed.")

            else:
                print('Wrong credentials.\n Try again or press <ctrl+c> to exit.\n')
                continue


except KeyboardInterrupt:
    print('Terminated by the user.\nGood-bye.')

except RuntimeError as e:
    print("Goodbye")