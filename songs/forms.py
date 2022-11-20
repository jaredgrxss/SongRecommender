from django import forms 


class RandomSong(forms.Form):
    GENRE_CHIOCES = (
        ('country','Country'),
        ('alternative','Alternative'),
        ('hip-hop','Hip-Hop'),
        ('r-n-b','R&B'),
        ('indie','Indie'),
        ('rock','Rock'),
        ('pop','Pop'),
        ('chill','Chill'),
        ('sad','Sad'),
        ('romance','Romance'),
        ('disney','Disney'),
    )
    genre = forms.ChoiceField(choices=GENRE_CHIOCES,label='Genre')



class PlaylistGeneratorForm(forms.Form):
    GENRE_CHIOCES = (
        ('country','Country'),
        ('alternative','Alternative'),
        ('hip-hop','Hip-Hop'),
        ('r-n-b','R&B'),
        ('indie','Indie'),
        ('rock','Rock'),
        ('pop','Pop'),
        ('chill','Chill'),
        ('sad','Sad'),
        ('romance','Romance'),
        ('disney','Disney'),
    )

    genre1 = forms.ChoiceField(choices=GENRE_CHIOCES,label="My favorite genre")
    genre2 = forms.ChoiceField(choices=GENRE_CHIOCES,label="A close second")
    genre3 = forms.ChoiceField(choices=GENRE_CHIOCES,label='Explore this genre')
    favorite_song = forms.CharField(label='Finally, enter the name of your current favorite song')

    def clean(self):
        one, two, three = self.cleaned_data['genre1'], self.cleaned_data['genre2'], self.cleaned_data['genre3']
        if one == two or one == three or two == three:
            raise forms.ValidationError("Make sure all of your genres are different!")
        return super().clean()
