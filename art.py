#Art and Animations
import os
import sys
import time
from colorama import Fore, Back, Style, init


header = """
***
 ** **
**   **
**   **         ****
**   **       **   ****
**  **       *   **   **
 **  *      *  **  ***  **
  **  *    *  **     **  *
   ** **  ** **        **
   **   **  **
  *           *
 *             *
*    0     0    *
*   /   @   |   *
*   |__/ |__/   *
  *          *
    **     **
      *****
"""


ani1 = '''
    |}         WhiteRa66it
    ||_
    ( _|
    / }__
   / _/`"`
  {|  )_
    `"""`
'''
ani2 = '''
     |}        WhiteRa66it
     ||_
     ( _|
     / }__
    / _/`"`
   {|  )_
   `"` `"""`
'''
ani3 = '''
      |}       WhiteRa66it
      ||_
      ( _|
      / }__
     / _/`"`
    {|  ) _
    `""``"""`
'''
ani4 = '''
       |}      WhiteRa66it
       ||_
       ( _|
       / }__
      / _/`"`
     {|   )
      `"""`
'''

ani5 = """
                        ..',;::ccccc:;,'.... .
                   .cdk0XNWMMMMMMMMMWWXKOxoc;'....
                  .kWMMMMMMMMMMMMMMMWWWWWWNNXOdc;'...
                 .l0NNNWWWWWWWWWWWWWWNNNNNNNNNNX0dc,''.
                 'd0KXXXXXNXXXNNNNNNNXXXXXXXXXXXKK0x:,,,.
                .cxO000KKKKKKKKKKKKKXXKXKKKKKKKK00OOko,','.
               .;odxkOOO000KNNNXKK000KKK00000O00OOkkkxo,.';.
               .:oodxxxkkk0NMMNKOOOOO000OOOkkkOOxxxxddol'.';.
              .,clooodddxONMMNOxxxkkkOOkkxxxxkkxdddoollc:. .;.
             .';clllloodONMMXkdddddxkxxxddddxkdooolllc::;.  ':.
            ..;:ccccllo0WMWKxooooddxdoooooooxxolcccll:;;,.   ;:.
            .',;::::co0NWN0dloooodxdlllcclldkoc::;:lc,,''.   .c,
           ..',,;;;:oOKXKxlclllodddlc::::cool;;,,,cl;'....   .::.
            ...'',:lxkkdc:::cclool::;;;;coo;'''..;c;.....     ,c.
             ....,:lol:,,,;:cooc;;,,,,;:oo,.....,c;.          ,l,
               ..',,,'..',;:ldc,'''',;:lc..    'll.           ,l,
             ,l:'... ...',;::,......,;:l,     .,;.            ;o,
           ;xNMNd.     .,:;..    ..',:,.    .'::.            .cl'
         .cKWWOc.    ..,,.     ...';;.     .,ol.             ,oc.
          ..;,.    .','.     ..,;;cc.    ..;c,              .co,
                 .'...      .';,'..     .,c:.              .;o:.
  .            ...         ':c,.      .';:,                ;oc.
   ..                    .;,..       .,,.                .;lc.
    ..                 .';'        ..'.                 .:lc.
     .'.            ...          ....                 .,cl;.
      .''.         .                                 ':c:'
        .,,.                                      .':c:'.
          .,;,..,,,,,''..''. .;,,,,'.    ...  .:;;col,.
            ..;dxc,...clloc;':;....''  .','..:dkxc''.
               .';colldo;;;ol;:;;;;oo,:olccloxl'..
                   .',:::cclooxxxxxxoooc:;,...
                         ...',,,;;,,'...
"""

menu_top = """
########################################################
#     #####                                            #
#    #     #  ####  #    # #####  #    # # #####       #
#    #       #    # ##   # #    # #    # #   #         #
#    #       #    # # #  # #    # #    # #   #         #
#    #       #    # #  # # #    # #    # #   #         #
#    #     # #    # #   ## #    # #    # #   #         #
#     #####   ####  #    # #####   ####  #   #         #
########################################################
#+++++++++++++++++By BackS/ash+++++++++++++++++++++++++#
"""


body_contents = """
,------------------------------------------------------.
| |O  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_| |
| |----.),------.),------.),------.),------.),------.| |
| |----' `------' `------' `------' `------' `------'| |
| |                                                  | |
| |                                                  | |
| |                                                  | |
| |                                                  | |
| |  (`-.     (`-.     (`-.     (`-.     (`-.     (`-| |
| | (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO | |
| |,------.),------.),------.),------.),------.),----| |
`-'`------' `------' `------' `------' `------' `----`-'
"""
