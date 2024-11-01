from reportlab.platypus import TableStyle
from reportlab.lib import colors

style = TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1,  colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 8 ), 1,  colors.black ), 
        ( "BACKGROUND" , ( 0 , 0 ), ( 4, 8 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 8 ), colors.whitesmoke ),
        ( "TEXTCOLOR" , ( 1, 1 ), ( 3, 8 ), colors.black ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "LEFT" ),
        ( "BACKGROUND" , ( 1 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
) 