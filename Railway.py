

rail = [

    [
        r"hi|hello|hey",
        ["hey there. \nWhat is your name?"]
    ],

    [
        r"my name is (.*)",
        [
         "Welcome to TRAVELLERA AIR %1"
         "Please provide your mobile number : ",
        ]

    ],

    [
        r"my number is (.*)",
        ["Thank you for your co operation!"
         "10% discount voucher code send to your number :) ",
        ]

    ],

    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],

    [
        r"great|awesome",
        [
         "Good to hear that!\n"
         "How may i help you?"
        ]
    ],


    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],

    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],

    [
        r"help (.*)",
        ["Fetching help...Please wait.\n"
         "Select your choice :\n"
         "1) Get Train schedule to (Enter_location)\t"
         "2) View suggested Locations\t"
         "3) Quit\t",
        ]

    ],

    [
        r"train from (.*)",
        ["Railway timings :\n"
         "FROM          TO          TRAIN NAME              BOARDING TIME   ARRIVAL TIME\n"
         "%1        Delhi       Rajdhani Express        17:00 hrs       6:00 hrs\n"
         "%1        Kolkata     Doranto Express		    15:00 hrs       3:00 hrs\n"
         "%1        Banglore    Superfast Express       11:00 hrs       5:00 hrs\n"
         "%1        Pune        Sinhagad Express        06:00 hrs       9:00 hrs\n",
        ]
    ],

    [
        r"train to (.*)",
        ["Railway timings :\n"
         "FROM          TO          TRAIN NAME              BOARDING TIME   ARRIVAL TIME\n"
         "Delhi        %1       Rajdhani Express        17:00 hrs       6:00 hrs\n"
         "Kolkata      %1       Doranto Express		    15:00 hrs       3:00 hrs\n"
         "Banglore     %1       Superfast Express       11:00 hrs       5:00 hrs\n"
         "Pune         %1       Sinhagad Express        06:00 hrs       9:00 hrs\n",
        ]
    ],

    [
        r"suggested (.*)",
        ["1) Mumbai \n 2)Delhi \n 3)Banglore \n 4)Kolkata", ]
    ],

    [
        r'thanks',
        ["You are welcome.",]
    ],

    [
        r"not getting you",
        [
         "Getting help.    Please wait..."
         "Select your choice :"
         "1) Get Train schedule to (Enter_location)"
         "2) View suggested Locations"
         "3) Quit",
        ]
    ],

    [
        r"mumbai",
        ["Places ti visit in Mumbai :"
         "1) Gate way of India \t"
         "2) Sanjay Gandhi National Park \n"
         "3) Red Carpet Wax Museum \t"
         "4) Elephanta Caves \n"
         "5) Chhatrapathi Shivaji Terminus (CST) \t"
         "6) Marine Drive \n",
         ]
    ],

    [
        r"banglore",
        ["Places to visit in Banglore :\n"
         "1) Lalbagh Botanical Garden\t"
         "2) Cubbon Park\n"
         "3) Bangalore Palace\t"
         "4) Bannerghatta Biological Park\n"
         "5) Tipu Sultan's Summer Palace\t"
         "6) Vidhana Soudha\n",
        ]

    ],

    [
        r'delhi',
        ["Places to visit in Delhi :\n"
         "1) Red Fort\t"
         "2) Qutubminar\n"
         "3) Lotus temple\t"
         "4) India Gate\n"
         "5) Swaminarayan Akshardham \t"
         "6) Jama Masjid\n",
        ]
    ],

    [
        r'kolkata',
        ["Places to visit in Banglore :\n"
         "1) Howrah Bridge\t"
         "2) Jorasanko Thakurbari\n"
         "3) Park Street\t"
         "4) Indian Museum\n"
         "5) Victoria Memorial\t"
         "6) Birla Temple\n",
        ]
    ],

    [
        r"(.*)",
        ["Sorry couldn't process it. How may i help you?",]

    ],

    [
        r"quit",
        ["Have a great journey!! \nDo visit again :)",]
    ]

]