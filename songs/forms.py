from django import forms 


class RandomSong(forms.Form):
    GENRE_CHIOCES = [
        'Country',
        'Rap',
        'Hip-Hop',
        'R&B',
        'Blues',
        'Alternative',
        'Indie',
        'Rock',
        'Pop'
    ]
    genre = forms.ChoiceField(choices=GENRE_CHIOCES)