import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from profiles.models import UserAppliedMember, UserCodeGenerator, UserSettingsMember
from store.models import UserStore

from ..base_view import FrontPage


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class RegisterMember(FrontPage):
    def post(self, request):
        userprofile = request.user

        userstore = UserStore()
        userstore.users = userprofile
        userstore.nama = userprofile.name
        userstore.deskripsi = "-"
        userstore.email = request.POST.get("email")
        userstore.telpon = request.POST.get("nomor")
        userstore.save()

        userapplied = UserAppliedMember()
        userapplied.user = userprofile
        userapplied.is_accept = False
        userapplied.name = request.POST.get("name", request.user.username)
        userapplied.email = request.POST.get("email", request.user.email)
        userapplied.nomor = request.POST.get("nomor", "081")
        userapplied.accept_date = datetime.datetime.now()
        userapplied.save()
        return redirect(reverse("register_member"))

    def get(self, request):
        applied = UserAppliedMember.objects.filter(
            user_id=request.user.id, is_accept=False
        )
        accept = False
        if applied.exists():
            applied = applied.first()
            accept = True
        applied_true = UserAppliedMember.objects.filter(
            user_id=request.user.id, is_accept=True
        )
        if applied_true.exists():
            applied_true = applied_true.first()
            code = UserCodeGenerator.objects.filter(user_apply_id=applied_true.id)
            if code.exists():
                codes = code.first()
                if codes.is_active:
                    return redirect(reverse("register_member_code"))
        usersetting = UserSettingsMember.objects.filter(user_id=request.user.id)
        if usersetting.exists():
            usersetting = usersetting.first()
            if usersetting:
                return redirect(reverse("profile"))
        return render(request, "member/register.html", {"register": accept})
