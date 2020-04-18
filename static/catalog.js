function addCards(cards) {
    console.log(cards);

    cards.forEach(function(card) {
        var li = document.createElement('li');
        var image = document.createElement('img');
        image.src = card[5];

        li.append(image)
        document.getElementById('cardList').appendChild(li);
    })
}