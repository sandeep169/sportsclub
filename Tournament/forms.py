from django import  forms

class AddTournament(forms.Form) :
    tour_name = forms.CharField(max_length=100)
    venue = forms.CharField(widget=forms.Textarea)
    tour_start_date = forms.DateField()
    reg_close_date = forms.DateField()
    organiser_name = forms.CharField(widget=forms.Textarea,required=False)
    prize = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea,required=False)
    total_team = forms.IntegerField(required=False)
    tour_img = forms.ImageField(required=False)


# class AddChess(forms.Form) :
#     tour_name = forms.CharField(max_length=100)
#     venue = forms.CharField(widget=forms.Textarea)
#     tour_start_date = forms.DateField()
#     reg_close_date = forms.DateField()
#     organiser_name = forms.CharField(widget=forms.Textarea)
#     prize = forms.CharField(widget=forms.Textarea)
#     description = forms.CharField(widget=forms.Textarea,required=False)
#     total_team = forms.IntegerField(required=False)
#     tour_imgs = forms.ImageField(required=False)
#
# class AddCricket(forms.Form) :
#     tour_name = forms.CharField(max_length=100)
#     venue = forms.CharField(widget=forms.Textarea)
#     tour_start_date = forms.DateField()
#     reg_close_date = forms.DateField()
#     organiser_name = forms.CharField(widget=forms.Textarea)
#     prize = forms.CharField(widget=forms.Textarea)
#     description = forms.CharField(widget=forms.Textarea,required=False)
#     total_team = forms.IntegerField(required=False)
#     tour_img = forms.ImageField(required=False)
#
# class AddTableTennis(forms.Form) :
#     tour_name = forms.CharField(max_length=100)
#     venue = forms.CharField(widget=forms.Textarea)
#     tour_start_date = forms.DateField()
#     reg_close_date = forms.DateField()
#     organiser_name = forms.CharField(widget=forms.Textarea)
#     prize = forms.CharField(widget=forms.Textarea)
#     description = forms.CharField(widget=forms.Textarea,required=False)
#     total_team = forms.IntegerField(required=False)
#     tour_img = forms.ImageField(required=False)
#