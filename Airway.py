

air = [

    [
        r"hi|hey|hello",
        [
         "hey there." 
         "What is your name?",
         ]
    ],

    [
        r"my name is (.*)",
        [
         "Welcome to TRAVELLERA AIR %1",
        ]
    ],

    [
        r"my number is (.*)",
        [
         "Thank you for your co operation!",
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
         "How may i help you?",
        ]
    ],

    [
        r"im doing (.*)",
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
        r"flights to (.*)| get plane schedule to (.*)",
        ["Railway timings :\n"
         "FROM          TO          COMPANY         BOARDING TIME   ARRIVAL TIME\n"
         "New York      %1         US Airways         12:21          01:00\n"
         "Dubai         %1         Etihad Airlines    04:00          06:52\n"
         "Berlin        %1         Munich Airlines    20:40          14:45\n"
         "Mumbai        %1         Air India          18:32          17:55\n",
         ]
    ],

    [
        r"flights from  (.*)| get plane schedule to (.*)",
        ["Railway timings :\n"
         "FROM          TO          COMPANY         BOARDING TIME   ARRIVAL TIME\n"
         "%1        New York       US Airways         12:21          01:00\n"
         "%1        Dubai          Etihad Airlines    04:00          06:52\n"
         "%1        Berlin         Munich Airlines    20:40          14:45\n"
         "%1        Mumbai         Air India          18:32          17:55\n",
         ]
    ],

    [
        r"berlin",
        ["Places ti visit in Berlin :"
         "1) Brandenburg Gate\t"
         "2) Reichstag Building\n"
         "3) Museum Island\t"
         "4) East Side Gallery\n"
         "5) Berlin Cathedral Church\t"
         "6) Alexanderplatz\n",
         ]
    ],

    [
        r"new york",
        ["Places to visit in New York :\n"
         "1) Statue of Liberty National Monument\t"
         "2) Central Park\n"
         "3) Empire State Building\t"
         "4) Rockefeller Center\n"
         "5) Brooklyn Bridge\t"
         "6) Times Square\n",
         ]

    ],

    [
        r'dubai',
        ["Places to visit in Dubai :\n"
         "1) Burj Khalifa\t"
         "2) Burj Al Arab Jumeirah\n"
         "3) The Dubai Mall\t"
         "4) Palm Jumeirah\n"
         "5) Palm Islands\t"
         "6) The Dubai Fountain\n",
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
      r"(.*)",
      ["Sorry couldn't process it. How may i help you?",]

    ],

    [
        r"quit",
        ["Have a great journey!! \nDo visit again :)"]
    ]

]