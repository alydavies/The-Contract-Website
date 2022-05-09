from itertools import chain

from account.models import Account
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
import account.views
from django.core.exceptions import PermissionDenied

# Create your views here.
from django.urls import reverse

from characters.models import Character
from powers.models import Power_Full, Enhancement, Drawback, Parameter, Base_Power, SYS_LEGACY_POWERS, SYS_PS2

from games.models import GAME_STATUS, Scenario
from hgapp.forms import SignupForm
from blog.models import Post
from info.models import FrontPageInfo
from cells.models import WorldEvent


class SignupView(account.views.SignupView):
   form_class = SignupForm

   def create_account(self, form):
       return Account.create(request=self.request, user=self.created_user, create_email=False, timezone=form.cleaned_data["timezone"])


class LoginView(account.views.LoginView):
    def get_initial(self):
        return {
            "remember": True
        }


class PasswordResetTokenView(account.views.PasswordResetTokenView):
    def get_context_data(self, **kwargs):
        ctx = super(PasswordResetTokenView, self).get_context_data(**kwargs)
        ctx["user"] = self.get_user()
        return ctx

def home(request):
    if request.user.is_anonymous:
        info = FrontPageInfo.objects.first()
        context = {
            'info': info,
        }
        return render(request, 'logged_out_homepage.html', context)
    else:
        if hasattr(request.user, 'profile'):
            if not request.user.profile.confirmed_agreements:
                return HttpResponseRedirect(reverse('profiles:profiles_terms'))
        my_characters = request.user.character_set.filter(is_deleted=False).order_by('name').all()
        living_characters = [x for x in my_characters if x.is_dead() == False]
        dead_characters = [x for x in my_characters if x.is_dead() == True]
        my_powers = request.user.power_full_set.filter(is_deleted=False).order_by('name').all()
        my_scenarios = request.user.scenario_creator.order_by("title").all()
        new_players = User.objects.order_by('-date_joined')[:6]
        new_powers = Power_Full.objects.filter(private=False, is_deleted=False).order_by('-id')[:6]
        new_characters = Character.objects.filter(private=False, is_deleted=False).order_by('-id')[:6]
        latest_blog_post = Post.objects.current().select_related("section", "blog").first()
        upcoming_games_running = request.user.game_creator.filter(status=GAME_STATUS[0][0]).all()
        upcoming_games_invited = request.user.game_invite_set.filter(relevant_game__status=GAME_STATUS[0][0], is_declined=False).all()
        active_games_attending = request.user.game_set.filter(status=GAME_STATUS[1][0])
        active_games_creator = request.user.game_creator.filter(status=GAME_STATUS[1][0])
        active_games = list(chain(active_games_attending, active_games_creator))
        avail_improvements = request.user.profile.get_avail_improvements()
        avail_charon_coins = request.user.profile.get_avail_charon_coins()
        avail_exp_rewards = request.user.profile.get_avail_exp_rewards()
        cells = request.user.cell_set.all()
        cell_ids = set(request.user.cell_set.values_list('id', flat=True).all())
        world_events = WorldEvent.objects.filter(parent_cell__id__in=cell_ids).order_by('-created_date').all()
        cell_invites = request.user.cellinvite_set.filter(membership=None).filter(is_declined=False).all()
        attendance_invites_to_confirm = request.user.game_invite_set.filter(attendance__is_confirmed=False).exclude(is_declined=True).all()
        context = {
            'living_characters': living_characters,
            'dead_characters': dead_characters,
            'powers': my_powers,
            'my_scenarios': my_scenarios,
            'new_players': new_players,
            'new_powers': new_powers,
            'new_characters': new_characters,
            'upcoming_games_running': upcoming_games_running,
            'upcoming_games_invited': upcoming_games_invited,
            'active_games': active_games,
            'avail_improvements': avail_improvements,
            'avail_charon_coins': avail_charon_coins,
            'cells': cells,
            'cell_invites': cell_invites,
            'world_events': world_events[:3],
            'attendance_invites_to_confirm': attendance_invites_to_confirm,
            'avail_exp_rewards': avail_exp_rewards,
            'latest_blog_post': latest_blog_post,
        }
        return render(request, 'logged_in_homepage.html', context)

def csrf_failure(request, reason=""):
    raise PermissionDenied("CSRF token failure. Refresh form and try again.")