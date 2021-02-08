class Locator:
    
    #username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]'
   # password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    #login_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button'

    username = '//android.widget.EditText[@index="1"]'
    password = '//android.widget.EditText[@index="2"]'
    #login = '//*[contains(text(),"Login")]'
    
    auth_login = 'dev.ankitkumar.kotlinlogin:id/auth_button'
    auth_login2 = 'dev.ankitkumar.kotlinlogin:id/auth_button'
    email_button = 'dev.ankitkumar.kotlinlogin:id/email_button'
    email = 'dev.ankitkumar.kotlinlogin:id/email'
    button_next = 'dev.ankitkumar.kotlinlogin:id/button_next'
    password = 'dev.ankitkumar.kotlinlogin:id/password'
    signin = 'dev.ankitkumar.kotlinlogin:id/button_done'