# ASCII-Image-Converter


## Description

Convert any image of any format to ASCII image in .txt format (in addition it allows to compress the file in some way).


## Features

- WIDTH : the width (in characters) of the output image, the height is then calculated with the image ratio
- ASCII : a predefined string that ranks the characters from lightest to darkest
- PATH : the path to the image you want to convert
- OUTPUT : the path to the output image


## Dependencies

- PIL / Pillow library


## Example

Here is an example of an image that can be converted (here in .png format).

![example](assets/example.png)


Then here is the result that we obtain with this program.

                                                                                                                                                      
                                                                                                                                                      
                                                po######*******ooooooaaaahhhhhhkkkkkkbdqX{          UOqqqqwwwwwmmmmmmZZZZOOOOOO000000QQQQQQLY/_       
                                               dB$dwwwwwwwwwwwqqqqqqqqqqqqqqqqqqqqqqqq#%kc|        ndWappppppppppppdddddddddddddddddddddddbkbCf       
                                              q%$mcczzzzzzzXXXXXXYYYYYYYUUUUUUUJJJJJUq8#Ln1        d&a0Q0000000OOOOOOZZZZZZmmmmmmmwwwwwwwqbkOz\       
                                             O&$pczzzzzXXXXXXYYYYYYYYUUUUUUUJJJJJJJJw8WQn)        p8*0Q00000000OOOOOOOOZZZZZZmmmmmmmwwwwwbhmX\        
                                            0#$dcczzzzzzzXXXXXXXYYYYYYYUUUUUUUUJJJUZ%8Ou)        p8MOLQQQQQ0000000OOOOOOOOOZZZZZmmmmmmmmbawYt         
                                           qa@kccccczzzzzzzzXXXXXXYYYYYYYYUUUUUUUU08Bmv(        w8&ZCLLLQQQQQQ00000000OOOOOOOOZZZZZZmmmbodUf          
                                           bBacvcccccczzzzzzzzXXXXXXYYYYYYYYUUUUYL&$pc\        q8%wCLLLLLLLQQQQQQ000000000OOOOOOOOZZZZd*kJr_          
                                          p8ozvccccccccczzzzzzzzXXXXXXXYYYYYYYYYJW$kz\        w8$pJCCCLLLLLLLLLQQQQQQ00000000OOOOOOOOp#aCx{           
                                         mW*YuvvvvcccccccczzzzzzzzzXXXXXXYYYYYYU*$oYt        p&$bJCCCCCCCCLLLLLLLLQQQQQQQ00000000OO0qM*Qn)            
                                        O#*UnvvvvvvvvcccccccczzzzzzzzzXXXXXXYXXh$*Uf        qW$aUJJJJCCCCCCCCLLLLLLLLLQQQQQQ0000000wMMOu)             
                                       Co#JnuuuuvvvvvvvccccccccczzzzzzzzzXXXXzp@MJj)       qM$*UUJJJJJJJCCCCCCCCCLLLLLLLLLQQQQQQ0QZM&mc|              
                                      Ch#Lnuuuuuuuvvvvvvvccccccccczzzzzzzzzzzm%MLr(        a$MJUUUUUUJJJJJJCCCCCCCCCCLLLLLLLLLQQLOM%qz|               
                                     Ud*0nnnuuuuuuuuvvvvvvvvccccccccczzzzzzc08WQn|        k$WCYUUUUUUUUUUJJJJJJCCCCCCCCCCLLLLLLLQ#BbX/                
                                    QqoOxnnnnnuuuuuuuuuvvvvvvvcccccccccczzcCMWOu(        p%&LXYYYYYUUUUUUUUUJJJJJJJJCCCCCCCCLLCL*@aYt                 
                                   qZaZnxnnnnnnnuuuuuuuuuuuvvvvvvcccccccccU*WZc(        m8&QzYYYYYYYYYUUUUUUUUUUJJJJJJJCCCCCCCCa$*Uf                  
                                   QhmnxxnnnnnnnnnnuuuuuuuuuuvvvvvvvvcccvXhMwz|        OM&0zXXXXYYYYYYYYYYUUUUUUUUUUUJJJJJJCCJk$WCrn                  
                                  CbwurxxxxxnnnnnnnnnnuuuuuuuuuuvvvvvvvvzbMqXf qqq    Q*8ZczzXXXXXXXYYYYYYYYYYUUUUUUUUUUUJJJUp$%Lx/                   
                                 Ypwurxxxxxxxxnnnnnnnnnnuuuuuuuuuuuvvvvvmahddddddbhqjxh&mczzzzzzXXXXXXXXYYYYYYYYYYYUUUUUUUUYm@%0n|                    
                                zqqvjrrrrxxxxxxxnnnnnnnnnnnnuuuuuuuuuuvvzczzzXXXzwMhJdWqcczzzzzzzzzzXXXXXXXXYYYYYYYYYYYUUUY0%BZu(                     
                               vmwzjrrrrrrrxxxxxxxxxnnnnnnnnnnnuuuuuuuuuuuuuuvvuQokJq#pcccccczzzzzzzzzzzzXXXXXXXXYYYYYYYYYLWBwv|                      
                              x0wzjrrrrrrrrrrrxxxxxxxxxnnnnnnnnnnnuuuuuuuuuuuuuCahCZ*dcvcccccccccczzzzzzzzzzzXXXXXXXXXYYXJ*%pz\                       
                             nLwYfjjjrrrrrrrrrrrrrxxxxxxxxnnnnnnnnnnnnuuuuuuunYkhL0adzuvvvccccccccccccczzzzzzzzzzzXXXXXXYa%dX/                        
                            rUmYfjjjjjjjjrrrrrrrrrrrrxxxxxxxxxnnnnnnnnnnnnuunzdkLLhbXuvvvvvvvvvcccccccccccczzzzzzzzzzzzXb8kYt                         
                           qzOUfffjjjjjjjjjjrrrrrrrrrrrrxxxxxxxxxnnnnnnnnnnnvqk0CbbYnuuuuuvvvvvvvvvvccccccccccczzzzzzzcqWhUf                          
                           v0JjfffffffjjjjjjjjrrrrrrrrrrrrrrxxxxxxxxxnnnnnnuZbOUpdUnuuuuuuuuuuuvvvvvvvvvccccccccccccccZMhJr(                          
                          xQJjtffffffffffjjjjjjjjjrrrrrrrrrrrrrrxxxxxxxxxxn0dOUwdJxnnnnuuuuuuuuuuuuuvvvvvvvvvvccccccvQ*aLx(                           
                         jCJrtfffffffffffffjjjjjjjjjjrrrrrrrrrrrrrrrxxxxxxCpZUmpCxnnnnnnnnnnuuuuuuuuuuuuuuvvvvvvvvvuCoaQn1                            
                        fCCrttttfffffffffffffffjjjjjjjjjjrrrrrrrrrrrrrrrrUwZUOqLxxxnnnnnnnnnnnnnuuuuuuuuuuuuuuuvvvuYka0v(                             
                       fCLn/ttttttttfffffffffffffffjjjjjjjjjjrrrrrrrrrrrXmZUQwLxxxxxxxxxnnnnnnnnnnnnnnuuuuuuuuuuuuzdhOc|                              
                      jC0u/tttttttttttttfffffffffffffffjjjjjjjjjjjjjjjjcZOULmQxrrrxxxxxxxxxxxnnnnnnnnnnnnnnnnuuunvqhZz\                               
                     jJOc///tttttttttttttttfffffffffffffffffuUUUJJJJJJC0OJJZQnrrrrrrrrrxxxxxxxxxxxxnnnnnnnnnnnnnumkmX/                                
                    tUmX///////ttttttttttttttttffffffffffffxCLCXvvcccccvxzOQnjrrrrrrrrrrrrrrrxxxxxxxxxxxxxnnnnnn0bmYt                                 
                    UwJ/\/////////tttttttttttttttttttfffftrUCJz|        rLQufjjjjjrrrrrrrrrrrrrrrrrxxxxxxxxxxxxCdmUj                                  
                   YqLt\\///////////////tttttttttttttttttfYCJX\        tCQufjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrrxxrUqmJr[                                  
                  YqOf\\\\\\\\/////////////tttttttttttttfYLJY/        \YLvffffffjjjjjjjjjjjjjjjrrrrrrrrrrrrrrzwmJn}                                   
                 Xpmj|\\\\\\\\\\\\/////////////tttttttttXQCYf        \zLctffffffffffffffjjjjjjjjjjjjjjjrrrrjvZZCu(                                    
                Xppx|\\\\\\\\\\\\\\\\\/////////////////z0LUj        (zQztttfffffffffffffffffffffjjjjjjjjjjjn0ZCc|                                     
               zpbu(|\\\\\\\\\\\\\\\\\\\\\\//////////\cOQUr(        c0YtttttttttttffffffffffffffffffffffffxLOCz|                                      
              zqhz(|||||||\\\\\\\\\\\\\\\\\\\\\\\///\uZOJn1        cOJf/ttttttttttttttttttfffffffffffffffjC0CX\                                       
             YqoU(||||||||||||||\\\\\\\\\\\\\\\\\\\|nmZCu1        vOLf///tttttttttttttttttttttttttfffffffYQCYt                                        
            Jq*L(||||||||||||||||||||\\\\\\\\\\\\\|rZwLc(        uZ0r\////////////ttttttttttttttttttttttzLCYf                                         
            w#Z|(|||||||||||||||||||||||||\\\\\\\|fZqQz|        nZZx\\\\////////////////////tttttttttt/vCJUj                                          
           mMp\)(((((||||||||||||||||||||||||||||/Od0z\        nZwu|\\\\\\\\\\\///////////////////////uCCUx(                                          
          mMkt)(((((((((((||||||||||||||||||||||\0bZX/        nZpc|\\\\\\\\\\\\\\\\\\\\\\\\/////////\nLLUn1                                           
         ZMoj)(((((((((((((((((((((|||||||||||||LkmYf        nObY|||||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\rQQJv(                                            
        ZMMn1((((((((((((((((((((((((((((||||((JhqUj        fOkC||||||||||||||||||\\\\\\\\\\\\\\\\|fQ0Cc)                                             
       ZM&c{)))))))))))))))))))))))))))))(((()XadJr[        0h0|(((((|||||||||||||||||||||||||||||tLZLz|                                              
      0MB0\/tttttttttttttttt/ttttttttttttttt/zohLn(        Qaqj/tttttttttttttttttttttttttttttttt/tLmQX\                                               
      ZdohhhhhhhhhhhhkkkkkkkkkbbbbbbbddddddddkdCn1         JqqwwwwwwwwwwmmmmmmmmZZZZZZZZOOOOOOOO0OZLzt                                                
        (fffffffffffffffffffffffffffffffffffft\)(           [/fffffffffffffffffffffffffffffffffffft|)                                                 
                                                                                                                                                      
                                                                                                                                                      
