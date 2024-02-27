# Generated by Django 4.1.2 on 2023-12-24 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUserChartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeaddress', models.IntegerField(choices=[(1, 'Domestic'), (2, 'Overseas')], default=1)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('zipcode', models.CharField(default='-', max_length=255)),
                ('is_primary', models.BooleanField(default=False)),
                ('rt', models.CharField(blank=True, max_length=5, null=True)),
                ('rw', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('kode', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Diproses'), (3, 'Selesai'), (4, 'Confirm')], default=1)),
                ('tanggal_dikirim', models.DateTimeField(blank=True, null=True)),
                ('tanggal_selesai', models.DateTimeField(blank=True, null=True)),
                ('status_pembayaran', models.IntegerField(choices=[(1, 'Pending'), (2, 'Diproses'), (3, 'Selesai'), (4, 'Confirm')], default=1)),
                ('status_toko', models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Diproses'), (3, 'Dikirim'), (4, 'Confirm')], default=0, null=True)),
                ('nomor_resi', models.CharField(blank=True, max_length=255, null=True)),
                ('catatan', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_cart', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GambarProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='produk_image/')),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=255, unique=True)),
                ('icon', models.FileField(upload_to='icon_kategori')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('stok_produk', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('stok', models.IntegerField(default=0)),
                ('is_promo', models.IntegerField(default=False)),
                ('is_archive', models.BooleanField(default=False)),
                ('berat', models.FloatField(default=0)),
                ('lebar', models.FloatField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProdukChartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('stok_produk', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('stok', models.IntegerField(default=0)),
                ('is_promo', models.IntegerField(default=False)),
                ('berat', models.FloatField(default=0)),
                ('lebar', models.FloatField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProdukStok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProdukTransaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_out', models.DateTimeField(auto_created=True)),
                ('date_in', models.DateTimeField(auto_created=True)),
                ('kode_transaksi', models.CharField(max_length=255)),
                ('jenis', models.IntegerField(choices=[(1, 'Stok awal'), (2, 'Stok tambahan')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipeProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(blank=True, max_length=255, null=True)),
                ('no_telepon', models.CharField(blank=True, max_length=255, null=True)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, default='ID', max_length=4, null=True)),
                ('typeuser', models.IntegerField(choices=[(1, 'Domestic'), (2, 'Overseas')], default=1)),
                ('token', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarnaProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UlasanCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pengiriman', models.FloatField(default=0)),
                ('produk', models.FloatField(default=0)),
                ('catatan', models.TextField(blank=True, null=True)),
                ('cart', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='produk.cart')),
                ('produkitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produk.produk')),
            ],
        ),
        migrations.CreateModel(
            name='StoreCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField()),
                ('coin', models.FloatField(blank=True, default=0, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.usercartitem')),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddressCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('rt', models.CharField(blank=True, max_length=10, null=True)),
                ('rw', models.CharField(blank=True, max_length=10, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('is_primary', models.BooleanField(default=False)),
                ('distric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.distric')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.provinsi')),
                ('regency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.regency')),
            ],
        ),
    ]
