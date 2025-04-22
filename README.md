plan for app:

have a database of skincare items (name, brand, price(gbp), ingredients, link and skin concerns (ex. hydration, cleansing, redness etc)) 
user has a profile in which they input their wants / needs from their skincare (for example, they want a sunscreen thats hydrating but have acne prone skin) and the app finds a product that matches all their wants/needs (ex. finds a hydrating spf suitable for acne prone skin)
the main idea is that the app itself reads the ingredients of items and learns which ingredients are best at what & what people usually like/dont like about a specific ingredient (for example they could dislike the smell, they could have allergies etc)

an example of an interaction with this app would be:
>user fills in their profile, they want an moisturiser that helps protect their skin barrier and hydrated but does not want retinol within the ingredients list.
> the app would then search all moisturisers in the database
> find all moisturisers
> exclude ones with retinol in
> show results from cleaned products that match users wants
> user can now scroll through a list of items that has their wants
>user can click on a product from the list and is sent to the boots website for that product
>user can purchase product from website blah blah blah

i initally wanted the app to webscrape to have updated prices & products from the boots website (boots.co.uk) but was having issues with webscraping, so i made the csv file by hand
the app is currently only scraping like 60 items from the csv, id like to incorporate more but for now i just need to get it working before adding more data :-)
