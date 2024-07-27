from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render

from frontend.models import Pengumuman
from master.models import Negara
from produk.models import Kategori, Produk

from ..models import Banner
from .base_view import FrontPage


class Home(FrontPage):
    def get(self, request):
        produk = Produk.objects.annotate(count_star=Avg("ulasancart__produk"))
        produk_paginator = Paginator(produk, 10)
        page_number = request.GET.get("page", 1)
        produk_page = produk_paginator.page(page_number)
        # Pengumuman data
        pengumuman = Pengumuman.objects.filter(is_active=True)
        pengumuman = pengumuman.first()

        # Languange list
        languages = Negara.objects.all()

        kategori = []
        banner = Banner.objects.all()

        try:
            kategori = Kategori.objects.all()
        except Exception as e:
            print(e)
            kategori = []

        return render(
            request,
            "home/index.html",
            {
                "produk": produk_page,
                "kategori": kategori,
                "banner": banner,
                "range_value": range(1, 6),
                "pengumuman": pengumuman,
                "languages": languages,
            },
        )
