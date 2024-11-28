# left = L, right = R, top = T, bottom = B, main = X, topleft = W, topright = D, bottomleft = A, bottomright = S, insidetopleft = Q, insidetopright = E, insidebottomright = Y, insidebottomleft = U, grass = M, e = enemy, s = captured soul


# each level is designated a dictionary containing 3 values: the level layout containing values assigned to a type of tileset. An enemy speed and the distance an enemy travels
level1 = {'level_map':[
'                              ',
'              e               ',
'                              ',
' MsM       M  M               ',
' WTTD      WTTD               ',
' LXXETD           M M  WD     ',
' LYBBBS       MsM WTD       d ',
' AS           WTTTQXR      WTT',
'           M  ABBBBBS         ',
'      M  WTD            WD    ',
' P    WTTQXR        M WTQR    ',
'M  M                WTQYBS    ',
'TTTD                ABBS      ',
'        M sM WTTD             ',
'       WTTTTTQXXR             ',
'       LXXXXXXXXR             ',
'       LXXXXXXXXR             ',
], 'enemy_speed': 3,'enemy_dist': 250}

level2 = {'level_map':[
'XXXXR                         ',
'XXXYS             e           ',
'XYBS                          ',
'BS        M    M s    M       ',
'          WTTTTTTTTTTTTD      ',
'     M                      M ',
'     WD      e             WTT',
'    WQR                   WQXX',
'                      M       ',
'TD                   WD       ',
'      M           s         d ',
'    WTD          WD       WTTT',
'   P       M                  ',
' M        WTTD        WD      ',
'TTTTD                     M s ',
'XXXXETD                M  WTTT',
'XXXXXXR                WTTQXXX',
'XXXXXXR                LXXXXXX'
], 'enemy_speed': 2,'enemy_dist': 125}

level3 = {'level_map':[
'                              ',
'                    e         ',
'                              ', 
'                              ',
'  P    s                    s ',
'TTD    T              WTTTTTTT',
'                      ABBUXXXX',
'           WTTTTTD       ABBBB',
'                              ',
'    WTD                       ',
'    AUR                       ',
'D    AS                       ',
'ED                            ',
'XR s                   WD     ',
'XETD    s              LR   d ',
'XXXR   WD      e       LETTTTT',
'XXXR   LR              LXXXXXX',
], 'enemy_speed': 4,'enemy_dist': 125}


tile_size = 48
win_width, win_height = 1400, 800 

yo = 6

print(f'hello {yo}')