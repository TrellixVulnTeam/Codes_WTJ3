# Generated by Django 3.2.9 on 2021-11-09 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('open_time', models.DateTimeField(auto_now_add=True)),
                ('balance', models.FloatField(default=0.0)),
                ('report_loss', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(default='123456', max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('A', 'admin'), ('E', 'employee'), ('S', 'r_staff'), ('M', 'r_manager'), ('D', 'r_delivery')], default='employee', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('building', models.CharField(max_length=255)),
                ('floor', models.IntegerField(default=1)),
                ('room', models.CharField(default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('dish_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('price', models.FloatField(default=0.0)),
                ('picture', models.ImageField(upload_to='')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('order_status', models.CharField(choices=[('0', '预定状态'), ('1', '订单开始'), ('2', '完成支付'), ('3', '完成备餐'), ('4', '完成接单'), ('5', '完成送达')], default='预定状态', max_length=20)),
                ('build_time', models.DateTimeField()),
                ('payment_time', models.DateTimeField()),
                ('meal_complete_time', models.DateTimeField()),
                ('accept_order_time', models.DateTimeField()),
                ('delivery_time', models.DateTimeField()),
                ('remark', models.CharField(max_length=256)),
                ('eat_in_store', models.CharField(choices=[('T', '堂食'), ('W', '外送')], max_length=20)),
                ('specify_delivery_time', models.DateTimeField()),
                ('payment_method', models.CharField(choices=[('W', '微信支付'), ('Z', '支付宝'), ('Y', '余额支付')], max_length=20)),
                ('payment_amount', models.FloatField()),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee1', to='TakeOutSystem.employee')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.location')),
                ('payment_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.balance_account')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TakeOutSystem.order')),
                ('time', models.DateTimeField()),
                ('type', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=255)),
                ('feedback', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='turnover',
            fields=[
                ('turn_id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('business_type', models.CharField(choices=[('Z', '支付'), ('C', '充值')], max_length=20)),
                ('amount', models.FloatField(default=0)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.balance_account')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.turnover'),
        ),
        migrations.AddField(
            model_name='order',
            name='r_delivery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee3', to='TakeOutSystem.employee'),
        ),
        migrations.AddField(
            model_name='order',
            name='r_staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee2', to='TakeOutSystem.employee'),
        ),
        migrations.CreateModel(
            name='employee_phone',
            fields=[
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.employee')),
            ],
        ),
        migrations.AddField(
            model_name='balance_account',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.employee'),
        ),
        migrations.CreateModel(
            name='order_menu',
            fields=[
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TakeOutSystem.order')),
                ('amount', models.IntegerField(default=1)),
                ('dish_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TakeOutSystem.menu')),
            ],
        ),
    ]
