import twitch

helix = twitch.Helix('0ty8ioia25p981k0jlzn3bkk0cor7', 'ikx57p55yua98r1obfyzz6x6mv70b2')

# Twitch Chat

twitch.Chat(channel='hypercoolness30', nickname='hypercoolness30', oauth='oauth:brd9ew3syobq4kxnk4mtf2g9yi2r8y').subscribe(
        lambda message: print(message.channel, message.user.display_name, message.text))