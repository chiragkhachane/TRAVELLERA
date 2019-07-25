
road =[

    [
        r"hi|hey|hello",
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
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
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
        [
            "I provide following functionality :"
            "1) Get plane schedule to (Enter_location)"
            "2) View suggested Locations"
            "3) Quit",
        ]

    ],

    [
        r"bus from (.*)",
        ["Railway timings :\n"
         "FROM          TO          BUS NAME              BOARDING TIME   ARRIVAL TIME\n"
         "%1        Delhi           Rajhans               17:00 hrs       6:00 hrs\n"
         "%1        Kolkata         City Link             15:00 hrs       3:00 hrs\n"
         "%1        Banglore        VRL                   11:00 hrs       5:00 hrs\n"
         "%1        Pune            Shivneri              06:00 hrs       9:00 hrs\n",
        ]
    ],

    [
        r"bus to (.*)",
        ["Railway timings :\n"
         "FROM          TO          BUS NAME              BOARDING TIME   ARRIVAL TIME\n"
         "Delhi        %1           Mahalakshmi           17:00 hrs       6:00 hrs\n"
         "Kolkata      %1           Knight Rider 		  15:00 hrs       3:00 hrs\n"
         "Banglore     %1           VRL                   11:00 hrs       5:00 hrs\n"
         "Pune         %1           Benz                  06:00 hrs       9:00 hrs\n",
         ]
    ],

    [
        r"mumbai",
        ["Places ti visit in Mumbai :"
         "1) Gate way of India\t"
         "2) Sanjay Gandhi National Park\n"
         "3) Red Carpet Wax Museum\t"
         "4) Elephanta Caves\n"
         "5) Chhatrapathi Shivaji Terminus (CST)\t"
         "6) Marine Drive\n",
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
        ["Places to visit in Banglore :\n"
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
        ["Sorry couldn't process it. How may i help you?"]

    ],

    [
        r"quit",
        ["Have a great journey!! \nDo visit again :)"]
    ]

]